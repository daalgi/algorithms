"""
https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x 
raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
-10^4 <= xn <= 10^4
"""
from functools import lru_cache


def recursion(x: float, n: int) -> float:
    # Time complexity: O(n)
    # Space complexity: O(n)

    if n == 0:
        return 1

    if n <= 0:
        return 1 / x * recursion(x, n + 1)

    return x * recursion(x, n - 1)


@lru_cache(maxsize=None)
def recursion_opt(x: float, n: int) -> float:
    # Time complexity: O(logn)
    # Space complexity: O(logn)

    if n == 0:
        return 1

    if n < 0 and n & 1:
        return 1 / x * recursion_opt(x, n + 1)

    if n & 1:
        return x * recursion_opt(x, n - 1)

    half_n = n >> 1
    return recursion_opt(x, half_n) * recursion_opt(x, half_n)


def recursion_opt2(x: float, n: int) -> float:
    # Time complexity: O(logn)
    # Space complexity: O(logn)

    if n == 0:
        return 1

    if n < 0 and n & 1:
        return 1 / recursion_opt2(x, -n)

    if n & 1:
        return x * recursion_opt2(x, n - 1)

    return recursion_opt2(x * x, n >> 1)


def iterative(x: float, n: int) -> float:
    # Time complexity: O(n)
    # Space complexity: O(1)

    increment = +1 if n > 0 else -1
    res = 1
    p = 0
    while abs(p) < abs(n):
        if increment > 0:
            res *= x
        else:
            res /= x
        p += increment
    return res


def iterative_opt(x: float, n: int) -> float:
    # Time complexity: O(logn)
    # Space complexity: O(1)

    increment = +1 if n > 0 else -1
    res = 1
    p = 0
    while abs(p) < abs(n):

        if n & 1:

            if increment > 0:
                res *= x
            else:
                res /= x
            p += increment

        else:

            res *= res
            p *= p

    return res


def iterative_opt2(x: float, n: int) -> float:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    """
    while n:
        if n & 1:
            # Example iter 1:
            #   x = 3, res = 9, n = 3
            #   --> res = 9 * 3 = 27
            # Example iter 2:
            #   x = 9, res = 9, n = 1
            #   --> res = 27 * 9 = 243
            res *= x

        # Example iter 1:
        # x = 3 * 3 = 9
        # n = 3 // 2 = 1
        # Example iter 2:
        # x = 9 * 9 = 81
        # n = 1 // 2 = 0
        x *= x
        n >>= 1

    res = 243
    """
    if n < 0:
        x = 1 / x
        n = -n

    res = 1
    while n:
        if n & 1:
            res *= x
        x *= x
        n >>= 1

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Pow(x, n)")
    print("-" * 60)

    test_cases = [
        # (string_s, string_t, solution)
        (99, 0, 1),
        (99, 1, 99),
        (99, -1, 1 / 99),
        (2, -3, 0.125),
        (5, 3, 125),
        (1.000000001, 999999999999999999999999, float("inf")),
        (999999999999999999999, -999999999999999999999999, 0),
    ]

    for x, n, solution in test_cases:

        print(f" {x}^{n}")

        if abs(n) < 100:
            result = recursion(x, n)
            output = f"      recursion = "
            output += " " * (10 - len(output))
            test_ok = solution == result
            output += str(result)
            output += " " * (55 - len(output))
            output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
            print(output)

            result = recursion_opt2(x, n)
            output = f" recursion_opt2 = "
            output += " " * (10 - len(output))
            test_ok = solution == result
            output += str(result)
            output += " " * (55 - len(output))
            output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
            print(output)

            result = iterative(x, n)
            output = f"      iterative = "
            output += " " * (10 - len(output))
            test_ok = solution == result
            output += str(result)
            output += " " * (55 - len(output))
            output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
            print(output)

            result = iterative_opt(x, n)
            output = f"  iterative_opt = "
            output += " " * (10 - len(output))
            test_ok = solution == result
            output += str(result)
            output += " " * (55 - len(output))
            output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
            print(output)

        result = recursion_opt(x, n)
        output = f"  recursion_opt = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = iterative_opt2(x, n)
        output = f" iterative_opt2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
