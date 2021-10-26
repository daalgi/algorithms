"""
CRACKING THE CODING INTERVIEW
16.26. Calculator:
Given an arithmetic equation consisting of positive ingegers,
+, -, * and / (no parentheses), compute the result.

Example 1:
Input: s = "2*3+5/6*3+15"
Output: 23.5
"""
from collections import deque


class Operator:
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    OPEN_PARENTHESIS = "("
    CLOSE_PARENTHESIS = ")"


def is_operator(c: str) -> bool:
    if any(
        c == o
        for o in [
            Operator.ADD,
            Operator.SUBTRACT,
            Operator.MULTIPLY,
            Operator.DIVIDE,
            Operator.OPEN_PARENTHESIS,
            Operator.CLOSE_PARENTHESIS,
        ]
    ):
        return True
    return False


def precedence(operator: str) -> int:
    if operator == Operator.OPEN_PARENTHESIS or operator == Operator.CLOSE_PARENTHESIS:
        return 3
    elif operator == Operator.MULTIPLY or operator == Operator.DIVIDE:
        return 2
    elif operator == Operator.ADD or operator == Operator.SUBTRACT:
        return 1
    return -1


def process_operation(left, operator: str, right) -> float:
    if operator == Operator.ADD:
        return left + right
    if operator == Operator.SUBTRACT:
        return left - right
    if operator == Operator.MULTIPLY:
        return left * right
    if operator == Operator.DIVIDE:
        return left / right
    return right


def sol1(s: str) -> float:
    # TODO make it work
    operators = set(["+", "-", "*", "/"])
    # Last operator * or /
    last_op = ""
    # Keep track of the digits of the current number
    digits = []
    # Value of the current addend
    addend = None
    # Store the final result
    res = 0
    # Loop over the characters of the string
    for c in s:

        if c in operators:
            # If the current character is an operator,
            # parse the integer of the number made of the
            # accumulated digits
            if digits:
                num = float("".join(digits))
            else:
                # addend
                pass
            # print('--->', num)
            # print('operator', c)

            # If the previous operator was * or /,
            # compute the previous operation within the current addend
            if last_op == Operator.MULTIPLY or last_op == Operator.DIVIDE:
                addend = process_operation(addend, last_op, num)

            # print('addend', addend)
            # Check current operator
            last_op = c
            if c == Operator.ADD or c == Operator.SUBTRACT:
                # If + or -, sum the current addend (with its sign)
                # to the result
                if addend is None:
                    addend = num
                res = process_operation(res, Operator.ADD, addend)
                # Restart the addend with the corresponding sign
                addend = 1 if c == Operator.ADD else -1
            # print('res', res)

            # Clear the digits list
            digits = []

        elif c.isnumeric():

            # Add digit
            digits.append(c)

    # Add last number
    num = float("".join(digits))
    if last_op == Operator.ADD or last_op == Operator.SUBTRACT:
        addend = process_operation(addend, Operator.MULTIPLY, num)
    else:
        addend = process_operation(addend, last_op, num)

    # return process_operation(res, last_op, addend)
    return res + addend


def stacks(s: str) -> float:
    # Operators and values stacks
    ops = deque()
    nums = deque()

    # Temporary variables
    num = 0

    # Loop over the characters of the string
    n = len(s)
    i = 0
    while i < n:

        current = s[i]
        # print(i, "-->", nums, ops, current)

        if current.isdigit():
            # If the current number is a digit
            # initialize the buffer
            num = 0

            # If it's a digit, add it to the buffer `num`
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1

            # Add the resulting number into the stack
            nums.append(num)

            # Compensate the last increment of `i` in the loop
            i -= 1

        elif is_operator(current):

            # Loop over until the operators' stack is empty or
            # the current operator precedence is greater than the
            # last in the stack
            # print(nums, ops)
            while len(ops) and precedence(current) <= precedence(ops[-1]):
                right = nums.pop()
                left = nums.pop()
                operator = ops.pop()
                res = process_operation(left, operator, right)
                nums.append(res)

            ops.append(current)

        # Update for next iter
        i += 1

    # Perform the remaining operations until the
    # stack `ops` is empty
    while len(ops):
        right = nums.pop()
        left = nums.pop()
        operator = ops.pop()
        res = process_operation(left, operator, right)
        nums.append(res)

    # Return the last number in the `nums` stack
    return nums.pop()


if __name__ == "__main__":
    print("-" * 60)
    print("Calculator")
    print("-" * 60)

    test_cases = [
        ("1+1", 2),
        ("2+1", 3),
        ("3+1+6", 10),
        ("3+1+6+3", 13),
        ("10 + 2 * 6", 22),
        ("3-1", 2),
        ("3-1-2-3", -3),
        # ("-3+1", -2), # not detecting the first negative sign so far
        ("1+1+2+4", 8),
        ("1*2", 2),
        ("1*2*3", 6),
        ("1*2*3+2", 8),
        ("1*2*3-4", 2),
        ("1+2", 3),
        ("1*3+2", 5),
        ("1*3/3", 1),
        ("2*3+5/6*3+15", 23.5),
    ]

    for s, solution in test_cases:

        result = stacks(s)
        string = f'stacks("{s}") = '
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
