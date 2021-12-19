"""
https://leetcode.com/problems/shortest-common-supersequence/

Given two strings str1 and str2, return the shortest string that 
has both str1 and str2 as subsequences. If there are multiple 
valid strings, return any of them.

A string s is a subsequence of string t if deleting some number 
of characters from t (possibly 0) results in the string s.

Example 1:
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because 
we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because 
we can delete the last "ac".
The answer provided is the shortest such string 
that satisfies these properties.

Example 2:
Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.


Strategy:
We can form a supersequence by simply combining both strings:
    s1 + s1 = "abac" + "cab" = "abaccab"
We can reduce the length of the supersequence by finding common
characters:
    supersequence("abac", "cab") = "aba" + "c" + "ab" = "abacab"
We can find the shortest common supersequence (SCS) 
by means of the LCS (longest common subsequence) of both strings:
    LCS("abac", "cab") = "ab"
    SCS("abac", "cab") = "c" + "ab" + "ac" = "cabac"
    len(SCS) = len(s1) + len(s2) - LCS
    * even though "c" is common in both strings, their order can't
    be maintained (in s1 "c" is in the last position; in s2 is in the first)
    * to find the SCS we have to maximize the number of common characters
    in both strings (LCS)
"""
from functools import lru_cache


def brute_force(s1: str, s2: str) -> int:
    # Time complexity: O(2^(m+n))
    # Worst case happens when there's no matching
    # characters between `s1` and `s2`.

    def dfs(comb: str, i: int, j: int) -> str:
        # Base cases
        if i == m and j == n:
            return comb
        if i == m:
            return comb + "".join(s2[j:])
        if j == n:
            return comb + "".join(s1[i:])

        if s1[i] == s2[j]:
            return dfs(comb + s1[i], i + 1, j + 1)

        return min(
            # Option 1: add the current `s1` char
            dfs(comb + s1[i], i + 1, j),
            # Option 2: add the current `s1` char
            dfs(comb + s2[j], i, j + 1),
            # Return the minimum string with their length as comparator
            key=len,
        )

    m, n = len(s1), len(s2)
    return dfs("", 0, 0)


def dp_memoization(s1: str, s2: str) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(mn*mn)
    # Same strategy as `brute_force`, but adding memoization
    # to avoid repeated computations with the
    # python's built-in function `lru_cache`.
    # Still NOT EFFICIENT!!

    @lru_cache(maxsize=None)
    def dfs(comb: str, i: int, j: int) -> str:
        # Base cases
        if i == m and j == n:
            return comb
        if i == m:
            return comb + "".join(s2[j:])
        if j == n:
            return comb + "".join(s1[i:])

        if s1[i] == s2[j]:
            return dfs(comb + s1[i], i + 1, j + 1)

        return min(
            # Option 1: add the current `s1` char
            dfs(comb + s1[i], i + 1, j),
            # Option 2: add the current `s1` char
            dfs(comb + s2[j], i, j + 1),
            # Return the minimum string with their length as comparator
            key=len,
        )

    m, n = len(s1), len(s2)
    return dfs("", 0, 0)


def longest_common_subsequence(s1: str, s2: str) -> str:
    # Dynamic programming - Tabulation
    # Auxiliary function to solve the "subproblem" of LCS
    # used in `scs_optimal`
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the DP table to find the length of the LCS
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # print('>>>Length', dp[-1][-1])
    # Build the LCS string
    lcs = []
    i, j = m - 1, n - 1
    while i >= 0 and j >= 0:
        if s1[i] == s2[j]:
            # Append the common char to the `lcs`,
            lcs.append(s2[j])
            # Update the pointers of both strings
            # (go diagonally in the `dp` table)
            i -= 1
            j -= 1
        else:
            # If char not in LCS, find the largest
            # value in the `dp` table and follow that path
            if dp[i + 1][j] > dp[i][j + 1]:
                # Go to the left in the `dp` table
                j -= 1
            else:
                # Go up in the `dp` table
                i -= 1

    # print('>>>LCS', "".join(lcs[::-1]))
    return "".join(lcs[::-1])


def scs_optimal(s1: str, s2: str) -> str:
    # Two subproblems:
    # - Compute the LCS (longest common subsequence) with DP
    #   Time complexity: O(mn)
    #   Space complexity: O(mn)
    # - Add the characters in a correct order (there can be multiple solutions)
    #   Time complexity: O(m+n)
    #   Space complexity: O(m+n)

    # Size of the strings
    m, n = len(s1), len(s2)

    # Compute the longest common subsequence
    string_lcs = longest_common_subsequence(s1, s2)

    # Use 3 pointers to identify the order of the characters
    # of the SCS, i.e.:
    # s1  = abac
    # s2  = cab
    # lcs = ab
    # scs = cabac
    i, j, scs = 0, 0, []
    # Loop over the chars of the LCS
    for c in string_lcs:

        # Add all the non-LCS chars from `s1`
        while i < m and s1[i] != c:
            scs.append(s1[i])
            i += 1

        # Add all the non-LCS chars from `s2`
        while j < n and s2[j] != c:
            scs.append(s2[j])
            j += 1

        # Add the LCS char
        scs.append(c)

        # Update both pointers for next iteration
        i += 1
        j += 1

    while i < m:
        scs.append(s1[i])
        i += 1

    while j < n:
        scs.append(s2[j])
        j += 1

    return "".join(scs)


if __name__ == "__main__":

    print("-" * 60)
    print("Shortest common supersequence")
    print("-" * 60)

    test_cases = [
        # Multiple valid solutions!
        # Differnt algorithms can return different valid solutions
        ("abac", "cab", "cabac"),
        ("aaaaaaaa", "a", "aaaaaaaa"),
        ("asdfewfsdf", "ewfdsfasd", "asdfewfdsfasdf"),
        (
            "bcaaacbbbcbdddcdcccdadadcbabaccbccdcdcbcaccacbbdcbabb",
            "dddbbdcbccaccbabababadcacddbacadabdabcdbaaabaccbdaa",
            "dddbcaaacbbbdcbdddcdcaccdbadbadcbabadcacbccdcdcbacaccdacbdabcdcbaaabaccbdaa",
        ),
        (
            "bcaaacbbbcbdcaddadcacbdddcdcccdadadcbabaccbccdcdcbcaccacbbdcbabb",
            "dddbbdcbccaccbababaacbcbacdddcdabadcacddbacadabdabcdbaaabaccbdaa",
            "dddbbdcbccaaaccbababaacbdcbacddadcdacbadddcacdcccdbadcadcbabdaccbccdcdcbcaaabaccacbbdcbabba",
        ),
    ]

    MAX_STRING_LENGTH = 20

    for s1, s2, solution in test_cases:

        if len(s1) > MAX_STRING_LENGTH or len(s2) > MAX_STRING_LENGTH:
            print(f"Strings:\n{s1}\n{s2}")
        else:
            print(f"Strings: {s1}, {s2}")

        if len(s1) < MAX_STRING_LENGTH and len(s2) < MAX_STRING_LENGTH:
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

        result = scs_optimal(s1, s2)
        string = f"   scs_optimal = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        print()
