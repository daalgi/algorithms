"""
https://leetcode.com/problems/valid-parentheses/

Given a string s, determine if the parentheses are well placed.

An input string is valid if:
1 - Open brackets must be closed by the same type of brackets.
2 - Open brackets must be closed in the correct order.

Example 1:
Input: s = "(a)"
Output: true

Example 2:
Input: s = "(a)bc[]d{e}"
Output: true

Example 3:
Input: s = "a(]"
Output: false

Example 4:
Input: s = "([c)]"
Output: false

Example 5:
Input: s = "{a[b]c}d"
Output: true

Constraints:
1 <= s.length <= 10^4
"""
from collections import deque


def stack(s: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(n)
    parentheses_set = set(["(", ")", "{", "}", "[", "]"])
    parentheses = {"(": ")", "{": "}", "[": "]"}
    stack = deque()

    # Loop over the characters of the string
    for c in s:

        if c in parentheses_set:
            # If the character is a parenthesis

            if len(stack) == 0 and c not in parentheses:
                # If the stack is empty, the first parenthesis
                # must be an opening one, that is,
                # must be in the keys of the dictionary `parentheses`,
                # otherwise it's not a valid
                return False

            elif c in parentheses:
                # If the character is an openening parenthesis, add its
                # corresponding closing parenthesis
                # to the stack to be compared with later characters
                stack.append(parentheses[c])

            else:
                # If the character is a closing parentheses
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


def stack2(s: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(n)
    parentheses_set = set(["(", ")", "{", "}", "[", "]"])
    parentheses = {"(": ")", "{": "}", "[": "]"}
    stack = deque()

    for c in s:
        if c in parentheses_set:
            if c in parentheses:
                stack.append(c)
            else:
                if not stack or c != parentheses[stack[-1]]:
                    return False
    return not stack


if __name__ == "__main__":
    print("-" * 60)
    print("Valid parentheses (any character)")
    print("-" * 60)

    test_cases = [
        ("(", False),
        ("(abc)", True),
        ("a(b]c", False),
        ("{aab(c}d]e", False),
        ("a(b)c[de]f(g)h", True),
        ("a(bc[]de(f)g)hijk", True),
        ("([a],(12{s[c]{()}}()))", True),
        ("([]11(1{[]2{()2}}(a)])", False),
    ]

    for s, solution in test_cases:

        print(f"Parentheses:\t'{s}'")

        result = stack(s)
        output = f"\t   stack = "
        output += " " * (20 - len(output))
        output += str(result)
        test_ok = solution == result
        output += " " * (35 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = stack(s)
        output = f"\t  stack2 = "
        output += " " * (20 - len(output))
        output += str(result)
        test_ok = solution == result
        output += " " * (35 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
