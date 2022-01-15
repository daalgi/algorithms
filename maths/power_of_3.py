"""
https://leetcode.com/problems/power-of-three/

Given an integer n, return true if it is a power of three. 
Otherwise, return false.

An integer n is a power of three, if there exists an 
integer x such that n == 3x.

Example 1:
Input: n = 27
Output: true

Example 2:
Input: n = 0
Output: false

Example 3:
Input: n = 9
Output: true

Constraints:
-2^31 <= n <= 2^31 - 1 

Follow up: Could you solve it without loops/recursion?
"""


def loop(n: int) -> bool:
    # Time complexity: O(log3(n))
    # Space complexity: O(1)

    # Numbers n < 0 are not a power of 3
    # n = 1 is a power of three: 3⁰ = 1
    if n < 1:
        return False

    # Loop while `n` is divisible by `3`
    while n % 3 == 0:
        n //= 3

    # If `n` was a power of three,
    # the last iterations were:
    #   9 --> 9 // 3 = 3 --> 3 % 3 = 0
    #   3 --> 3 // 3 = 1 --> 1 % 3 = 1
    # Therefore, `n` must be 1 now,
    # otherwise it was not a power of three
    return n == 1


def recursion(n: int) -> bool:
    # Time complexity: O(log3(n))
    # Space complexity: O(log3(n))
    if n == 1:
        return True
    if n < 1 or n % 3 != 0:
        return False
    
    return recursion(n // 3)


def math(n: int) -> bool:
    # Time complexity: O(1)
    # Space complexity: O(1)
    # Note: max power of three for a 32-bit signed integer is 3¹⁹
    # return n > 0 and 3 ** 19 % n == 0
    return n > 0 == 3 ** 19 % n


if __name__ == "__main__":
    print("-" * 60)
    print("Power of 3")
    print("-" * 60)

    test_cases = [
        (-3, False),
        (0, False),
        (1, True),
        (2, False),
        (3, True),
        (9, True),
        (15, False),
        (27, True),
        (64, False),
        (81, True),
        (2 ** 31 - 1, False),
        (3 ** 15, True),
        (3 ** 19, True),
    ]

    for n, solution in test_cases:

        print(f"Number:", n)

        result = loop(n)
        output = f"       loop = "
        output += " " * (15 - len(output))
        test_ok = solution == result
        output += f"{str(result)}"
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = recursion(n)
        output = f"  recursion = "
        output += " " * (15 - len(output))
        test_ok = solution == result
        output += f"{str(result)}"
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = math(n)
        output = f"       math = "
        output += " " * (15 - len(output))
        test_ok = solution == result
        output += f"{str(result)}"
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
