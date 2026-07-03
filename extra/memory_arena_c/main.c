#include <stdbool.h>
#include <stdint.h>
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
#define ALIGN_UP_POW2(n, p) (((uint64)(n) + ((uint64)(p)-1)) & ~((uint64)(p)-1))
/*
 * n = 20
 * p = 8
 * 20 + 8 - 1 & ~(8 - 1)
 * 27 & ~7
 * 00011011 & ~(00000111)
 * 00011011 & 11111000 = 00011000 = 24
 */

#define ARENA_BASE_POS (sizeof(mem_arena))
#define ARENA_ALIGN (sizeof(void *))

#define ARENA_PUSH_STRUCT(arena, T) (T *)ArenaPush((arena), sizeof(T), false)
#define ARENA_PUSH_STRUCT_NZ(arena, T) (T *)ArenaPush((arena), sizeof(T), true)
#define ARENA_PUSH_ARRAY(arena, T, n)                                          \
  (T *)ArenaPush((arena), sizeof(T) * (n), false)
#define ARENA_PUSH_ARRAY_NZ(arena, T, n)                                       \
  (T *)ArenaPush((arena), sizeof(T) * (n), true)

typedef struct {
  uint64 ReserveSize;
  uint64 CommitSize;
  uint64 Position;
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

int main(void) {

  mem_arena *PermanentArena = ArenaCreate(MiB(1), MiB(1));

  ArenaDestroy(PermanentArena);
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
  Size = MIN(Size, Arena->Position - ARENA_BASE_POS);
  Arena->Position -= Size;
}

void ArenaPopTo(mem_arena *Arena, uint64 Position) {
  uint64 Size = (Position < Arena->Position) ? Arena->Position - Position : 0;
  ArenaPop(Arena, Size);
}

void ArenaClear(mem_arena *Arena) { ArenaPopTo(Arena, ARENA_BASE_POS); }

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
