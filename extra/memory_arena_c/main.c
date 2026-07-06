#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef int8_t int8;
typedef int16_t int16;
typedef int32_t int32;
typedef int64_t int64;
typedef uint8_t uint8;
typedef uint16_t uint16;
typedef uint32_t uint32;
typedef uint64_t uint64;
typedef int32 bool32;

#define KiB(val) ((uint64)(val) << 10)
#define MiB(val) ((uint64)(val) << 20)
#define GiB(val) ((uint64)(val) << 30)

#define MAX(a, b) (((a) > (b)) ? (a) : (b))
#define MIN(a, b) (((a) < (b)) ? (a) : (b))

/*
 * n = 20
 * p = 8
 * 20 + 8 - 1 & ~(8 - 1)
 * 27 & ~7
 * 00011011 & ~(00000111)
 * 00011011 & 11111000 = 00011000 = 24
 */
#define ALIGN_UP_POW2(n, p) (((uint64)(n) + ((uint64)(p)-1)) & ~((uint64)(p)-1))
#define ARENA_BASE_POS (sizeof(mem_arena))
#define ARENA_ALIGN (sizeof(void *))

#define ARENA_PUSH_STRUCT(arena, T) (T *)ArenaPush((arena), sizeof(T), false)
#define ARENA_PUSH_STRUCT_NZ(arena, T) (T *)ArenaPush((arena), sizeof(T), true)
#define ARENA_PUSH_ARRAY(arena, T, n)                                          \
  (T *)ArenaPush((arena), sizeof(T) * (n), false)
#define ARENA_PUSH_ARRAY_NZ(arena, T, n)                                       \
  (T *)ArenaPush((arena), sizeof(T) * (n), true)

/*
 * To reserve: The OS reserves range of virtual addresses inside this process,
 * so future allocations in this process will not use that address range.
 * To commit: The OS makes pages in that reserved range readeable/writeable.
 */

typedef struct {
  // How much total virtual address space arena is allowed to use
  uint64 ReserveSize;

  // In which chunks is memory phisically activated
  uint64 CommitSize;

  // Where is currently the end of used memory
  uint64 Position;

  // Until which position is the memory actually commited (usable for
  // read/write)
  uint64 CommitPosition;

} mem_arena;

mem_arena *ArenaCreate(uint64 ReserveSize, uint64 CommitSize);
void ArenaDestroy(mem_arena *Arena);
void *ArenaPush(mem_arena *Arena, uint64 Size, bool32 NonZero);
void ArenaPop(mem_arena *Arena, uint64 Size);
void ArenaPopTo(mem_arena *Arena, uint64 Position);
void ArenaClear(mem_arena *Arena);

uint32 PlatformGetPageSize(void);
void *PlatformMemoryReserve(uint64 Size);
bool32 PlatformMemoryCommit(void *MemoryPointer, uint64 Size);
bool32 PlatformMemoryDecommit(void *MemoryPointer, uint64 Size);
bool32 PlatformMemoryRelease(void *MemoryPointer, uint64 Size);

void ArenaDebugPrint(mem_arena *Arena, const char *Label);

int main(void) {

  mem_arena *A = ArenaCreate(KiB(64), KiB(4));
  if (!A) {
    return 1;
  }
  ArenaDebugPrint(A, "After create");

  ArenaPush(A, KiB(1), false);
  ArenaDebugPrint(A, "After push 1 KiB");

  ArenaPush(A, KiB(2), false);
  ArenaDebugPrint(A, "After push 2 KiB");

  ArenaPush(A, KiB(2), false);
  ArenaDebugPrint(A, "After push 2 KiB again");

  ArenaPush(A, KiB(10), false);
  ArenaDebugPrint(A, "After push 10 KiB");

  ArenaPush(A, KiB(25), false);
  ArenaDebugPrint(A, "After push 25 KiB");

  ArenaClear(A);
  ArenaDebugPrint(A, "After clear");

  ArenaDestroy(A);
  return 0;
}

mem_arena *ArenaCreate(uint64 ReserveSize, uint64 CommitSize) {
  uint32 PageSize = PlatformGetPageSize();
  ReserveSize = ALIGN_UP_POW2(ReserveSize, PageSize);
  CommitSize = ALIGN_UP_POW2(CommitSize, PageSize);

  mem_arena *Arena = PlatformMemoryReserve(ReserveSize);

  if (!Arena) {
    return NULL;
  }

  if (!PlatformMemoryCommit(Arena, CommitSize)) {
    PlatformMemoryRelease(Arena, ReserveSize);
    return NULL;
  }

  Arena->ReserveSize = ReserveSize;
  Arena->CommitSize = CommitSize;
  Arena->Position = ARENA_BASE_POS;
  Arena->CommitPosition = CommitSize;

  return Arena;
}

void ArenaDestroy(mem_arena *Arena) {
  if (Arena) {
    PlatformMemoryRelease(Arena, Arena->ReserveSize);
  }
}

