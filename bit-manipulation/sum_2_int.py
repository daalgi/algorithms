"""
https://leetcode.com/problems/sum-of-two-integers/

Given two integers a and b, return the sum of the two 
integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

Constraints:
-1000 <= a, b <= 1000
"""


def sum2int(a: int, b: int) -> int:
    # Python allows arbitrary length integers, so we
    # use a mask to restrict the length to 32 bits.
    # This effectively adds 0s to the left up until infinite...
    mask = 0xFFFFFFFF

    # Loop over until `b` is 0.
    # `a` is going to keep track of the "whole" sum
    # `b` is going to keep track of the "carry part" of the sum
    while b:
        # XOR operator to simulate addition, with the mask
        # to restrict it to 32 bits
        sum = (a ^ b) & mask

        # AND operator only affects the bits whose sum
        # need a "carry", then we shift left,
        # so the carry is applied in the correct bit position.
        # Again, we use the mask to restrict it to 32 bits
        carry = ((a & b) << 1) & mask

        # For next iteration
        # `a` keeps the "whole" sum, but the current
        # "carry part" is added in the next iteration
        a = sum
        # `b` represents the current "carry part" of the sum
        b = carry

    # Handle negative integers (32-bit like integers),
    if a >> 31 & 1:
        # If the leftmost bit is set,
        # it's a negative 32-bit integer.
        # However, python thinks it's just a large integer
        # (python has infinite length integers), because all
        # the bits to the left are 0s.
        # We need to convert the 32 bits negative integer
        # into an infinite bits negative integer.
        # We can do it by using the 2s complement:
        # -n = ~n + 1
        # However, we can't use "+" or "-".
        # There's an usefull relationship:
        # ~(x + 1) + 1 = ~x
        # Additionally, given that in python the ~ operator
        # flips infinite bits and we only need to flip 32 bits,
        # we're going to use XOR with the mask (all 1s, 0xffffffff),
        # that will have the same result as flipping:
        # ~x = ~(a ^ mask),
        return ~(a ^ mask)

    return a


if __name__ == "__main__":
    print("-" * 60)
    print("Sum of two integers")
    print("-" * 60)

    test_cases = [
        (0, 1, 1),
        (2, 1, 3),
        (2, 3, 5),
        (0, 8, 8),
        (25, 6, 31),
        (8, 8, 16),
        (0, -1, -1),
        (5, -1, 4),
        (-5, -1, -6),
        (-8, -16, -24),
    ]

    for a, b, solution in test_cases:
        string = f"sum2int{a, b} = "
        string += " " * (15 - len(string))
        result = sum2int(a, b)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
