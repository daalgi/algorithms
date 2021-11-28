"""
https://leetcode.com/problems/power-of-four/

Given an integer n, return true if it is a power of four. 
Otherwise, return false.

An integer n is a power of four, if there exists an 
integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true

Constraints:

-2^31 <= n <= 2^31 - 1
"""


def power_of_4(n: int) -> int:
    # 1 - only positive numbers can be power of 4
    # 2 - powers of 4 are also powers of 2
    # 3 - OR with a mask where the power of 4 bits are set:
    # mask = 010101010101
    mask = 0xAAAAAAAA >> 1
    return n > 0 and n & (n - 1) == 0 and n | mask == mask


if __name__ == "__main__":
    print("-" * 60)
    print("Power of four")
    print("-" * 60)

    test_cases = [
        (0, False),
        (1, True),
        (2, False),
        (3, False),
        (4, True),
        (5, False),
        (6, False),
        (7, False),
        (8, False),
        (9, False),
        (10, False),
        (15, False),
        (16, True),
        (32, False),
        (64, True),
    ]

    for n, solution in test_cases:
        string = f"power_of_4({n}) = "
        string += " " * (25 - len(string))
        result = power_of_4(n)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
