"""
https://leetcode.com/problems/basic-calculator-iii/

Implement a basic calculator to evaluate a 
simple expression string.

The expression string contains only non-negative integers, 
'+', '-', '*', '/' operators, and open '(' and closing 
parentheses ')'. The integer division should truncate 
toward zero.

You may assume that the given expression is always valid. 
All intermediate results will be in the range of [-2^31, 2^31 - 1].

Note: You are not allowed to use any built-in function which 
evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "1+1"
Output: 2

Example 2:
Input: s = "6-4/2"
Output: 4

Example 3:
Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21

Constraints:
1 <= s <= 10^4
s consists of digits, '+', '-', '*', '/', '(', and ')'.
s is a valid expression.
"""
from collections import deque


def has_precedence(curr_op: str, prev_op: str) -> bool:
    if prev_op == "(":
        return False
    if (curr_op == "*" or curr_op == "/") and (prev_op == "+" or prev_op == "-"):
        return False
    return True


def process_operation(operator: str, right: int, left: int) -> float:
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        # Integer division truncated towards zero
        if left * right > 0:
            return left // right
        return (left + (-left % right)) // right
    return right


def two_stacks(s: str) -> float:
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Strategy: use two stacks (numbers and operations)

    OPERATORS = set(["+", "-", "*", "/", "(", ")"])
    
    i, n, num, numbers, operators = 0, len(s), 0, deque(), deque()
    while i < n:
        c = s[i]

        if c.isdigit():
            # Form the number (operand)
            num = int(c)
            i += 1
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            # Undo the last `i` increment, since it'll be
            # increased again at the end of the loop
            i -= 1

            # Store the number
            numbers.append(num)

        elif c in OPERATORS:

            if c == "(":
                operators.append(c)

            elif c == ")":
                # Compute operations until we find the
                # corresponding open parenthesis
                while operators[-1] != "(":
                    numbers.append(
                        process_operation(
                            operator=operators.pop(),
                            right=numbers.pop(),
                            left=numbers.pop(),
                        )
                    )
                # Remove the open parenthesis "(" from the
                # `operations` stack
                operators.pop()

            else:  # if c in ["+", "-", "*", "/"]

                while operators and has_precedence(c, operators[-1]):
                    numbers.append(
                        process_operation(
                            operator=operators.pop(),
                            right=numbers.pop(),
                            left=numbers.pop(),
                        )
                    )
                operators.append(c)

        # Next char
        i += 1

    while operators:
        numbers.append(
            process_operation(
                operator=operators.pop(),
                right=numbers.pop(),
                left=numbers.pop(),
            )
        )

    return numbers[-1]


if __name__ == "__main__":
    print("-" * 60)
    print("Basic calculator III")
    print("-" * 60)

    test_cases = [
        ("1+1", 2),
        ("1/2", 0),
        ("5/2", 2),
        ("3+1+6+3", 13),
        ("10 + 2 * 6", 22),
        ("(10 + 2) * 6", 72),
        ("((10 + 2) / 2) * (6 - 6/2)", 18),
        ("10/(2+3)", 2),
        ("3-1", 2),
        ("3-1-2-3", -3),
        ("1*2*3", 6),
        ("1*2*3+2", 8),
        ("1*2*3-4", 2),
        ("1*3/3", 1),
        ("(0-3)/4", 0),
        ("(0-3)/(1-5)", 0),
        ("3/(1-5)", 0),
        ("2*(5+5*2)/3+(6/2+8)", 21),
        ("3+5*8*(84/((1+1)*2)/2*2)-1", 802),
    ]

    for s, solution in test_cases:

        print("Expression:", s)

        result = two_stacks(s)
        output = f"    two_stacks = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
