"""
https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

You are given a string s.

A split is called good if you can split s into 
two non-empty strings sleft and sright where their 
concatenation is equal to s (i.e., sleft + sright = s) 
and the number of distinct letters in sleft and 
sright is the same.

Return the number of good splits you can make in s.

Example 1:
Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
("a", "acaba") Left string and right string contains 
    1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 
    1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 
    2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 
    2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 
    3 and 1 different letters respectively.

Example 2:
Input: s = "abcd"
Output: 1
Explanation: Split the string as follows ("ab", "cd").

Constraints:
1 <= s.length <= 10^5
s consists of only lowercase English letters.
"""


def counting(s: str) -> int:
    # Time complexity: O(26n)
    # Space complexity: O(26) = O(1)

    # Count the number of letters in the `right` substring
    right = {}
    for c in s:
        right[c] = right.get(c, 0) + 1

    # Loop over the characters keeping track of the
    # letters added so far in `curr_counter` and compare
    # it with `counter`
    good_splits = 0
    left = {}
    n = len(s)
    for i in range(n - 1):
        # Update current counter
        left[s[i]] = left.get(s[i], 0) + 1
        # Update the total counter
        right[s[i]] -= 1
        # Check if currently both rights have the same
        # amount of different letters
        left_sum = sum(True for _ in left)
        right_sum = sum(True for c in right if right[c] != 0)
        if left_sum == right_sum:
            good_splits += 1

    return good_splits


def counting2(s: str) -> int:
    # Time complexity: O(26 + n) = O(n)
    # Space complexity: O(26) = O(1)

    right = {}
    for c in s:
        right[c] = right.get(c, 0) + 1

    # Loop over the characters keeping track of the
    # letters added so far in `curr_counter` and compare
    # it with `counter`
    good_splits = 0
    left = {}
    n = len(s)
    for i in range(n - 1):
        # Update current counter
        left[s[i]] = left.get(s[i], 0) + 1
        # Update the total counter
        right[s[i]] -= 1
        if right[s[i]] == 0:
            # If the current character in the `right` right is
            # null, remove it from the hashtable
            del right[s[i]]

        # Check if currently both counters have the same
        # amount of different letters.
        # Since we have removed any 0 cont in `right`,
        # we can just compare the lengths of both counters
        # (much more EFFICIENT!)
        if len(left) == len(right):
            good_splits += 1

    return good_splits


if __name__ == "__main__":
    print("-" * 60)
    print("Number of good ways to split a string")
    print("-" * 60)

    test_cases = [
        ("a", 0),
        ("ab", 1),
        ("abcd", 1),
        ("aacaba", 2),
        ("aaaaab", 1),
        ("aaaaaaaabbbaaaaabbbaaaaacccbbbbbbbbbbb", 1),
        ("aaaaaaaabbbaaaaabbbaaaaabbbbbbbbbbb", 15),
        ("aacabasfdifnasdifasdfaksdfksdfkkkdkdkdkdiosfksdfkskdkdkdisdf", 0),
    ]

    for s, solution in test_cases:

        print("String:", s)

        result = counting(s)
        output = f"      counting = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = counting2(s)
        output = f"     counting2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
