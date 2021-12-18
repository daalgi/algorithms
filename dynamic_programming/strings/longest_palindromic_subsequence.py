"""
https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another 
sequence by deleting some or no elements without changing the 
order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Constraints:
1 <= s.length <= 1000
s consists only of lowercase English letters.
"""
from typing import List
from functools import lru_cache


def brute_force(s: str) -> int:
    # Time complexity: O(2^n)
    # Space complexity: O(n)

    def dfs(sub: List[str], i: int) -> int:
        # DFS - backtracking

        # Base case
        if i == n:
            return len(sub) if sub == sub[::-1] else 1

        # Add candidate
        sub.append(s[i])
        # Explore
        op1 = dfs(sub, i + 1)

        # Remove added candidate
        sub.pop()
        # Explore
        op2 = dfs(sub, i + 1)

        return max(op1, op2)

    n = len(s)
    return dfs([], 0)


def dp_memoization(s: str) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(n²)
    # Space complexity: O(n²)

    @lru_cache(maxsize=None)
    def dfs(start: int, end: int) -> int:

        # Base cases
        if start > end:
            # If the `start` pointer passes `end`,
            # not a valid subsequence
            return 0
        if start == end:
            # Same `start` and `end` indices means that
            # the subsequence is made of 1 character,
            # so the maximum length equals 1 (always a palindrome)
            return 1

        if s[start] == s[end]:
            # If the two characters are the same,
            # check the maximum palindromic subsequence in between,
            # and add the current two caracters, i.e.:
            #   ccaaabbaa
            #   012345678
            #      s    e
            #   string[s] == string[e], then,
            #   LPS[s+1][e-1] = 4 ("abba")
            #   LPS[s][e] = LPS[s+1][e-1] + 2 ("aabbaa")
            return dfs(start + 1, end - 1) + 2
        else:
            # If the two characters are NOT the same,
            # check the maximum palindromic subsequence
            # in between, i.e.:
            #   ccaaabbaa
            #   012345678
            #      s e
            #   string[s] != string[e], then,
            #   LPS[s+1][e] = 1 ("a", "b")
            #   LPS[s][e-1] = 2 ("aa")
            #   LPS[s][e] = max(1, 2) = 2 ("aa")
            return max(dfs(start + 1, end), dfs(start, end - 1))

    # Call the recursive function
    return dfs(0, len(s) - 1)


def dp_tabulation(s: str) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(n²)
    # Space complexity: O(n²)

    # Size of the string
    n = len(s)

    # State variables: `start` and `end` indices of the subsequence
    # Table mapping the indices of the characters in the string to
    # the maximum length of the palindromic subsequence:
    # row `i`: maximum length of palindromic subsequence starting at `i`
    # col `j`: maximum length of palindromic subsequence end at `j`
    dp = [[0] * n for _ in range(n)]

    # Initialize the diagonal with 1s:
    # a single letter is always a palindrome
    for i in range(n):
        dp[i][i] = 1

    # Loop over the elements of the table (top triangular),
    for end in range(1, n):
        # start at one element above the current diagonal cell,
        # and go upwards
        for start in range(end - 1, -1, -1):
            if s[start] == s[end]:
                # If the two characters are the same,
                # check the maximum palindromic subsequence in between,
                # and add the current two caracters, i.e.:
                #   ccaaabbaa
                #   012345678
                #      s    e
                #   string[s] == string[e], then,
                #   dp[s+1][e-1] = 4 ("abba")
                #   dp[s][e] = dp[s+1][e-1] + 2 ("aabbaa")
                dp[start][end] = dp[start + 1][end - 1] + 2

            else:
                # If the two characters are NOT the same,
                # check the maximum palindromic subsequence
                # in between, i.e.:
                #   ccaaabbaa
                #   012345678
                #      s e
                #   string[s] != string[e], then,
                #   dp[s+1][e] = 1 ("a", "b")
                #   dp[s][e-1] = 2 ("aa")
                #   dp[s][e] = max(1, 2) = 2 ("aa")
                dp[start][end] = max(dp[start][end - 1], dp[start + 1][end])

    # Return the value in the `dp` table where the
    # left pointer (start) at 0,
    # and the right pointer (end) at the last character
    return dp[0][-1]


if __name__ == "__main__":

    print("-" * 60)
    print("Longest palindromic subsequence")
    print("-" * 60)

    test_cases = [
        ("abcd", 1),
        ("cbbab", 3),
        ("babad", 3),
        ("bbbab", 4),
        ("cbbd", 2),
        ("aaaabbaa", 6),
        ("ccaaabbaa", 6),
        ("cbbtadatad", 5),
        ("asdfasdfasdfasdf", 7),
        ("aaaaaaaa", 8),
        ("aacabdkacaa", 9),
    ]

    for s, solution in test_cases:

        print("String:", s)

        result = brute_force(s)
        string = f"   brute_force = "
        string += " " * (20 - len(string))
        string += str(result)
        string += " " * (50 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        result = dp_memoization(s)
        string = f"dp_memoization = "
        string += " " * (20 - len(string))
        string += str(result)
        string += " " * (50 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        result = dp_tabulation(s)
        string = f" dp_tabulation = "
        string += " " * (20 - len(string))
        string += str(result)
        string += " " * (50 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        print()
