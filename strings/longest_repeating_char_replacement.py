"""
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character 
of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter 
you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
"""
from collections import Counter


def sliding_window(s: str, k: int) -> int:
    # Time complexity: O(26n) = O(n)
    # Space complexity: O(26) = O(1)

    n = len(s)
    if n <= k:
        return n

    count = dict()
    # Loop over the characters using two pointers to keep
    # track of both the current character (`right`), and the start
    # of the current substring (`left`)
    left, max_length = 0, 1 + k
    for right in range(n):
        # Current character `c`
        c = s[right]
        count[c] = count.get(c, 0) + 1
        # Current substring length
        curr_length = right - left + 1
        # For the current substring, the needed `k` to still
        # be a valid substring, O(26)
        needed_k = curr_length - max(count.values())

        if needed_k > k:
            # If it's not a valid substring,
            # move the `left` pointer (reduce the length).
            # Also, we have remove the character at `left` from the counter
            count[s[left]] -= 1
            left += 1
        else:
            # If it's still a valid substring,
            # update the maximum length if needed
            if curr_length > max_length:
                max_length = curr_length

    return max_length


def sliding_window_opt(s: str, k: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(26) = O(1)
    # Strategy: Instead of evaluating the max count at every
    # iteration (time complexity O(26)),
    # we keep track of the max count, updating it at every iteration.

    # `max_length` is the longest subsequence without
    # repeating chars and `k` changes.
    # `max_count` is the longest subsequence of the same char so far
    max_length = max_count = 0
    # Counter to keep track of the number of repeated chars in the current
    # subsequence
    # count = Counter()
    count = dict()
    # Loop over the characters of the string
    n = len(s)
    for i in range(n):
        # Add the current char to the count
        # count[s[i]] += 1
        count[s[i]] = count.get(s[i], 0) + 1
        # Find the new `max_count` only if the current char count exceeds it
        # max_count = max(max_count, count[s[i]])
        if count[s[i]] > max_count:
            max_count = count[s[i]]
        # If the current count `max_count` plus the allowed changes `k` is
        # larger than the previous `max_length`, update it
        if k + max_count > max_length:
            max_length += 1
        else:
            # If it's not larger, remove from the count the char of
            # the start of the subsequence at `i - max_length`
            # count[s[i - max_length]] -= 1
            left_char = s[i - max_length]
            count[left_char] = count.get(left_char, 0) - 1

    return max_length


if __name__ == "__main__":
    print("-" * 60)
    print("Longest repeating character replacement")
    print("-" * 60)

    test_cases = [
        # (string, k, solution)
        ("AB", 1, 2),
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AABCDA", 2, 4),
        ("AAAABAAABAAABBCAABA", 3, 13),
    ]

    for s, k, solution in test_cases:

        print(f"String: {s}\nk: {k}")

        result = sliding_window(s, k)
        output = f"\t     sliding_window = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += "\n" + " " * 55
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sliding_window_opt(s, k)
        output = f"\t sliding_window_opt = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += "\n" + " " * 55
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
