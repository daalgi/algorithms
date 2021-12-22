"""
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters 
into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters 
include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing 
non-alphanumeric characters.
Since an empty string reads the same forward and backward, 
it is a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


def two_pointers(s: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Remove non-alphanumeric characters from the string
    # and make all characters lower case
    s = "".join(c for c in s if c.isalnum()).lower()

    # Use two pointers to check if the characters
    # are the same from the edges towards the center
    left, right = 0, len(s) - 1
    while left <= right and s[left] == s[right]:
        # If the pointer haven't crossed and the
        # characters at both pointers are the same,
        # move both pointers
        left += 1
        right -= 1

    # If the loop finished before the pointers crossed,
    # there was some not-matching character along the way,
    # so it's not a palindrome; if the pointers crossed,
    # it's a palindrome.
    return left >= right


if __name__ == "__main__":
    print("-" * 60)
    print("Valid palindrome")
    print("-" * 60)

    test_cases = [
        (" ", True),
        ("Abbcbba", True),
        ("1Abbba1", True),
        ("Abbbba", True),
        ("Abba", True),
        ("Aba", True),
        ("Aa", True),
        ("Aac", False),
        ("Abbbcbba", False),
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("asd fa98hs fanerf)(HUbh/uG*+", False),
        ("a" * 30 + "ad" + "a" * 30, False),
    ]

    for s, solution in test_cases:

        output = f"String: {s}"
        if len(output) > 60:
            output = output[:60] + "..."
        print(output)

        result = two_pointers(s)
        output = f"\t two_pointers = "
        output += " " * (15 - len(output))
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
