"""
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

Given two strings s1 and s2, return the lowest ASCII sum of deleted 
characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value 
of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the 
minimum sum possible to achieve this.

Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer 
is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", 
we would get answers of 433 or 417, which are higher.

Constraints:
1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.
"""
from functools import lru_cache


def brute_force(s1: str, s2: str) -> int:
    # Time complexity: O(2^(m+n))
    # Worst case happens when there's no matching
    # characters between `s1` and `s2`.

    def dfs(i: int, j: int) -> int:
        # Recursive function that compares char by char
        # from the beginning forwards.

        # Base cases
        if i == m and j == n:
            # If both strings have no characters left,
            # there's nothing to delete
            return 0
        if i == m:
            # If `s1` has no characters left to check
            # all the remaining characters in `s2`
            # will have to be removed
            return sum([ord(x) for x in s2[j:]])
        if j == n:
            # If `s2` has no characters left to check,
            # all the remaining characters in `s1`
            # will have to be removed
            return sum([ord(x) for x in s1[i:]])

        # If the current characters are the same,
        # continue moving the pointers of both strings
        # (no need to delete any character)
        if s1[i] == s2[j]:
            return dfs(i + 1, j + 1)

        # If the characters are not the same, continue
        # recursevely considering both scenarios:
        return min(
            # removing the current character at `s1`
            ord(s1[i]) + dfs(i + 1, j),
            # removing the current character at `s2`
            ord(s2[j]) + dfs(i, j + 1),
        )

    # Call the recursive function, starting with
    # the pointers at the last character of each string
    m, n = len(s1), len(s2)
    return dfs(0, 0)


def dp_memoization(s1: str, s2: str) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(mn)
    # Same strategy as `brute_force`, but adding memoization
    # to avoid repeated computations with the
    # python's built-in function `lru_cache`

    @lru_cache(maxsize=None)
    def dfs(i: int, j: int) -> int:
        # Base cases
        if i == m and j == n:
            return 0
        if i == m:
            return sum([ord(x) for x in s2[j:]])
        if j == n:
            return sum([ord(x) for x in s1[i:]])

        if s1[i] == s2[j]:
            return dfs(i + 1, j + 1)
        return min(
            # Option 1: remove current char from `s1`
            ord(s1[i]) + dfs(i + 1, j),
            # Option 2: remove current char from `s2`
            ord(s2[j]) + dfs(i, j + 1),
        )

    # Size of the strings
    m, n = len(s1), len(s2)
    return dfs(0, 0)


def dp_tabulation(s1: str, s2: str) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(mn)
    # Space complexity: O(mn)

    # Size of the strings
    m, n = len(s1), len(s2)

    # Matrix to store the ASCII sum of deleted chars.
    # The length of the matrix is (m+1)x(n+1)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the first column and row with the base cases:
    # Fill the first row with the ASCII sum of deleted
    # chars assuming `s1` equals to the empty string ""
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

    # Fill the first column with the ASCII sum of deleted
    # chars assuming `s2` equals to the empty string ""
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

    # Loop over the characters of `s1`
    for i in range(1, m + 1):
        # Loop over the characters of `s2`
        for j in range(1, n + 1):
            # Check if the current characters are equal
            if s1[i - 1] == s2[j - 1]:
                # If equal characters, there's no char to be deleted,
                # so the cumulated sum will equal the sum before
                # checking the current pair of characters
                # (i - 1, j - 1), i.e.:
                #   zabycx      (i)
                #   abcdefghi   (j)
                #   012345678
                #   dp[i][j] = dp[4][2] = dp[3][1]
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # If NOT equal characters, get the minimum sum of these two:
                # 1) remove current character in `s1`
                # 2) remove current character in `s2`
                # i.e.:
                #   zabycx      (i)
                #   abcdefghi   (j)
                #   012345678
                #   dp[i][j] = dp[2][7] = min(
                #       ord("b") + dp[1][7], # s1
                #       ord("h") + dp[2][6]  # s2
                #   )
                dp[i][j] = min(
                    # Option 1: remove the current char at `s1`
                    ord(s1[i - 1]) + dp[i - 1][j],
                    # Option 2: remove the current char at `s2`
                    ord(s2[j - 1]) + dp[i][j - 1],
                )

    return dp[-1][-1]


if __name__ == "__main__":

    print("-" * 60)
    print("Minimum ASCII delete sum for two strings")
    print("-" * 60)

    test_cases = [
        ("sea", "eat", 231),
        ("delete", "leet", 403),
        ("abc", "abc", 0),
        ("cba", "abc", 390),
        ("abc", "abcdef", sum([ord(x) for x in "def"])),
        ("aabbcc", "abc", sum([ord(x) for x in "abc"])),
        ("ace", "xabccde", sum([ord(x) for x in "xbcd"])),
        ("abcdaf", "acbcf", sum([ord(x) for x in "cda"])),
        ("asdpoinasdgasisga", "fgerinzvxidfasef", 2460),
        ("asdpoinfewwwwwisga", "fgwwrinzvwidfasef", 2463),
    ]

    for s1, s2, solution in test_cases:

        print(f"Strings: {s1}, {s2}")

        if len(s1) < 10 and len(s2) < 10:
            result = brute_force(s1, s2)
            string = "   brute_force = "
            string += " " * (25 - len(string))
            string += str(result)
            string += " " * (60 - len(string))
            test_ok = solution == result
            string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
            print(string)

        result = dp_memoization(s1, s2)
        string = f"dp_memoization = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        result = dp_tabulation(s1, s2)
        string = f" dp_tabulation = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        print()
