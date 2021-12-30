"""
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, 
and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? 
How would you adapt your solution to such a case?
"""


def count_char_freq(s: str, t: str) -> bool:
    # Time complexity: O(m+n)
    # Space complexity: O(max(m, n))

    count = dict()
    for c in s:
        count[c] = count.get(c, 0) + 1

    for c in t:
        count[c] = count.get(c, 0) - 1

    return all(v == 0 for v in count.values())


if __name__ == "__main__":
    print("-" * 60)
    print("Valid anagram")
    print("-" * 60)

    test_cases = [
        # (string_s, string_t, solution)
        ("a", "t", False),
        ("ab", "ba", True),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ]

    for s, t, solution in test_cases:

        print(f"String s: {s}\nString t: {t}")

        result = count_char_freq(s, t)
        output = f"\t count_char_freq = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
