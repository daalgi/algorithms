"""
https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

You are working in a ball factory where you have n balls numbered 
from lowLimit up to highLimit inclusive 
(i.e., n == highLimit - lowLimit + 1), and an infinite number 
of boxes numbered from 1 to infinity.

Your job at this factory is to put each ball in the box with a 
number equal to the sum of digits of the ball's number. 
For example, the ball number 321 will be put in the box 
number 3 + 2 + 1 = 6 and the ball number 10 will be put in the 
box number 1 + 0 = 1.

Given two integers lowLimit and highLimit, return the number of 
balls in the box with the most balls.

Example 1:
Input: lowLimit = 1, highLimit = 10
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
Box 1 has the most number of balls with 2 balls.

Example 2:
Input: lowLimit = 5, highLimit = 15
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
Boxes 5 and 6 have the most number of balls with 2 balls in each.

Example 3:
Input: lowLimit = 19, highLimit = 28
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
Box 10 has the most number of balls with 2 balls.

Constraints:
1 <= lowLimit <= highLimit <= 10^5
"""


def brute_force(low_limit: int, high_limit: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    count = dict()
    for ball in range(low_limit, high_limit + 1):
        box = 0
        while ball:
            box += ball % 10
            ball //= 10
        count[box] = count.get(box, 0) + 1

    return max(v for v in count.values())


if __name__ == "__main__":
    print("-" * 60)
    print("Maximum number of balls in a box")
    print("-" * 60)

    test_cases = [
        # (low_limit, high_limit, solution)
        (1, 10, 2),
        (5, 15, 2),
        (19, 28, 2),
        (50, 100000, 6000),
    ]

    for low_limit, high_limit, solution in test_cases:

        output = f" Low limit: {low_limit}"
        output += f"\nHigh limit: {high_limit}"
        print(output)

        result = brute_force(low_limit, high_limit)
        output = f"\t     brute_force = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
