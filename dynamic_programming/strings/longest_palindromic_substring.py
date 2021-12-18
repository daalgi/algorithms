"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.  
"""


def brute_force(s: str) -> str:
    # Time complexity: O(n³)
    # Space complexity: O(n)
    n = len(s)
    res = ""
    # Loop over the starting indices of the different substrings
    for i in range(n):
        # Loop over the ending indices of the different substrings
        for j in range(i + 1, n + 1):
            curr = s[i:j]
            # Check if the current substring is a palindrome
            if curr == curr[::-1]:
                if len(curr) > len(res):
                    res = curr

    return res


def two_pointers(s: str) -> str:
    # Time complexity: O(n²)
    # Space complexity: O(1)
    # Strategy: expand around the center for each character

    def palindromes_from_center(left: int, right: int) -> str:
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    n = len(s)
    res = ""
    # Loop over the indices of the characters in the string
    for i in range(n):
        # Longest palindromes expanding from `i` as a center
        odd = palindromes_from_center(i, i)
        even = palindromes_from_center(i, i + 1)

        res = max(res, odd, even, key=len)

    return res


def dp_tabulation(s: str) -> str:
    # Dynamic programming - Tabulation
    # Time complexity: O(n²)
    # Space complexity: O(n²)

    # Size of the string
    n = len(s)

    # State variables: `start` and `end` indices
    # Table mapping the indices of the characters in the string:
    # row `i`: substring starting at `i`
    # col `j`: substring ending at `j`
    dp = [[False] * n for _ in range(n)]

    # Initialize the diagonal with `True`: a single letter
    # is always a palindrome
    for i in range(n):
        dp[i][i] = True

    # Initialize the max length parameters to the first character,
    # taking into account that it'll return s[start:end+1]
    max_length, max_length_start, max_length_end = 1, 0, 0

    # Loop over the elements of the table (top triangular),
    for end in range(1, n):
        # start at one element above the current diagonal cell,
        # and go upwards
        for start in range(end - 1, -1, -1):
            if s[start] == s[end]:
                # If the two characters are the same,
                # check if the substring in between is a palindrome, i.e.:
                #   ccaaabbaa
                #   012345678
                #      s    e
                #   string[s] == string[e], then,
                #   is string[s+1:e-1] palindrome?
                #   Yes, so the current substring is a palindrome:
                #   dp[s][e] = True
                #   curr_length = 8 - 3 + 1 = 6
                #   if that's the max_length, return string[s:e+1]
                if end - start == 1 or dp[start + 1][end - 1]:
                    dp[start][end] = True
                    curr_length = end - start + 1
                    if curr_length > max_length:
                        max_length = curr_length
                        max_length_start, max_length_end = start, end

    return s[max_length_start : max_length_end + 1]


if __name__ == "__main__":

    print("-" * 60)
    print("Longest palindromic substring")
    print("-" * 60)

    test_cases = [
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("aaaabbaa", "aabbaa"),
        ("ccaaabbaa", "aabbaa"),
        ("cbbtadatad", "tadat"),
        ("asdfasdfasdfasdf", "a"),
        ("aaaaaaaaaaa", "aaaaaaaaaaa"),
        ("aacabdkacaa", "aca"),
    ]

    for s, solution in test_cases:

        print("String:", s)

        result = brute_force(s)
        string = f"  brute_force = "
        string += " " * (20 - len(string))
        string += str(result)
        string += " " * (50 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        result = two_pointers(s)
        string = f" two_pointers = "
        string += " " * (20 - len(string))
        string += str(result)
        string += " " * (50 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        result = dp_tabulation(s)
        string = f"dp_tabulation = "
        string += " " * (20 - len(string))
        string += str(result)
        string += " " * (50 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)
        print()
