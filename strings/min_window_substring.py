"""
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every 
character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" 
includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.
 
Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


def sliding_window(s: str, t: str) -> str:
    # Time complexity: O(m*n)
    # Space complexity: O(n)

    m, n = len(s), len(t)

    # Edge case
    if m < n or n == 0:
        return ""

    # Count the characters in `t`
    count = dict()
    for c in t:
        count[c] = count.get(c, 0) + 1

    # Use `left` and `right` pointers
    left, right = 0, 0
    min_length, substring = float("inf"), ""

    # Loop over the characters of the string `s`
    while right < m:

        if s[right] in count:
            # If the character at `right` is in `t`,
            # decrease the count
            count[s[right]] -= 1

        # Current window length
        current_length = right - left + 1
        # If the current window is at least the size of the substring `t`
        # and all characters in `t` appear in the window,
        # move the `left` pointer forward to try to reduce the window length
        while current_length >= n and all(v <= 0 for v in count.values()):

            # Check if the current length is less than the actual min
            if current_length < min_length:
                min_length = current_length
                substring = s[left : right + 1]

            # If the character at `left` is in `t`,
            # increase the count before moving it forward
            if s[left] in count:
                count[s[left]] += 1
            # Move the `left` pointer and update the `current_length`
            left += 1
            current_length -= 1

        # Move the `right` pointer forward
        right += 1

    return substring


def sliding_window_opt(s: str, t: str) -> str:
    # Time complexity: O(m+n), worst case O(2m)
    # Space complexity: O(2n) = O(n)

    m, n = len(s), len(t)
    # Edge case
    if m < n or n == 0:
        return ""

    # Counter of the characters in `t`
    count_t = dict()
    for c in t:
        count_t[c] = count_t.get(c, 0) + 1

    # Counter of the characters in the current window
    # that are also in `t`
    count_window = dict()

    # Variables to keep track of the chars that are
    # both in the current window and in `t`
    window_chars, required_chars = 0, n

    # Two pointers to keep track of the window
    left, right = 0, 0

    # Min length of the window
    min_length, substring = float("inf"), ""

    # Loop over the chars of `s`
    while right < m:

        # Current character
        c = s[right]

        # Check if the current character is in `t`
        if c in count_t:
            # Update the char count in the current window
            count_window[c] = count_window.get(c, 0) + 1

            if count_window[c] == count_t[c]:
                # When the count in the window reaches
                # the count in `t`, update `window_chars`
                window_chars += 1

        curr_length = right - left + 1
        # If it's possible to reduce the current window,
        # move the `left` pointer forward as much as possible
        while curr_length >= n and window_chars == required_chars:

            if curr_length < min_length:
                # If the current length is shorter than the min, update it
                min_length = curr_length
                substring = s[left : right + 1]

            if s[left] in count_t:
                # If the char at `left` is in `t`, update the window counter
                count_window[s[left]] -= 1

                if count_window[s[left]] < count_t[s[left]]:
                    # If the number of repetitions of the char at `left`
                    # is less than in `t`, update `window_chars`
                    window_chars -= 1

            # Move the `left` pointer and update the current length
            left += 1
            curr_length -= 1

        # Update the `right` pointer for next iter
        right += 1

    return substring


if __name__ == "__main__":
    print("-" * 60)
    print("Minimum window substring")
    print("-" * 60)

    test_cases = [
        # (string_s, string_t, solution)
        ("a", "", ""),
        ("a", "a", "a"),
        ("aa", "a", "a"),
        ("a", "aa", ""),
        ("aaaaabbbbmmca", "abc", "bmmca"),
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("sdofiasndfoaisndfqlkwenfzoixdnasd", "aeiou", ""),
    ]

    for s, t, solution in test_cases:

        print(f"String s: {s}\nString t: {t}")

        result = sliding_window(s, t)
        output = f"\t     sliding_window = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sliding_window_opt(s, t)
        output = f"\t sliding_window_opt = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
