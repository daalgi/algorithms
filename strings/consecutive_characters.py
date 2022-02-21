"""
https://leetcode.com/problems/consecutive-characters/

The power of the string is the maximum length of a 
non-empty substring that contains only one unique 
character.

Given a string s, return the power of s.

Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 
with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 
with the character 'e' only.

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters.
"""
from itertools import groupby


def one_pass(s: str) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    curr_len, max_len, n = 1, 1, len(s)
    for i in range(1, n):
        if s[i] == s[i - 1]:
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
        elif curr_len > 1:
            curr_len = 1

    return max_len


def one_liner(s: str) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    return max(len(list(c)) for _, c in groupby(s))


if __name__ == "__main__":
    print("-" * 60)
    print("Consecutive characters")
    print("-" * 60)

    test_cases = [
        # (s, solution)
        ("google", 2),
        ("aabbbccdddddeeff", 5),
        ("castellon", 2),
        ("valencia", 1),
    ]

    for s, solution in test_cases:

        print("String:", s)

        result = one_pass(s)
        output = f"       one_pass = "
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = one_liner(s)
        output = f"      one_liner = "
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
