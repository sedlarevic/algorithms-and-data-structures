From a blogpost:
https://nullprogram.com/blog/2023/04/29/

Static warnings
  gcc

gcc -Wall -Wextra -Wno-unknown-pragmas -Wdouble-promotion -Wconversion -Wno-sign-conversion -fsanitize=address,undefined -g3


    * -Wall - It enables a large set of basic, highly impactful warnings about questionable code constructs that are likely to be bugs
(e.g., unused variables, uninitialized variables, and return type mismatches).
    * -Wextra - This flag enables an additional set of useful warnings that -Wall misses.
Examples include warnings for override mismatches, signed/unsigned comparisons, and unused parameters.
    * -Wno-unknown-pragmas - Silences warnings when the compiler encounters a #pragma directive it does not recognize.
    * -Wdouble-promotion - Warns you when a float (32-bit) is implicitly promoted to a double (64-bit).
    * -Wconversion - Warns about implicit type conversions that could alter a value or change its sign (e.g., assigning a 64-bit long to a 32-bit int).
    * -Wno-sign-conversion - Disables warnings about implicit conversions between signed and unsigned integers.
    * -fsanitize=... - Check below.
    * -g3 - Generates maximum debug information during compilation.




  msvc (cl)

cl /W4 /wd4146 /wd4245 /D_CRT_SECURE_NO_WARNINGS /fsanitize=address /Z7 main.cpp


    * wd4146 - unary minus operator applied to unsigned type
This warning triggers when a unary minus (-) is applied to an unsigned variable or literal.
Because unsigned types cannot hold negative values, the result wraps around according to modular arithmetic and stays unsigned.
    * wd4245 - conversion from 'type1' to 'type2', signed/unsigned mismatch.
This warning triggers when you initialize or assign a signed variable using an unsigned value (or vice versa)
and the conversion forces a change in how the data is interpreted. E.g. assigning a literal -1 to an unsigned int.
Converting a negative signed integer to an unsigned type causes data wrap-around (e.g., -1 becomes 4294967295 in a 32-bit system)
    * D_CRT_SECURE_NO_WARNINGS
Microsoft considers many standard C library functions (like strcpy, sprintf, scanf, and fopen) unsafe because they do not strictly enforce buffer sizes.
This lack of restriction makes them vulnerable to buffer overflow security exploits.
    * -fsanitize=... - Check below.
    * /RTCcs - Enables two specific Run-Time Error Checks (Run-Time Checks)
      * c - Reports when a value is assigned to a smaller data type and results in a loss of data (e.g., stripping bits)
      * s - Enables stack frame run-time error checking (e.g., catching basic stack buffer overflows or verifying stack pointer integrity). 
    * /Z7 - Generates debug information and stores it directly inside the object (.obj) files instead of creating a separate .pdb (Program Database) file.




Dynamic run-time checks (sanitizers!)
ASAN - Address Sanitizer -fsanitize=address
UBSAN - Undefined Behavior Sanitizer -fsanitize=undefined
TSAN - Thread Sanitizer (used for proving the presence of — data races. must be used at compile time and link time.) -fsanitize=thread

To make ASAN and UBSAN break on error:
    * export ASAN_OPTIONS=abort_on_error=1:halt_on_error=1
    * export UBSAN_OPTIONS=abort_on_error=1:halt_on_error=1

