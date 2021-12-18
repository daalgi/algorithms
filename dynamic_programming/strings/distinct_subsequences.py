"""
https://leetcode.com/problems/distinct-subsequences/

Given two strings s and t, return the number of distinct 
subsequences of s which equals t.

A string's subsequence is a new string formed from the original 
string by deleting some (can be none) of the characters without 
disturbing the remaining characters' relative positions. 
(i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 
32-bit signed integer.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag

Constraints:
1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""


def dp_memoization(s: str, t: str) -> int:
    # Time complexity: O(mn)
    # Space complexity: O(mn)
    # TODO
    pass


def dp_tabulation(s: str, t: str) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(mn)
    # Space complexity: O(mn)

    # Size of the string
    m, n = len(s), len(t)

    # Table mapping the indices of the characters in both strings and
    # the number of distinct subsequences:
    # row `i`: character `i` of `t`
    # col `j`: character `j` of `s`
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # Initialize the first row (row = 0), which represents
    # the empty subsequence "" of `t`, to 1s:
    # the empty string is always subsequence of `s`, but only one distinct
    for i in range(m + 1):
        dp[0][i] = 1

    # Loop over the characters of `t`
    for i in range(1, n + 1):
        # Loop over the characters of `s`
        for j in range(1, m + 1):
            if t[i - 1] == s[j - 1]:
                # If the two characters are the same,
                # check if the number of distinct previous subsequences
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

            else:
                # If the two characters are not the same,
                # the number of distinct subsequences doesn't change
                # from the previous `j` (comparison with s[j-1]
                dp[i][j] = dp[i][j - 1]

    return dp[-1][-1]


if __name__ == "__main__":

    print("-" * 60)
    print("Distinct subsequences")
    print("-" * 60)

    test_cases = [
        ("babad", "c", 0),
        ("babad", "", 1),
        ("", "a", 0),
        ("babad", "bab", 1),
        ("cbbd", "bb", 1),
        ("aaaabbaa", "ab", 8),
        ("rabbbit", "rabbit", 3),
        ("babgbag", "bag", 5),
        ("aaaaaaaa", "a", 8),
        ("aaaaaaaa", "aa", 28),
    ]

    for s, t, solution in test_cases:

        print("String s:", s)
        print("String t:", t)

        result = dp_tabulation(s, t)
        string = f"dp_tabulation = "
        string += " " * (20 - len(string))
        string += str(result)
        string += " " * (50 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        print()
