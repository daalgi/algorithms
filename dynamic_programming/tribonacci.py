"""
https://leetcode.com/problems/n-th-tribonacci-number/

The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537

Constraints:
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, 
ie. answer <= 2^31 - 1.
"""
import time


def iterative_memory_o1(n: int) -> int:
    if n == 0:
        return 0
    if n < 3:
        return 1

    a, b, c = 0, 1, 1
    for _ in range(3, n + 1):
        c, b, a = c + b + a, c, b

    return c


if __name__ == "__main__":

    print("-" * 60)
    print("N-th Tribonacci number")
    print("-" * 60)

    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 4),
        (5, 7),
        (8, 44),
        (13, 927),
        (37, 2082876103),
    ]

    for n, solution in test_cases:

        result = iterative_memory_o1(n)
        string = f"iterative_memory_O(1)({n}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
