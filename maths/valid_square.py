"""
https://leetcode.com/problems/valid-square/

Given the coordinates of four points in 2D space 
p1, p2, p3 and p4, return true if the four points 
construct a square.

The coordinate of a point pi is represented as 
[xi, yi]. The input is not given in any order.

A valid square has four equal sides with positive 
length and four equal angles (90-degree angles).

Example 1:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true

Example 2:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false

Example 3:
Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true

Constraints:
p1.length == p2.length == p3.length == p4.length == 2
-10^4 <= xi, yi <= 10^4
"""
from typing import List


def brute_force(
    p1: List[int], p2: List[int], p3: List[int], p4: List[int]
) -> bool:
    # Time complexity: O(4!) = O(1)
    # Space complexity: O(1)

    # A square has four sides of equal length, and
    # two diagonals of equal length.
    # If we compute the length between all the points,
    # a square will have only two unique lengths:
    # side and diagonal.
    # We can measure the distances between all points
    # and store them in a hashset.

    def dist(p: List[int], q: List[int]) -> int:
        # Compute the square distance to avoid using square-roots
        # and possible precission problems
        return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])

    # Hashset to count the number of different distances between points
    count = set(
        [
            dist(p1, p2),
            dist(p1, p3),
            dist(p1, p4),
            dist(p2, p3),
            dist(p3, p4),
        ]
    )

    # If there's no zero-length side and the total number of different
    # distances is equal to two, it's a square
    return 0 not in count and len(count) == 2


def sorting(
    p1: List[int], p2: List[int], p3: List[int], p4: List[int]
) -> bool:
    # Time complexity: O(4!) = O(1)
    # Space complexity: O(1)

    # Instead of considering all the permutations of possible arrangements,
    # we can sort the set of points, so we'll always have
    #   points = sorted([p1, p2, p3, p4]) = [q1, q2, q3, q4]
    #   sides: dist(q1, q2), dist(q1, q3), dist(q2, q4), dist(q3, q4)
    #   diagonals: dist(q1, q4), dist(q2, q3)

    def dist(p: List[int], q: List[int]) -> int:
        # Compute the square distance to avoid using square-roots
        # and possible precission problems
        return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])

    q1, q2, q3, q4 = sorted([p1, p2, p3, p4])

    return (
        # Equal non-zero sides
        dist(q1, q2) == dist(q1, q3) == dist(q2, q4) == dist(q3, q4) != 0
        # Equal diagonals
        and dist(q1, q4) == dist(q2, q3)
    )


if __name__ == "__main__":
    print("-" * 60)
    print("Valid square")
    print("-" * 60)

    test_cases = [
        # (points, solution)
        ([[0, 0], [1, 1], [0, 1], [1, 0]], True),
        ([[0, 0], [1, 1], [0, 0], [0, 0]], False),
        ([[0, 0], [1, 1], [1, 0], [0, 12]], False),
        ([[1, 0], [-1, 0], [0, 1], [0, -1]], True),
        ([[2, 2], [2, 6], [0, 4], [4, 4]], True),
    ]

    for points, solution in test_cases:

        print("Points:", points)

        result = brute_force(*points)
        output = f"   brute_force = "
        test_ok = solution == result
        output += f"{str(result)}"
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sorting(*points)
        output = f"       sorting = "
        test_ok = solution == result
        output += f"{str(result)}"
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
