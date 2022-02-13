"""
https://leetcode.com/problems/read-n-characters-given-read4/

Given a file and assume that you can only read the 
file using a given method read4, implement a 
method to read n characters.

Method read4:
The API read4 reads four consecutive characters 
from file, then writes those characters into 
the buffer array buf4.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much 
like FILE *fp in C.

Definition of read4:
    Parameter:  char[] buf4
    Returns:    int

buf4[] is a destination, not a source. The results 
from read4 will be copied to buf4[].
Below is a high-level example of how read4 works:

File file("abcde"); 
// File is "abcde", initially file pointer (fp) points to 'a'

char[] buf4 = new char[4]; 
// Create buffer with enough space to store characters
read4(buf4); 
// read4 returns 4. Now buf4 = "abcd", fp points to 'e'

read4(buf4); 
// read4 returns 1. Now buf4 = "e", fp points to end of file

read4(buf4); 
// read4 returns 0. Now buf4 = "", fp points to end of file
 

Method read:
By using the read4 method, implement the method 
read that reads n characters from file and store 
it in the buffer array buf. Consider that you 
cannot manipulate file directly.

The return value is the number of actual characters read.

Definition of read:
    Parameters:	char[] buf, int n
    Returns:	int

buf[] is a destination, not a source. You will need 
to write the results to buf[].

Note:
- Consider that you cannot manipulate the file directly. 
The file is only accessible for read4 but not for read.
- The read function will only be called once for each 
test case.
- You may assume the destination buffer array, buf, is 
guaranteed to have enough space for storing n characters.
 
Example 1:
Input: file = "abc", n = 4
Output: 3
Explanation: After calling your read method, buf 
should contain "abc". We read a total of 3 characters 
from the file, so return 3.
Note that "abc" is the file's content, not buf. buf 
is the destination buffer that you will have to 
write the results to.

Example 2:
Input: file = "abcde", n = 5
Output: 5
Explanation: After calling your read method, buf 
should contain "abcde". We read a total of 5 
characters from the file, so return 5.

Example 3:
Input: file = "abcdABCD1234", n = 12
Output: 12
Explanation: After calling your read method, buf should 
contain "abcdABCD1234". We read a total of 12 characters 
from the file, so return 12.

Constraints:
1 <= file.length <= 500
file consist of English letters and digits.
1 <= n <= 1000
"""
from typing import List


def read4(buf4: List[str]):
    # Non-implemented
    return


def read(buf: List[str], n: int, file: str) -> int:
    # Time complexity: O(n)
    # Space complexity: O(4) = O(1)

    # Note: correct implementation of the algorithm,
    # but API function `read4` not implemented

    buf4 = [""] * 4
    read_chars = 0
    while read_chars < n:
        new_chars = min(n - read_chars, read4(buf4))
        if not new_chars:
            break
        buf[read_chars : read_chars + new_chars] = buf4[:new_chars]
        read_chars += new_chars

    return read_chars


if __name__ == "__main__":
    print("-" * 60)
    print("Read N characters given read4")
    print("-" * 60)

    test_cases = [
        # (file, read_calls_n, solutions)
        # where each solution = (read_chars, buf)
        # NOTE: API function `read4` not
        # implemented in this script, so can't run tests
        # ("", 2, (0, "")),
        # ("abc", 2, (2, "ab")),
        # ("abc", 5, (3, "abc")),
        # ("Alfambra", 1, (1, "A")),
        # ("Alfambra", 3, (3, "Alf")),
        # ("Alfambra", 5, (5, "Alfam")),
        # ("Alfambra", 13, (8, "Alfambra")),
    ]

    for file, n, solution in test_cases:

        print("File:", file)
        print("n =", n)

        buf = [""] * n
        result = read(buf=buf, n=n, file=file)
        output = "read:"
        output += " " * (13 - len(output))
        output += f"read chars = {result} "
        output += " " * (35 - len(output))
        buf = "".join(buf)
        output += f"buf = {buf} "
        test_ok = solution == (result, buf)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
