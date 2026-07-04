https://www.youtube.com/watch?v=4R9J-NGiALM
https://www.osc.edu/resources/getting_started/howto/howto_use_address_sanitizer

gcc main.c -o main -fsanitize=address -g

ASAN - Address Sanitizer -fsanitize=address
UBSAN - Undefined Behavior Sanitizer -fsanitize=undefined
TSAN - Thread Sanitizer (used for proving the presence of — data races. must be used at compile time and link time.) -fsanitize=thread

To make ASAN and UBSAN break on error:
    * export ASAN_OPTIONS=abort_on_error=1:halt_on_error=1
    * export UBSAN_OPTIONS=abort_on_error=1:halt_on_error=1

Address Sanitizer is a tool developed by Google detect memory access error such as use-after-free and memory leaks. 

It's helpful to compile the code with debug symbols.
AddressSanitizer will print line numbers if debug symbols are present. To do this, add the "-g" flag.

Example 1 (Missing free()):

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
int main(int argc, const char *argv[]) {
    char *s = malloc(100);
    strcpy(s, "Hello world!");
    printf("string is: %s\n", s);
    return 0;
}
```

Building with:
```text
gcc leak.c -o leak -fsanitize=address -static-libasan
```

```text
=================================================================
==235624==ERROR: LeakSanitizer: detected memory leaks
 
Direct leak of 100 byte(s) in 1 object(s) allocated from:
    #0 0x4eaaa8 in __interceptor_malloc ../../.././libsanitizer/asan/asan_malloc_linux.cc:144
    #1 0x5283dd in main /users/PZS0710/edanish/test/asan/leak.c:6
    #2 0x2b0c29909544 in __libc_start_main (/lib64/libc.so.6+0x22544)
 
SUMMARY: AddressSanitizer: 100 byte(s) leaked in 1 allocation(s).
```

On line 6, memory was allocated that caused the memory leak.

Example 2 (Use after free):

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
int main(int argc, const char *argv[]) {
    char *s = malloc(100);
    free(s);
    strcpy(s, "Hello world!");
    printf("string is: %s\n", s);
    return 0;
}
```

```text
gcc uaf.c -o uaf -fsanitize=address -static-libasan
```
```text
=================================================================
==244157==ERROR: AddressSanitizer: heap-use-after-free on address 0x60b0000000f0 at pc 0x00000047a560 bp 0x7ffcdf0d59f0 sp 0x7ffcdf0d51a0
WRITE of size 13 at 0x60b0000000f0 thread T0
    #0 0x47a55f in __interceptor_memcpy ../../.././libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:790
    #1 0x528403 in main /users/PZS0710/edanish/test/asan/uaf.c:8
    #2 0x2b47dd204544 in __libc_start_main (/lib64/libc.so.6+0x22544)
    #3 0x405f5c  (/users/PZS0710/edanish/test/asan/uaf+0x405f5c)
 
0x60b0000000f0 is located 0 bytes inside of 100-byte region [0x60b0000000f0,0x60b000000154)
freed by thread T0 here:
    #0 0x4ea6f7 in __interceptor_free ../../.././libsanitizer/asan/asan_malloc_linux.cc:122
    #1 0x5283ed in main /users/PZS0710/edanish/test/asan/uaf.c:7
    #2 0x2b47dd204544 in __libc_start_main (/lib64/libc.so.6+0x22544)
 
previously allocated by thread T0 here:
    #0 0x4eaaa8 in __interceptor_malloc ../../.././libsanitizer/asan/asan_malloc_linux.cc:144
    #1 0x5283dd in main /users/PZS0710/edanish/test/asan/uaf.c:6
    #2 0x2b47dd204544 in __libc_start_main (/lib64/libc.so.6+0x22544)
 
SUMMARY: AddressSanitizer: heap-use-after-free ../../.././libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:790 in __interceptor_memcpy
Shadow bytes around the buggy address:
  0x0c167fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c167fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c167fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c167fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c167fff8000: fa fa fa fa fa fa fa fa fd fd fd fd fd fd fd fd
=>0x0c167fff8010: fd fd fd fd fd fa fa fa fa fa fa fa fa fa[fd]fd
  0x0c167fff8020: fd fd fd fd fd fd fd fd fd fd fd fa fa fa fa fa
  0x0c167fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c167fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c167fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c167fff8060: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==244157==ABORTING
```

Starting at the top, we see what AddressSanitizer detected. In this case, a "WRITE" of 13 bytes (from our strcpy). Immediately below that, we get a stack trace of where the write occured.
This tells us that the write occured on line 8 in uaf.c in the function called "main".

Next, AddressSanitizer reports where the memory was located.

