"""
https://leetcode.com/problems/longest-common-subsequence/

VARIATION: RESTORE THE SUBSEQUENCE

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


def dp_iter(s1: str, s2: str, verbose: bool = False) -> str:
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

    if verbose:
        for row in memo:
            print(row)
    # Trace back in the memo matrix where the increases
    # in the LCS come from
    i, j = m, n
    sub = []
    while i > 0 and j > 0 and memo[i][j] > 0:
        if (
            memo[i][j] > memo[i][j - 1] 
            and memo[i][j] > memo[i - 1][j]
        ):
            # Current LCS equal to the diagonal (top-left),
            # add the character and go to the diagonal
            i -= 1
            j -= 1
            sub.append(s1[i])
        elif memo[i - 1][j] >= memo[i][j - 1]:
            # Current value in memo coming from the left cell
            i -= 1
        else:
            # Current value in memo coming from the top cell
            j -= 1

    # Return the reversed string
    return "".join(sub[::-1])


if __name__ == "__main__":

    print("-" * 60)
    print("Longest common subsequence - RESTORE THE SUBSEQUENCE")
    print("-" * 60)

    test_cases = [
        ("abcde", "ace", "ace"),
        ("abcde", "hfg", ""),
        ("abc", "abc", "abc"),
        ("cba", "abc", "c"),
        ("abc", "abcdef", "abc"),
        ("aabbcc", "abc", "abc"),
        ("ace", "xabccde", "ace"),
        ("abcdaf", "acbcf", "abcf"),
    ]

    for s1, s2, solution in test_cases:

        result = dp_iter(s1, s2)
        string = f"dp_iter{s1, s2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
