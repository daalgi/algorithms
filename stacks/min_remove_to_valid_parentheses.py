"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of 
parentheses ( '(' or ')', in any positions ) so that the 
resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), 
where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Constraints:
1 <= s.length <= 10^5
s[i] is either'(' , ')', or lowercase English letter.
"""
from collections import deque


def greedy(s: str) -> str:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Convert the input string into a list to be able
    # to modify characters more efficiently
    s = list(s)

    # Loop over the characters of the string,
    # and add the indices of the open parentheses
    # to a stack
    stack = deque()
    n = len(s)
    for i in range(n):
        if s[i] == "(":
            # Add the index of the open parenthesis to
            # the stack
            stack.append(i)
        elif s[i] == ")":
            # Closing parenthesis
            if stack:
                # If there's a matching open parenthesis,
                # pop it from the stack
                stack.pop()
            else:
                # If there's no matching open parenthesis,
                # we have to remove it from the string
                s[i] = ""

    # If the stack is not empty, remove the characters
    # of the non-matched open parentheses
    while stack:
        i = stack.pop()
        s[i] = ""

    return "".join(s)


if __name__ == "__main__":
    print("-" * 60)
    print("Minimum remove to make valid parentheses")
    print("-" * 60)

    test_cases = [
        ("(", ""),
        (")", ""),
        ("(*)))", "(*)"),
        ("))((", ""),
        ("a)b(c)d", "ab(c)d"),
        ("lee(t(c)o)de)", "lee(t(c)o)de"),
    ]

    for s, solution in test_cases:

        print("String:", s)
        result = greedy(s)
        output = f"     greedy = "
        output += " " * (20 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
