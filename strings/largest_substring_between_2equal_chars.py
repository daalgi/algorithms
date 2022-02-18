"""
https://leetcode.com/problems/largest-substring-between-two-equal-characters/

Given a string s, return the length of the longest 
substring between two equal characters, excluding 
the two characters. If there is no such substring 
return -1.

A substring is a contiguous sequence of characters 
within a string.

Example 1:
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty 
substring between the two 'a's.

Example 2:
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear 
twice in s.

Constraints:
1 <= s.length <= 300
s contains only lowercase English letters.
"""
from collections import defaultdict


def brute_force(s: str) -> int:
    # Time complexity: O(n²)
    # Space complexity: O(1)
    pass


def hashmap(s: str) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Use a hashmap { letter1: [index1, index2, ...], ... }
    indices = defaultdict(list)
    n = len(s)
    for i in range(n):
        indices[s[i]].append(i)

    # Find the largest difference between the indices of
    # each character
    longest = -1
    for c in indices:
        if len(indices[c]) > 1:
            # If the character appears more than once,
            # compare last and first indices
            curr_length = indices[c][-1] - indices[c][0] - 1
            if curr_length > longest:
                longest = curr_length

    return longest


def one_pass(s: str) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Hashmap { letter: first_index }
    indices = {}
    longest = -1
    # Loop over the string
    n = len(s)
    for i in range(n):
        if s[i] in indices:
            # If the current char `s[i]` is in the hashmap,
            # compute the current length
            curr_length = i - indices[s[i]] - 1
            if curr_length > longest:
                longest = curr_length
        else:
            # If the current char is not in the hashmap,
            # add its index
            indices[s[i]] = i

    return longest


def one_pass2(s: str) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    indices, longest, n = {}, -1, len(s)
    for i in range(n):
        longest = max(longest, i - indices.setdefault(s[i], i) - 1)

    return longest


if __name__ == "__main__":
    print("-" * 60)
    print("Longest substring between two equal characters")
    print("-" * 60)

    test_cases = [
        # (s, solution)
        ("a", -1),
        ("aa", 0),
        ("aaa", 1),
        ("abca", 2),
        ("asdfzxcbv", -1),
        ("asdfzxcbsvs", 8),
    ]

    for s, solution in test_cases:

        print("String", s)

        result = hashmap(s)
        output = f"      hashmap = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = one_pass(s)
        output = f"     one_pass = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = one_pass2(s)
        output = f"    one_pass2 = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
