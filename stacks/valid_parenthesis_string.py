"""
https://leetcode.com/problems/valid-parenthesis-string/

Given a string s containing only three types of characters: 
'(', ')' and '*', return true if s is valid.

The following rules define a valid string:
- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a 
single left parenthesis '(' or an empty string "".

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true

Constraints:
1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""
from collections import deque


def greedy1(s: str) -> bool:
    # NOTE: not passing one test (the last one)

    # Basic case
    if s[0] == ")" or s[-1] == "(":
        return False

    # Loop over the characters of the string
    # keeping track of the maximum and minimum
    # possible open and close parentheses, taking
    # into account that "*" can be both "(" or ")"
    open_max, open_min, close_max, close_min = 0, 0, 0, 0
    for c in s:
        if c == "(":
            open_max += 1
            open_min += 1
        elif c == ")":
            close_max += 1
            close_min += 1
        else:
            # "*" can be changed as both "(" and ")"
            open_max += 1
            close_max += 1

        if close_min > open_max:
            # Since we start from the left, if the minimum
            # close parentheses ")" is ever greater than the maximum
            # open parentheses "(" + "*", not valid
            return False

    # At the end of the string, the minimum open parentheses "("
    # must be less or equal than the maximum
    # close parentheses ")" + "*"
    return open_min <= close_max


def greedy2(s: str) -> bool:

    # Basic case
    if s[0] == ")" or s[-1] == "(":
        return False

    # Balance min, balance max refer to the not yet closed
    # parentheses count.
    # bmin: minimum number of closing parentheses
    # bmax: maximum number of open parentheses
    bmin, bmax = 0, 0
    # Loop over the characters of the string
    for c in s:
        if c == "(":
            # Open parentheses
            bmax += 1
            bmin += 1
        elif c == ")":
            # Closing parentheses
            bmax -= 1
            bmin -= 1
        else:
            # If "*", we can open a parenthesis or close it
            bmax += 1
            bmin -= 1

        if bmax < 0:
            # Not enough open parentheses to match closeing parentheses
            return False

        # Limit the number of closing parentheses.
        # If there are enough "*", we'll ignore the "*" not needed
        bmin = max(bmin, 0)

    # At the end, if the closing parentheses are balanced out,
    # is valid
    return bmin == 0


def greedy3(s: str) -> bool:
    """
    1 - Starting from the first char, 
        check if there're more open+wild than closed parentheses
    2 - Starting from the last char,
        check if there're more closed+wild than open parentheses
    If both checks are ok, the parentheses are valid.
    """
    # Time complexity: O(n)
    # Space complexity: O(n)
    def validate(s: str, ref: str) -> bool:
        bal, wild = 0, 0
        for i in range(n):
            if s[i] == "*":
                wild += 1
            else:
                bal += 1 if s[i] == ref else -1

            if bal + wild < 0:
                return False

        return bal <= wild

    n = len(s)
    return validate(s, "(") and validate(s[::-1], ")")


def stack(s: str) -> bool:
    # TODO
    pass


if __name__ == "__main__":
    print("-" * 60)
    print("Valid parentheses string")
    print("-" * 60)

    test_cases = [
        ("(", False),
        (")", False),
        ("(*)))", False),
        ("(*", True),
        ("(*)", True),
        ("((*)", True),
        ("(((*)", False),
        ("(((*)*", True),
        ("(((****(", False),
        ("((*))", True),
        ("((**))", True),
        ("**(*", True),
        ("**(**", True),
        ("**(***", True),
        ("(*(*", True),
        ("(**(*", True),
        ("(*((**", True),
        ("(*((***", True),
        ("(*((*", False),
        ("((*())", True),
        ("()()", True),
        ("(()*)", True),
        (
            "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())",
            False,
        ),
    ]

    for s, solution in test_cases:

        result = greedy1(s)
        output = f'greedy1("{s}") = '
        output += " " * (35 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = greedy2(s)
        output = f'greedy2("{s}") = '
        output += " " * (35 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = greedy3(s)
        output = f'greedy2("{s}") = '
        output += " " * (35 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
