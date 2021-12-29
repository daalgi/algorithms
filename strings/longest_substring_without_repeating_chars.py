"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without 
repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a 
subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""


def sliding_window(s: str) -> int:
    # Time complexity: O(2n) = O(n)
    # Space complexity: O(26) = O(1)

    # Keep track of the character repetitions
    count = dict()
    # Loop over the characters,
    # using two pointers `left` and `right`
    left, max_length = 0, 0
    n = len(s)
    for right in range(n):
        # Current character count
        count[s[right]] = count.get(s[right], 0) + 1

        if count[s[right]] == 1:
            # If there's no repetition of the current char,
            # update the length of the substring
            curr_length = right - left + 1
            if curr_length > max_length:
                max_length = curr_length
        else:
            # If there's a repetition of the current char,
            # find where it is moving the left pointer forward
            while s[left] != s[right]:
                # subtract 1 from the current counter
                count[s[left]] -= 1
                # move the pointer
                left += 1
            # After finding the repeated character, move the
            # `left` pointer one more character forward to
            # avoid any repetitions
            # subtract 1 from the current counter
            count[s[left]] -= 1
            # move the pointer
            left += 1

    return max_length


def sliding_window2(s: str) -> int:
    # Time complexity: O(2n) = O(n)
    # Space complexity: O(26) = O(1)

    # Keep track of the character repetitions
    count = dict()
    # Loop over the characters,
    # using two pointers `left` and `right`
    left, max_length = 0, 0
    n = len(s)
    for right in range(n):
        # Current character count
        count[s[right]] = count.get(s[right], 0) + 1

        while count[s[right]] > 1:
            count[s[left]] -= 1
            left += 1

        curr_length = right - left + 1
        if curr_length > max_length:
            max_length = curr_length

    return max_length


def sliding_window_opt(s: str) -> int:
    # Time complexity: O(n)
    # Space complexity: O(26) = O(1)
    # Strategy: instead of keeping track of the count of characters,
    # use a dictionary to map { char: index + 1 },
    # so when the current char is in the mapping, we can know exactly
    # where the left pointer should go to have a valid substring.

    # Keep track of the character repetitions
    chars = dict()
    # Loop over the characters,
    # using two pointers `left` and `right`
    left, max_length = 0, 0
    n = len(s)
    for right in range(n):

        if s[right] in chars:
            # If the current character is in the mapping,
            # move the left pointer
            left = max(left, chars[s[right]])

        # Update the current character last index
        chars[s[right]] = right + 1

        # Check if the current length is greater than the max
        curr_length = right - left + 1
        if curr_length > max_length:
            max_length = curr_length

    return max_length


if __name__ == "__main__":
    print("-" * 60)
    print("Longest substring without repeating characters")
    print("-" * 60)

    test_cases = [
        # (string, solution)
        ("", 0),
        ("ab", 2),
        ("aba", 2),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("tmmzuxt", 5),
        ("asdpofinqwefaosidfasdfadfasfgsdtyasdfiuhasdiuf", 11),
    ]

    for s, solution in test_cases:

        print(f"String: {s}")

        result = sliding_window(s)
        output = f"\t     sliding_window = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sliding_window2(s)
        output = f"\t    sliding_window2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sliding_window_opt(s)
        output = f"\t sliding_window_opt = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
