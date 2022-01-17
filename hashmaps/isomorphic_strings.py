"""
https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if 
they are isomorphic.

Two strings s and t are isomorphic if the 
characters in s can be replaced to get t.

All occurrences of a character must be replaced with 
another character while preserving the order of characters. 
No two characters may map to the same character, but a 
character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 10^4
t.length == s.length
s and t consist of any valid ascii character.
"""


def hashmap2(s: str, t: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Check if the number of words is equal
    # to the number of characters in the pattern
    if len(s) != len(t):
        return False

    # Check if the number of unique words is the
    # same as the number of unique characters in the pattern
    if len(set(s)) != len(set(t)):
        return False

    # Loop over the words and characters, adding not yet seen
    # words and characters to the hashmap `word_to_pattern`
    #   word_to_pattern = { "word1": "a", "word2": "b", ...}
    s_to_t = {}
    for i in range(len(s)):
        if s[i] not in s_to_t:
            s_to_t[s[i]] = t[i]
        elif s_to_t[s[i]] != t[i]:
            return False

    return True


def hashmap3(s: str, t: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)
    return list(map(s.index, s)) == list(map(t.index, t))


def hashmap4(s: str, t: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)
    return [s.index(c) for c in s] == [t.index(c) for c in t]


def hashmap5(s: str, t: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)
    return len(s) == len(t) and len(set(zip(s, t))) == len(set(s)) == len(set(t))


if __name__ == "__main__":
    print("-" * 60)
    print("Isomorphic strings")
    print("-" * 60)

    test_cases = [
        # ( pattern, s, solution )
        ("a", "b", True),
        ("ab", "ca", True),
        ("ab", "cc", False),
        ("aaa", "cdc", False),
        ("aba", "mam", True),
        ("aab", "xyz", False),
        ("bab", "mno", False),
        ("bab", "xyx", True),
    ]

    for s, t, solution in test_cases:

        print("String 1:", s)
        print("String 2:", t)

        result = hashmap2(s, t)
        output = f"    hashmap2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap3(s, t)
        output = f"    hashmap3 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap4(s, t)
        output = f"    hashmap4 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap5(s, t)
        output = f"    hashmap5 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
