"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate the value of an arithmetic expression 
in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand 
may be an integer or another expression.

Note that division between two integers should 
truncate toward zero.

It is guaranteed that the given RPN expression is 
always valid. That means the expression would always 
evaluate to a result, and there will not be any 
division by zero operation.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = 
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 
Constraints:
1 <= tokens.length <= 10^4
tokens[i] is either an operator: "+", "-", "*", or "/", 
or an integer in the range [-200, 200].
"""
from typing import List
from collections import deque


def process_operation(operator: str, right: int, left: int) -> float:
    # print("Operation:", (left, operator, right))
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        # Integer division truncated towards zero
        # Method 1:
        # if left * right > 0:
        #     return left // right
        # return (left + (-left % right)) // right
        # Method 2:
        return int(left / right)
    return right


def stack(tokens: List[str]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    numbers = deque()
    for token in tokens:
        if token.isnumeric() or (token[0] == "-" and len(token) > 1):
            numbers.append(int(token))
        else:
            numbers.append(
                process_operation(
                    operator=token, right=numbers.pop(), left=numbers.pop()
                )
            )
    return numbers[-1]


if __name__ == "__main__":
    print("-" * 60)
    print("Evaluate reverse Polish notation")
    print("-" * 60)

    test_cases = [
        (["1"], 1),
        (["1", "7", "+"], 8),
        (["-1", "2", "/"], 0),
        (["1", "-2", "/"], 0),
        (["-3", "-2", "/"], 1),
        (["-3", "2", "/"], -1),
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ]

    for tokens, solution in test_cases:

        print("Tokens:", tokens)

        result = stack(tokens)
        output = f"    stacks = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
