"""
https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of 
their longest common subsequence. If there is no common 
subsequence, return 0.

A subsequence of a string is a new string generated from 
the original string with some characters (can be none) 
deleted without changing the relative order of the 
remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that 
is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its 
length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its 
length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, 
so the result is 0.

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""


def brute_force(s1: str, s2: str) -> int:
    # Time complexity: O(2^(m+n))
    # Worst case happens when there's no matching
    # characters between `s1` and `s2`.

    def rec(s1: str, s2: str, i: int, j: int) -> int:
        # Recursive function that compares char by char
        # from the end backwards.

        # Base case - if the indices go out of bounds
        if i < 0 or j < 0:
            return 0

        # If the current characters are the same,
        # add 1 and continue moving the pointers
        # of both strings
        if s1[i] == s2[j]:
            return 1 + rec(s1, s2, i - 1, j - 1)

        # If the characters are not the same, continue
        # recursevely considering both scenarios:
        # moving the pointer `s1` and `s2`
        return max(rec(s1, s2, i - 1, j), rec(s1, s2, i, j - 1))

    # Call the recursive function, starting with
    # the pointers at the last character of each string
    return rec(s1, s2, len(s1) - 1, len(s2) - 1)


def dp_iter(s1: str, s2: str) -> int:
    # Time complexity: O(mn)
    # Space complexity: O(mn)

    # Size of the strings
    m, n = len(s1), len(s2)
    # Matrix to store the longest common subsequence (LCS)
    # for each combination of characters.
    # The length of the matrix must be (m+1)x(n+1)
    # The first row and first column are filled with zeros.
    memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Loop over the characters of `s1`
    for i in range(m):
        # Loop over the characters of `s2`
        for j in range(n):
            # Check if the current characters are equal
            if s1[i] == s2[j]:
                # If equal characters,
                memo[i + 1][j + 1] = 1 + memo[i][j]
            else:
                memo[i + 1][j + 1] = max(
                    memo[i][j + 1], 
                    memo[i + 1][j]
                )

    return memo[m][n]


def dp_iter_opt(s1: str, s2: str) -> int:
    # Time complexity: O(mn)
    # Space complexity: O(min(m, n))
    # Memory optimization by storing only the last row
    # instead of all the rows in the `memo` matrix

    # Size of the strings
    m, n = len(s1), len(s2)
    # Force s2 to be the shortest string
    if m < n:
        s1, s2, m, n = s2, s1, n, m

    # Last row
    memo = [0] * (n + 1)

    prev, curr = 0, 0

    for i in range(m):
        prev = 0
        for j in range(n):
            curr = memo[j + 1]
            memo[j + 1] = max(
                memo[j + 1], 
                memo[j], 
                prev + 1 if s1[i] == s2[j] else 0
            )
            prev = curr

    return memo[n]


if __name__ == "__main__":

    print("-" * 60)
    print("Longest common subsequence")
    print("-" * 60)

    test_cases = [
        ("abcde", "ace", 3),
        ("abcde", "hfg", 0),
        ("abc", "abc", 3),
        ("cba", "abc", 1),
        ("abc", "abcdef", 3),
        ("aabbcc", "abc", 3),
        ("ace", "xabccde", 3),
        ("abcdaf", "acbcf", 4),
    ]

    for s1, s2, solution in test_cases:

        result = brute_force(s1, s2)
        string = f"brute_force{s1, s2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = dp_iter(s1, s2)
        string = f"    dp_iter{s1, s2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = dp_iter_opt(s1, s2)
        string = f"dp_iter_opt{s1, s2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
