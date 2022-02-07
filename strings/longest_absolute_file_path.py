"""
https://leetcode.com/problems/longest-absolute-file-path/

Suppose we have a file system that stores both files 
and directories. An example of one system is represented 
in the following picture:

Here, we have dir as the only directory in the root. 
dir contains two subdirectories, subdir1 and subdir2. 
subdir1 contains a file file1.ext and subdirectory subsubdir1. 
subdir2 contains a subdirectory subsubdir2, 
which contains a file file2.ext.

In text form, it looks like this 
(with ⟶ representing the tab character):
dir
⟶ subdir1
⟶ ⟶ file1.ext
⟶ ⟶ subsubdir1
⟶ subdir2
⟶ ⟶ subsubdir2
⟶ ⟶ ⟶ file2.ext

If we were to write this representation in code, it will look 
like this: 
"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext". 
Note that the '\n' and '\t' are the new-line and tab characters.

Every file and directory has a unique absolute path in 
the file system, which is the order of directories that 
must be opened to reach the file/directory itself, all 
concatenated by '/'s. Using the above example, the 
absolute path to file2.ext is "dir/subdir2/subsubdir2/file2.ext". 
Each directory name consists of letters, digits, and/or spaces. 
Each file name is of the form name.extension, where name and 
extension consist of letters, digits, and/or spaces.

Given a string input representing the file system in the 
explained format, return the length of the longest absolute 
path to a file in the abstracted file system. If there is no 
file in the system, return 0.

Example 1:
Input: input = 
"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
Output: 20
Explanation: We have only one file, and the absolute path is 
"dir/subdir2/file.ext" of length 20.

Example 2:
Input: input = 
"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
Output: 32
Explanation: We have two files:
"dir/subdir1/file1.ext" of length 21
"dir/subdir2/subsubdir2/file2.ext" of length 32.
We return 32 since it is the longest absolute path to a file.

Example 3:
Input: input = "a"
Output: 0
Explanation: We do not have any files, just a single 
directory named "a".

Constraints:
1 <= input.length <= 10^4
input may contain lowercase or uppercase English letters, 
a new line character '\n', a tab character '\t', 
a dot '.', a space ' ', and digits.
"""
from collections import deque


def with_stack(s: str) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    i, n = 0, len(s)

    # Root dir
    is_file = False
    while i < n and s[i] != "\n":
        if s[i] == ".":
            is_file = True
        i += 1

    # Keep track of the size of the dir names.
    # Use the prefix sum to avoid repeated computations
    if is_file:
        curr_path = deque()
        max_length = i
    else:
        curr_path = deque([i])
        max_length = 0

    # Loop over the rest of the subdirs

    while i < n:

        # Skip new line
        if s[i] == "\n":
            i += 1

        # Count the number of "\t" to
        # know the current level
        level = 0
        while s[i] == "\t":
            level += 1
            i += 1

        # Remove the previous deeper subdirs
        # that are no longer in the current path
        while level < len(curr_path):
            curr_path.pop()

        # Count chars until next "\"
        is_file = False
        start = i
        while i < n and s[i] != "\n":
            if s[i] == ".":
                is_file = True
            i += 1

        # Add the current subdir or file name size
        # to the prefix sum
        # (take into account the separator "/")
        if curr_path:
            curr_path.append(curr_path[-1] + 1 + i - start)
        else:
            # No root dir, only file
            curr_path.append(i - start)

        if is_file and curr_path[-1] > max_length:
            max_length = curr_path[-1]

    return max_length


def with_stack2(s: str) -> int:
    paths, stack, ans = s.split("\n"), [], 0
    for path in paths:
        p = path.split("\t")
        depth, name = len(p) - 1, p[-1]
        l = len(name)
        while stack and stack[-1][1] >= depth:
            stack.pop()
        if not stack:
            stack.append((l, depth))
        else:
            stack.append((l + stack[-1][0], depth))
        if "." in name:
            ans = max(ans, stack[-1][0] + stack[-1][1])
    return ans


def hashmap(s: str) -> int:
    # Hasmap to store the dirs at every level in a path
    levels = {}
    longest = 0
    # Split the string by lines and loop over them
    file_list = s.split("\n")
    for i in file_list:
        if "." not in i:
            # It's a folder
            # Level
            level = i.count("\t")
            # Length of the folder
            value = len(i.replace("\t", ""))
            levels[level] = value
        else:
            # It's a file
            level = i.count("\t")
            # Sum the lengths of the dirs at the different levels
            # and the file
            length = (
                sum([levels[j] for j in levels.keys() if j < level])
                + len(i.replace("\t", ""))
                + level
            )
            longest = max(longest, length)
    return longest


if __name__ == "__main__":
    print("-" * 60)
    print("Longest absolute file path")
    print("-" * 60)

    test_cases = [
        ("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext", 20),
        (
            "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",
            32,
        ),
        ("a", 0),
        ("file1.txt\nfile2.txt\nlongfile.txt", 12),
        ("file1.txt\nfolderfolder\n\tfile2.txt\nlongfile.txt", 22),
    ]

    for s, solution in test_cases:

        print(">> File system:")
        print(s)

        result = with_stack(s)
        output = f"-->   one_scan_stack = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = with_stack2(s)
        output = f"-->  one_scan_stack2 = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap(s)
        output = f"-->          hashmap = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
