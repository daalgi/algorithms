"""
https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the 
encoded_string inside the square brackets is being 
repeated exactly k times. Note that k is guaranteed 
to be a positive integer.

You may assume that the input string is always valid; 
there are no extra white spaces, square brackets are 
well-formed, etc.

Furthermore, you may assume that the original data 
does not contain any digits and that digits are only 
for those repeat numbers, k. For example, there will 
not be input like 3a or 2[4].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, 
and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""
from typing import List
from collections import deque


def one_stack(s: str) -> str:
    # Time complexity: O(max_k^count_k * n)
    # Space complexity: O(sum(max_k ^ count_k * n)),
    # where max_k is the max value of `k`,
    # count_k is the count of nested `k`,
    # and `n` is the maximum length of encoded string
    # Example:
    #   10[ab10[cd]]10[ef]
    #   max_k = 10, count_k = 2, n = 2
    #   Time complexity: 10 * cd * 10 * ab + 10 * 2 = 10² * 2
    """
    Example:
    012345678910
    a2[bc3[g]o]
    i=0, stack = [a]
    i=1, stack = [a, 2]
    i=2, stack = [a, 2, "["]
    i=3, stack = [a, 2, "[", b]
    i=4, stack = [a, 2, "[", b, c]
    i=5, stack = [a, 2, "[", b, c, 3]
    i=6, stack = [a, 2, "[", b, c, 3, "["]
    i=7, stack = [a, 2, "[", b, c, 3, "[", g]
    i=8, decoded = [g, g, g]
         stack = [a, 2, "[", b, c, g, g, g]
    i=9, stack = [a, 2, "[", b, c, g, g, g, o]
    i=10,decoded = [bcgggo, bcgggo]
         stack = [a, bcgggo, bcgggo]
    """

    stack = deque()

    # Loop over the characters of the string
    for c in s:

        if c != "]":
            stack.append(c)

        else:
            # Store the letters from last open brackets
            decoded = []
            while stack and stack[-1] != "[":
                decoded.append(stack.pop())

            # Remove "[" from the stack
            stack.pop()

            # Get the number of repetitions
            num, base = 0, 1
            while stack and stack[-1].isnumeric():
                num += (ord(stack.pop()) - ord("0")) * base
                base *= 10

            # Push back to the `stack` the decoded string
            while num:
                for i in range(len(decoded) - 1, -1, -1):
                    stack.append(decoded[i])
                num -= 1

    return "".join(stack)


def one_stack2(s: str) -> str:
    # Time complexity: O(max_k^count_k * n)
    # Space complexity: O(sum(max_k ^ count_k * n)),

    # Small optimizations that run much faster on Leetcode
    # in comparison with the previous solution `one_stack`:
    # - integer conversion faster than ord('8')-ord('0')
    # - string.isdigit() faster than string.isnumeric()
    stack = deque()

    for c in s:
        if c != "]":
            stack.append(c)

        else:
            # Store the letters from last open brackets
            decoded = []
            while stack and stack[-1] != "[":
                decoded.append(stack.pop())

            # Remove "[" from the stack
            stack.pop()

            # Get the number of repetitions
            num, base = 0, 1
            while stack and stack[-1].isdigit():
                num += int(stack.pop()) * base
                base *= 10

            # Push back to the `stack` the decoded string
            while num:
                for i in range(len(decoded) - 1, -1, -1):
                    stack.append(decoded[i])
                num -= 1

    return "".join(stack)


def one_stack3(s: str) -> str:
    # Time complexity: O()
    # Space complexity: O()

    # Slow solution

    num, stack = 0, deque([""])
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == "[":
            stack.append(num)
            num = 0
            stack.append("")
        elif c == "]":
            curr = stack.pop()
            repetitions = stack.pop()
            prev = stack.pop()
            # Note: expensive string concatenation
            stack.append(prev + curr * repetitions)
        else:
            # Note: expensive string concatenation
            stack[-1] += c

    return stack[0]


def two_stacks(s: str) -> str:
    # Time complexity: O(max_k n)
    # where `max_k` is the max value of `k`
    # `n` is the length of the string `s`

    # Space complexity: O(m + n)
    # where `m` is the number of letters
    # `n` is the number of digits

    """
    0123456789
    a2[b3[c]d]
    i=0, curr_string = [a]
    i=1, num=2
    i=2, count_stack = [2]
         string_stack = [a]
         curr_string = []
    i=3, curr_string = [b]
    i=4, num=3
    i=5, count_stack = [2, 3]
         string_stack = [a, b]
         curr_string = []
    i=6, curr_string = [c]
    i=7, repetitions = 3, count_stack = [2]
         curr_string = [b, c, c, c], string_stack = [a]
    i=8, curr_string = [b, c, c, c, d]
    i=9, repetitions = 2, count_stack = []
         curr_string = [a, b, c, c, c, d, b, c, c, c, d]
         string_stack = []
    """
    count_stack, string_stack = deque(), deque()
    curr_string = []
    num = 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)

        elif c == "[":
            # Push the number to the count stack
            count_stack.append(num)
            num = 0
            # Push the current string into the string stack
            string_stack.append("".join(curr_string))
            curr_string = []

        elif c == "]":
            repetitions = count_stack.pop()
            curr_string = [string_stack.pop()] + repetitions * curr_string

        else:
            curr_string.append(c)

        # print('\n--->', c)
        # print('count_stack', count_stack)
        # print('string_stack', string_stack)
        # print('curr_string', curr_string)
    return "".join(curr_string)


def recursion(s: str) -> str:
    # Time complexity: O(max_k n)
    # Space complexity: O(n)

    def decode_str(index: int) -> tuple:
        result = []
        # Loop over the chars until the end of the string
        # or until the next closing bracket "]", where the
        # current recursion would finish
        while index < n and s[index] != "]":

            if s[index].isdigit():
                # Form the number
                num = int(s[index])
                index += 1
                while index < n and s[index].isdigit():
                    num = num * 10 + int(s[index])
                    index += 1

                # Skip opening bracket "["
                index += 1

                # Recursive call to decode the string
                # up the the next `]` (or the end of the string)
                index, decoded_str = decode_str(index)

                # Skip the closing bracket "]"
                index += 1

                # Concatenate the current `result`
                # with the current nested decoded string
                result.extend(num * decoded_str)

            else:
                # If it's a char, add it to the current `result`
                result.append(s[index])
                index += 1

        return index, result

    n = len(s)
    return "".join(decode_str(0)[1])


if __name__ == "__main__":
    print("-" * 60)
    print("Decode string")
    print("-" * 60)

    test_cases = [
        ("2[a]", "aa"),
        ("m2[a]m", "maam"),
        ("m2[a]3[g2[o]al]", "maagooalgooalgooal"),
        (
            "2[2[2[2[2[abc]]3[cd]]e]f]",
            "abcabcabcabccdcdcdabcabcabcabccdcdcdeabcabcabcabccdcdcdabcabcabcabccdcdcdefabcabcabcabccdcdcdabcabcabcabccdcdcdeabcabcabcabccdcdcdabcabcabcabccdcdcdef",
        ),
    ]

    for s, solution in test_cases:

        print("Encoded string:", s)

        result = one_stack(s)
        test_ok = solution == result
        output = f"     one_stack = "
        if len(result) > 35:
            output += "".join(result[:30]) + "..."
        else:
            output += result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = one_stack2(s)
        test_ok = solution == result
        output = f"    one_stack2 = "
        if len(result) > 35:
            output += "".join(result[:30]) + "..."
        else:
            output += result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = one_stack3(s)
        test_ok = solution == result
        output = f"    one_stack3 = "
        if len(result) > 35:
            output += "".join(result[:30]) + "..."
        else:
            output += result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = two_stacks(s)
        test_ok = solution == result
        output = f"    two_stacks = "
        if len(result) > 35:
            output += "".join(result[:30]) + "..."
        else:
            output += result

        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = recursion(s)
        test_ok = solution == result
        output = f"     recursion = "
        if len(result) > 35:
            output += "".join(result[:30]) + "..."
        else:
            output += result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
