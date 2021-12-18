"""
https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""
from typing import List
from functools import lru_cache


def brute_force(s: str) -> int:
    # Time complexity: O(n^3)
    # Space complexity: O(n)
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            curr = s[i : j + 1]
            if curr == curr[::-1]:
                count += 1
    return count


def two_pointers(s: str) -> int:
    # Strategy: expand palindromes
    # Time complexity: O(n²)
    # Space complexity: O(1)

    def expand_palindromes(s: str, left: int, right: int) -> int:
        # Given the two pointers `left` and `right`,
        # count the palindromes further expanding to the left and right
        count = 0
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    # Start algorithm
    n = len(s)
    count = 0
    # Loop over the indices of the string
    for i in range(n):
        # Count the palindromes expanding from one single
        # character, resulting in palindromes of odd length
        count += expand_palindromes(s, i, i)
        # Count the palindromes expanding from two contiguous
        # characters, resulting in palindromes of even length
        count += expand_palindromes(s, i, i + 1)

    return count


def dp_memoization(s: str) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(n²)
    # Space complexity: O(n²)

    @lru_cache(maxsize=None)
    def dfs(start: int, end: int) -> int:
        # DFS recursive function with python's built-in memoization

        # Base case
        if start >= end:
            # When the pointers cross, there's
            # one palidrome made of one single character
            return 1

        if s[start] == s[end]:
            # If the current characters are equal,
            # check if the substrings between `start` and `end`
            # are palindromes
            return dfs(start + 1, end - 1)

        # If the current characters are not equal,
        # not a palindrome
        return 0

    # Start algorithm
    n = len(s)
    count = 0
    # Loop over the indices of the string to define
    # the start of the substrings to be checked
    for i in range(n):
        # Loop over the end of the substrings
        for j in range(i, n):
            # Recursive function that uses memoization
            # to check if the current substring is a palindrome
            count += dfs(i, j)

    return count


def dp_tabulation(s: str) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(n²)
    # Space complexity: O(n²)

    # Size of the string
    n = len(s)

    # State variables: `start` and `end` indices of the substrings.
    # Table mapping the indices of the characters in the string to
    # boolean values indicating whether the current substring is a palidrome.
    # row `i`: substring starting at `i`
    # col `j`: substring ending at `j`
    dp = [[False] * n for _ in range(n)]

    # Initialize the diagonal with True:
    # a single letter is always a palindrome
    for i in range(n):
        dp[i][i] = True

    # Use the defined table `dp` to keep track of whether already computed
    # substrings are palindromes or not
    count = 0
    # Loop over the elements of the table (top triangular),
    for end in range(n):
        # start at one element above the current diagonal cell,
        # and go upwards
        for start in range(end, -1, -1):
            if start == end:
                # The diagonal is always True:
                # a single letter is always a palindrome
                dp[start][end] = True
            elif start + 1 == end:
                # 2-character substring
                if s[start] == s[end]:
                    # If both characters are equal, is a palindrome
                    dp[start][end] = True
            else:
                # Substring of 3 or more characters
                if s[start] == s[end]:
                    # If the `start` and `end` characters are equal,
                    # check the inner substring to determine
                    # if it's a palindrome. Example:
                    #   cbaabc
                    #   012345
                    #    s  e
                    #   string[s] == string[e] ("b")
                    #   string[s+1:(e-1)+1] = "aa" --> palindrome
                    #   dp[s][e] = dp[s+1][e-1] = True
                    dp[start][end] = dp[start + 1][end - 1]

            # If the current substring is a palindrome,
            # add it to the count
            count += dp[start][end]

    return count


if __name__ == "__main__":

    print("-" * 60)
    print("Palindromic substrings")
    print("-" * 60)

    test_cases = [
        ("abc", 3),
        ("aaa", 6),
        ("abcd", 4),
        ("cbbab", 7),
        ("babad", 7),
        ("bbbab", 9),
        ("cbbd", 5),
        ("aaaabbaa", 18),
        ("cbbtadatad", 15),
        ("asdfasdfasdfasdf", 16),
        ("aaaaaaaa", 36),
        ("aacabdkacaa", 15),
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

        result = two_pointers(s)
        string = f"  two_pointers = "
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
