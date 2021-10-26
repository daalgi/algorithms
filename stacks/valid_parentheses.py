"""
https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1 - Open brackets must be closed by the same type of brackets.
2 - Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
from collections import deque


def valid_parentheses(s: str) -> bool:
    parentheses = {"(": ")", "{": "}", "[": "]"}
    stack = deque()

    # Loop over the characters of the string
    for c in s:
        if len(stack) == 0 and c not in parentheses:
            # All the characters are parentheses,
            # and the first one must be in the keys of the
            # dictionary `parentheses`,
            # otherwise it's not a valid
            return False
        elif c in parentheses:
            # If the character is in `parentheses`, add its
            # closing parenthesis to the stack to be compared
            # with later characters
            stack.append(parentheses[c])
        else:
            # If the character is not an opening parentheses
            if c == stack[-1]:
                # If the character is the closing parenthesis
                # corresponding to the last added to the stack,
                # so far ok, so remove it from the stack
                stack.pop()
            else:
                # If the character is not the suitable closing
                # parenthesis, the string is not valid
                return False

    # If all the parentheses are balanced, 
    # the stack should be empty
    return len(stack) == 0


if __name__ == "__main__":
    print("-" * 60)
    print("Valid parentheses (only parentheses characters)")
    print("-" * 60)

    test_cases = [
        ("(", False),
        ("()", True),
        ("(]", False),
        ("{(}]", False),
        ("()[]()", True),
        ("([]())", True),
        ("([]({[]{()}}()))", True),
        ("([]({[]{()}}()])", False),
    ]

    for s, solution in test_cases:

        result = valid_parentheses(s)
        string = f'valid_parentheses("{s}") = '
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')