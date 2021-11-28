"""
https://leetcode.com/problems/divide-two-integers/

Given two integers dividend and divisor, divide two integers 
without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which 
means losing its fractional part. For example, 8.345 
would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that 
could only store integers within the 32-bit signed 
integer range: [−231, 231 − 1]. For this problem, 
if the quotient is strictly greater than 231 - 1, 
then return 231 - 1, and if the quotient is strictly 
less than -231, then return -231.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Example 3:
Input: dividend = 0, divisor = 1
Output: 0

Example 4:
Input: dividend = 1, divisor = 1
Output: 1

Constraints:
-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0
"""


def brute_force(dividend: int, divisor: int) -> int:
    # Time complexity: O(n), where n is the
    # quotient dividend / divisor

    # Edge cases: overflow
    int_min_magnitude = 2 ** 31
    if dividend == -int_min_magnitude and divisor == -1:
        return int_min_magnitude - 1

    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    if not positive:
        quotient = -quotient
    return quotient


def bit_manip(dividend: int, divisor: int) -> int:
    # Every integer can be expressed as a power of 2.
    # We need to find the greatest `x`
    # that satisfies `dividend - x * divisor >= 0`
    # Time complexity - Worst case O(logN * logN)

    # Edge cases: overflow
    int_min = -(2 ** 31)
    if dividend == int_min and divisor == -1:
        return int_min - 1

    # Sign of the result
    positive = (dividend < 0) is (divisor < 0)
    # Work with positive integers
    dividend, divisor = abs(dividend), abs(divisor)
    # Variable to keep the result
    quotient = 0
    # Loop over until the dividend is less than the divisor.
    # Instead of increasing +1 at each iteration,
    # we can increase by powers of two:
    # 1, 2, 4, 8, 16, 32, ...
    # and when the dividend is exceeded, start over 1, 2, 4, ...
    while dividend >= divisor:  # O(logN)
        accum, i = divisor, 1
        # Loop over while there's no overflow
        while accum < (-int_min >> 1) and dividend <= (accum >> 1):
            # Worst case: O(logN)
            i <<= 1
            accum <<= 1
        dividend -= accum
        quotient += i

    # If the result was negative, change the sign
    if not positive:
        quotient = -quotient
    # Return the result, limited to 32bit numbers
    return quotient


def bit_manip2(dividend: int, divisor: int) -> int:
    # https://leetcode.com/problems/divide-two-integers/discuss/13403/Clear-python-code

    # Edge cases: overflow
    int_min = -(2 ** 31)
    if dividend == int_min and divisor == -1:
        return int_min - 1

    positive = (dividend < 0) is (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        accum, i = divisor, 1
        while dividend >= accum:
            dividend -= accum
            res += i
            i <<= 1
            accum <<= 1
    if not positive:
        res = -res
    return res


def bit_manip3(dividend: int, divisor: int) -> int:
    # Time complexity: O(32) = O(1)

    # Edge case: overflow
    if dividend == -2147483648 and divisor == -1:
        return 2147483647

    # Is the result positive?
    is_positive = (dividend > 0) is (divisor > 0)
    # Simplify by assuming only positive numbers
    dividend, divisor = abs(dividend), abs(divisor)
    # Loop over the 32 powers of two for a 32bit number
    quotient = 0
    for x in range(32)[::-1]:
        if (dividend >> x) - divisor >= 0:
            quotient += 1 << x
            dividend -= divisor << x
    return quotient if is_positive else -quotient


if __name__ == "__main__":
    print("-" * 60)
    print("Divide two integers")
    print("-" * 60)

    test_cases = [
        (2, 1, 2),
        (3, 2, 1),
        (8, 3, 2),
        (9, 3, 3),
        (64, 7, 9),
        (86868686, 8693, 9992),
    ]

    for dividend, divisor, solution in test_cases:
        string = f"brute_force{dividend, divisor} = "
        string += " " * (25 - len(string))
        result = brute_force(dividend, divisor)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f"  bit_manip{dividend, divisor} = "
        string += " " * (25 - len(string))
        result = bit_manip(dividend, divisor)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f" bit_manip2{dividend, divisor} = "
        string += " " * (25 - len(string))
        result = bit_manip2(dividend, divisor)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f" bit_manip3{dividend, divisor} = "
        string += " " * (25 - len(string))
        result = bit_manip3(dividend, divisor)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
