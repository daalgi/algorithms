"""
https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

Given a file and assume that you can only read the 
file using a given method read4, implement a method 
read to read n characters. Your method read may be 
called multiple times.

Method read4:
The API read4 reads four consecutive characters 
from file, then writes those characters into 
the buffer array buf4.

The return value is the number of actual 
characters read.

Note that read4() has its own file pointer, 
much like FILE *fp in C.

Definition of read4:
    Parameter:  char[] buf4
    Returns:    int

buf4[] is a destination, not a source. The results 
from read4 will be copied to buf4[].

Below is a high-level example of how read4 works:

File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
char[] buf4 = new char[4]; // Create buffer with enough space to store characters
read4(buf4); // read4 returns 4. Now buf4 = "abcd", fp points to 'e'
read4(buf4); // read4 returns 1. Now buf4 = "e", fp points to end of file
read4(buf4); // read4 returns 0. Now buf4 = "", fp points to end of file
 
Method read:
By using the read4 method, implement the method read 
that reads n characters from file and store it in 
the buffer array buf. Consider that you cannot 
manipulate file directly.

The return value is the number of actual characters read.

Definition of read:
    Parameters:	char[] buf, int n
    Returns:	int

buf[] is a destination, not a source. You will need 
to write the results to buf[].

Note:
- Consider that you cannot manipulate the file directly. 
The file is only accessible for read4 but not for read.
- The read function may be called multiple times.
- Please remember to RESET your class variables declared 
in Solution, as static/class variables are persisted 
across multiple test cases. Please see here for more 
details.
- You may assume the destination buffer array, buf, is 
guaranteed to have enough space for storing n characters.
- It is guaranteed that in a given test case the same 
buffer buf is called by read.

Example 1:
Input: file = "abc", queries = [1,2,1]
Output: [1,2,0]
Explanation: The test case represents the following scenario:
File file("abc");
Solution sol;
sol.read(buf, 1); 
// After calling your read method, buf should 
contain "a". We read a total of 1 character from 
the file, so return 1.

sol.read(buf, 2); 
// Now buf should contain "bc". We read a total of 2 
characters from the file, so return 2.

sol.read(buf, 1); 
// We have reached the end of file, no more characters 
can be read. So return 0.

Assume buf is allocated and guaranteed to have enough 
space for storing all characters from the file.

Example 2:
Input: file = "abc", queries = [4,1]
Output: [3,0]
Explanation: The test case represents the following scenario:
File file("abc");
Solution sol;
sol.read(buf, 4); 
// After calling your read method, buf should contain "abc". 
We read a total of 3 characters from the file, so return 3.

sol.read(buf, 1); 
// We have reached the end of file, no more characters 
can be read. So return 0.

Constraints:
1 <= file.length <= 500
file consist of English letters and digits.
1 <= queries.length <= 10
1 <= queries[i] <= 500
"""
from collections import deque
from typing import List


class Read:
    def __init__(self, file: str):
        # `read4` API parameters, used for testing
        self.file = file
        self.size = len(file)
        self.index = 0

    def read4(self, buf4: List[str]):
        # API function, implemented inside the class
        # only for testing purposes, not part of the question
        new_chars = 0
        while self.index < self.size and new_chars < 4:
            buf4[new_chars] = self.file[self.index]
            self.index += 1
            new_chars += 1
        return new_chars


class ReadWithQueue(Read):
    def __init__(self, file: str):
        self.q = deque([])
        super(ReadWithQueue, self).__init__(file)

    def read(self, buf: List[str], n: int) -> int:
        # Time complexity: O(n)
        # Space complexity: O(4) = O(1)

        read_chars = 0
        while read_chars < n:

            if self.q:
                buf[read_chars] = self.q.popleft()
                read_chars += 1

            else:
                buf4 = [""] * 4
                new_chars = self.read4(buf4)
                if not new_chars:
                    break
                for i in range(new_chars):
                    self.q.append(buf4[i])

        return read_chars


class ReadWithPointer(Read):
    def __init__(self, file: str):
        # Note: according to the problem statement,
        # we DON'T HAVE access to `read4` parameters,
        # so the current implementation
        # shouldn't be possible, since in this
        # solution we control the current
        # pointer of the `file` of the API.
        self.index = 0
        super(ReadWithPointer, self).__init__(file)

    def read(self, buf: List[str], n: int) -> int:
        # Time complexity: O(n)
        # Space complexity: O(4) = O(1)
        read_chars = 0
        while read_chars < n:

            buf4 = [""] * 4
            new_chars = self.read4(buf4)
            i = 0
            while i < new_chars and read_chars < n:
                buf[read_chars] = buf4[i]
                i += 1
                read_chars += 1

            # If the previous loop ended due to `read_chars == n`,
            # position the `file` pointer `index` at the
            # character to be read the next time `read` is called
            if read_chars == n:
                self.index -= new_chars - i

            # If we reached the end of the file we have
            # `new_chars < 4`, so we can exit the loop
            if new_chars < 4:
                break

        return read_chars


if __name__ == "__main__":
    print("-" * 60)
    print("Read N characters given read4 II - call multiple times")
    print("-" * 60)

    test_cases = [
        # (file, read_calls_n, solutions)
        # where each solution = (read_chars, buf)
        ("", [1, 2], [(0, ""), (0, "")]),
        ("abc", [1, 2, 1], [(1, "a"), (2, "bc"), (0, "")]),
        ("Alfambra", [3, 1, 8], [(3, "Alf"), (1, "a"), (4, "mbra")]),
        ("Little wing", [3, 1, 4], [(3, "Lit"), (1, "t"), (4, "le w")]),
        ("Little wing", [3, 1, 5], [(3, "Lit"), (1, "t"), (5, "le wi")]),
        ("pleistoceno", [1, 1, 1, 2], [(1, "p"), (1, "l"), (1, "e"), (2, "is")]),
    ]

    for file, read_calls_n, solutions in test_cases:

        print("File:", file)
        rq = ReadWithQueue(file)
        rp = ReadWithPointer(file)

        for n, solution in zip(read_calls_n, solutions):
            print(">> n =", n)

            buf = [""] * n
            result = rq.read(buf=buf, n=n)
            output = "ReadWithQueue:"
            output += " " * (17 - len(output))
            output += f"read chars = {result} "
            output += " " * (35 - len(output))
            buf = "".join(buf)
            output += f"buf = {buf} "
            test_ok = solution == (result, buf)
            output += " " * (55 - len(output))
            output += f'Test: {"OK" if test_ok else "NOT OK"}'
            print(output)

            buf = [""] * n
            result = rp.read(buf=buf, n=n)
            output = "ReadWithPointer:"
            output += " " * (17 - len(output))
            output += f"read chars = {result} "
            output += " " * (35 - len(output))
            buf = "".join(buf)
            output += f"buf = {buf} "
            test_ok = solution == (result, buf)
            output += " " * (55 - len(output))
            output += f'Test: {"OK" if test_ok else "NOT OK"}'
            print(output)

            print()

        print()