void *ArenaPush(mem_arena *Arena, uint64 Size, bool32 NonZero) {

  uint64 AlignedPosition = ALIGN_UP_POW2(Arena->Position, ARENA_ALIGN);
  uint64 NewPosition = AlignedPosition + Size;
  if (NewPosition > Arena->ReserveSize) {
    return NULL;
  }
  if (NewPosition > Arena->CommitPosition) {
    uint64 NewCommitPosition = NewPosition;
    /*
        Commit memory in CommitSize chunks.
        NewPosition = first byte past the requested allocation.
        Round NewPosition up to the next CommitSize boundary:

            CommitSize = 10

            23 -> 23 + 9 = 32
                 32 % 10 = 2
                 32 - 2 = 30
            20 -> 20 + 9 = 29
                 29 % 10 = 9
                 29 - 9 = 20

        Then commit only the missing range:

            |========|+++++++|-------|
                     ^
              old CommitPosition

            '=' already committed
            '+' newly committed
    */
    NewCommitPosition += Arena->CommitSize - 1;
    NewCommitPosition -= NewCommitPosition % Arena->CommitSize;
    NewCommitPosition = MIN(NewCommitPosition, Arena->ReserveSize);

    uint8 *Memory = (uint8 *)Arena + Arena->CommitPosition;
    uint64 CommitSize = NewCommitPosition - Arena->CommitPosition;

    if (!PlatformMemoryCommit(Memory, CommitSize)) {
      return NULL;
    }
    Arena->CommitPosition = NewCommitPosition;
  }
  uint8 *Out = (uint8 *)Arena + AlignedPosition;

  if (!NonZero) {
    memset(Out, 0, Size);
  }

  Arena->Position = NewPosition;
  return Out;
}

void ArenaPop(mem_arena *Arena, uint64 Size) {
  // NOTE: Committed memory stays committed after pop.
  Size = MIN(Size, Arena->Position - ARENA_BASE_POS);
  Arena->Position -= Size;
}

void ArenaPopTo(mem_arena *Arena, uint64 Position) {
  uint64 Size = (Position < Arena->Position) ? Arena->Position - Position : 0;
  ArenaPop(Arena, Size);
}

void ArenaClear(mem_arena *Arena) { ArenaPopTo(Arena, ARENA_BASE_POS); }

void ArenaDebugPrint(mem_arena *Arena, const char *Label) {

  printf("\n%s\n", Label);
  printf("Position:          %llu\n", Arena->Position);
  printf("CommitPosition:    %llu\n", Arena->CommitPosition);
  printf("ReserveSize:       %llu\n", Arena->ReserveSize);

  int Width = 64;

  for (int i = 0; i < Width; ++i) {

    uint64 At = (Arena->ReserveSize * i) / Width;
    if (At < Arena->Position) {
      putchar('#'); // used
    } else if (At < Arena->CommitPosition) {
      putchar('='); // commited but unused
    } else {
      putchar('-'); // reserved but uncommited
    }
  }
  putchar('\n');
}
#ifdef _WIN32
#include <windows.h>
uint32 PlatformGetPageSize(void) {
  SYSTEM_INFO SystemInfo = {0};
  GetSystemInfo(&SystemInfo);

  return SystemInfo.dwPageSize;
}

void *PlatformMemoryReserve(uint64 Size) {
  return VirtualAlloc(NULL, Size, MEM_RESERVE, PAGE_READWRITE);
}

bool32 PlatformMemoryCommit(void *MemoryPointer, uint64 Size) {
  void *Result = VirtualAlloc(MemoryPointer, Size, MEM_COMMIT, PAGE_READWRITE);
  return Result != NULL;
}

bool32 PlatformMemoryDecommit(void *MemoryPointer, uint64 Size) {
  return VirtualFree(MemoryPointer, Size, MEM_DECOMMIT);
}

bool32 PlatformMemoryRelease(void *MemoryPointer, uint64 Size) {
  return VirtualFree(MemoryPointer, 0, MEM_RELEASE);
}

#else
#include <sys/mman.h>
#include <unistd.h>
#ifndef MAP_ANONYMOUS
#define MAP_ANONYMOUS MAP_ANON
#endif
uint32 PlatformGetPageSize(void) { return getpagesize(); }

void *PlatformMemoryReserve(uint64 Size) {
  void *Result =
      mmap(NULL, Size, PROT_NONE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
  return Result == MAP_FAILED ? NULL : Result;
}

bool32 PlatformMemoryCommit(void *MemoryPointer, uint64 Size) {
  void *Result = mmap(MemoryPointer, Size, PROT_READ | PROT_WRITE,
                      MAP_PRIVATE | MAP_ANONYMOUS | MAP_FIXED, -1, 0);
  return Result != MAP_FAILED;
}
bool32 PlatformMemoryDecommit(void *MemoryPointer, uint64 Size) {
  void *Result = mmap(MemoryPointer, Size, PROT_NONE,
                      MAP_PRIVATE | MAP_ANONYMOUS | MAP_FIXED, -1, 0);
  return Result != MAP_FAILED;
}
bool32 PlatformMemoryRelease(void *MemoryPointer, uint64 Size) {
  return munmap(MemoryPointer, Size) == 0;
}
#endif