Two key pieces of information follow. AddressSanitizer tells us where the memory was freed (the "freed by thread T0 here" section), giving us another stack trace indicating the memory was freed on line 7.
Then, it reports where it was originally allocated ("previously allocated by thread T0 here:"), line 6 in uaf.c.

Example 3 (Heap overflow):

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, const char *argv[]) {
    // whoops, forgot c strings are null-terminated
    // and not enough memory was allocated for the copy
    char *s = malloc(12);
    strcpy(s, "Hello world!");
    printf("string is: %s\n", s);
    free(s);
    return 0;
}
```

Building with:
```text
gcc overflow.c -o overflow -fsanitize=address -static-libasan -g -Wall
```

```text
==168232==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60200000003c at pc 0x000000423454 bp 0x7ffdd58700e0 sp 0x7ffdd586f890
WRITE of size 13 at 0x60200000003c thread T0
    #0 0x423453 in __interceptor_memcpy /apps_src/gnu/8.4.0/src/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:737
    #1 0x5097c9 in main /users/PZS0710/edanish/test/asan/overflow.c:8
    #2 0x2ad93cbd7544 in __libc_start_main (/lib64/libc.so.6+0x22544)
    #3 0x405d7b  (/users/PZS0710/edanish/test/asan/overflow+0x405d7b)
 
0x60200000003c is located 0 bytes to the right of 12-byte region [0x602000000030,0x60200000003c)
allocated by thread T0 here:
    #0 0x4cd5d0 in __interceptor_malloc /apps_src/gnu/8.4.0/src/libsanitizer/asan/asan_malloc_linux.cc:86
    #1 0x5097af in main /users/PZS0710/edanish/test/asan/overflow.c:7
    #2 0x2ad93cbd7544 in __libc_start_main (/lib64/libc.so.6+0x22544)
 
SUMMARY: AddressSanitizer: heap-buffer-overflow /apps_src/gnu/8.4.0/src/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:737 in __interceptor_memcpy
Shadow bytes around the buggy address:
  0x0c047fff7fb0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c047fff8000: fa fa 00 fa fa fa 00[04]fa fa fa fa fa fa fa fa
  0x0c047fff8010: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==168232==ABORTING
```

AddresssSanitizer can also detect heap overflows.
The "Hello world!" string is 13 characters long including the null terminator, but we've only allocated 12 bytes, so the strcpy above will overflow the buffer that was allocated.
It tells us that a heap buffer overflow occured, then goes on to report where the write happened and where the memory was originally allocated.

Example 4 (Delete mismatch CPP):

```cpp
#include <iostream>
#include <cstring>
 
int main(int argc, const char *argv[]) {
    char *cstr = new char[100];
    strcpy(cstr, "Hello World");
    std::cout << cstr << std::endl;
 
    delete cstr;
    return 0;
}
```

Building with:
```text
g++ bad_delete.cxx -o bad_delete -fsanitize=address -static-libasan -g
```

Output:
```text
Hello World
=================================================================
==257438==ERROR: AddressSanitizer: alloc-dealloc-mismatch (operator new [] vs operator delete) on 0x60b000000040
    #0 0x4d0a78 in operator delete(void*, unsigned long) /apps_src/gnu/8.4.0/src/libsanitizer/asan/asan_new_delete.cc:151
    #1 0x509ea8 in main /users/PZS0710/edanish/test/asan/bad_delete.cxx:9
    #2 0x2b8232878544 in __libc_start_main (/lib64/libc.so.6+0x22544)
    #3 0x40642b  (/users/PZS0710/edanish/test/asan/bad_delete+0x40642b)
 
0x60b000000040 is located 0 bytes inside of 100-byte region [0x60b000000040,0x60b0000000a4)
allocated by thread T0 here:
    #0 0x4cf840 in operator new[](unsigned long) /apps_src/gnu/8.4.0/src/libsanitizer/asan/asan_new_delete.cc:93
    #1 0x509e5f in main /users/PZS0710/edanish/test/asan/bad_delete.cxx:5
    #2 0x2b8232878544 in __libc_start_main (/lib64/libc.so.6+0x22544)
 
SUMMARY: AddressSanitizer: alloc-dealloc-mismatch /apps_src/gnu/8.4.0/src/libsanitizer/asan/asan_new_delete.cc:151 in operator delete(void*, unsigned long)
==257438==HINT: if you don't care about these errors you may set ASAN_OPTIONS=alloc_dealloc_mismatch=0
==257438==ABORTING
```

What's the problem here? The memory pointed to by "cstr" was allocated with new[]. An array allocation must be deleted with the delete[] operator, not "delete".
This is similar to the other AddressSanitizer outputs we've looked at. This time, it tells us there's a mismatch between new and delete. It prints a stack trace for where the delete occured (line 9) and also a stack trace for where to allocation occured (line 5)
