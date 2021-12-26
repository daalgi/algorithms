"""
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

In a row of dominoes, tops[i] and bottoms[i] represent the top and 
bottom halves of the ith domino. (A domino is a tile with two numbers 
from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in 
tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

Example 1:
Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: 
before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value 
in the top row equal to 2, as indicated by the second figure.

Example 2:
Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row 
of values equal.

Constraints:
2 <= tops.length <= 2 * 10^4
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6
"""
from typing import List
from functools import lru_cache
from collections import Counter


def solution1(tops: List[int], bottoms: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)

    def count_swaps(ref: int, ref_array: List[int], other_array: List[int]) -> int:
        swaps = 0
        n = len(ref_array)
        # Loop over all the dominoes
        for i in range(n):
            if ref_array[i] != ref:
                if other_array[i] != ref:
                    # if there's no element `i` equal
                    # to the reference `ref`, solution
                    # not possible
                    return float("inf")

                # If the reference array's ith-element
                # is not equal to the reference number,
                # but the other array's ith-element is,
                # we can swap the domino
                swaps += 1
        return swaps

    min_swaps = min(
        # Try to make all `tops` equal to top[0]
        count_swaps(tops[0], tops, bottoms),
        # Try to make all `tops` equal to bottom[0]
        count_swaps(bottoms[0], tops, bottoms),
        # Try to make all `tops` equal to top[0]
        count_swaps(tops[0], bottoms, tops),
        # Try to make all `bottoms` equal to bottom[0]
        count_swaps(bottoms[0], bottoms, tops),
    )

    # If all the attemps were impossible, return -1;
    # otherwise, return the minimum number of swaps
    return -1 if min_swaps == float("inf") else min_swaps


def solution2(tops: List[int], bottoms: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    
    n = len(tops)
    # Count the occurrence of all numbers in `tops` and `bottoms`,
    # and also the dominoes with the same number at the top and bottom
    count_tops = [0] * 7
    count_bottoms = [0] * 7
    count_same = [0] * 7
    for i in range(n):
        count_tops[tops[i]] += 1
        count_bottoms[bottoms[i]] += 1
        if tops[i] == bottoms[i]:
            count_same[tops[i]] += 1

    # If it's possible to reach a solution, i.e. for number `2`: 
    #   count_tops[2] + count_bottoms[2] - count_same[2] = n
    # and then, the minimum number of swaps:
    #   n - max(count_tops[2], count_bottoms[2])
    for i in range(1, 7):
        if count_tops[i] + count_bottoms[i] - count_same[i] == n:
            return n - max(count_tops[i], count_bottoms[i])
    return -1


if __name__ == "__main__":
    print("-" * 60)
    print("Minimum domino rotations for equal row")
    print("-" * 60)

    test_cases = [
        # (tops, bottoms, solution)
        ([2, 5, 6], [5, 2, 2], 1),
        ([2, 5, 1], [5, 2, 1], -1),
        ([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2], 2),
        ([2, 1, 2, 4, 1, 1], [5, 2, 2, 2, 2, 2], 1),
        ([2, 5, 2, 5, 2, 1], [5, 6, 5, 4, 3, 1], -1),
    ]

    for tops, bottoms, solution in test_cases:

        output = f"   Tops: {tops}"
        output += f"\nBottoms: {bottoms}"
        print(output)

        result = solution1(tops, bottoms)
        output = f"\t     solution1 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = solution2(tops, bottoms)
        output = f"\t     solution2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
