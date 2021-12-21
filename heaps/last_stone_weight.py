"""
https://leetcode.com/problems/last-stone-weight/

You are given an array of integers stones where stones[i] is the 
weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the 
heaviest two stones and smash them together. Suppose the heaviest 
two stones have weights x and y with x <= y. The result of this smash is:

- If x == y, both stones are destroyed, and
- If x != y, the stone of weight x is destroyed, and the stone of 
weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. 
If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then 
that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""
from typing import List
import heapq
import math


def heapmax1(stones: List[int]) -> int:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)

    # Transform to negative values to have a "heapmax"
    # (remember to multiply by -1 again when operating with them)
    heap = []
    # O(n)
    for w in stones:
        # O(logn)
        heapq.heappush(heap, -w)

    # O(n)
    while len(heap) > 1:
        # O(1)
        w1 = heapq.heappop(heap)
        # O(1)
        w2 = heapq.heappop(heap)
        if w1 != w2:
            w1 -= w2
            # O(logn)
            heapq.heappush(heap, w1)

    return -heap[0] if heap else 0


if __name__ == "__main__":
    print("-" * 60)
    print("Last stone weight")
    print("-" * 60)

    test_cases = [
        ([1], 1),
        ([3, 11], 8),
        ([2, 7, 4, 1, 8, 1], 1),
        ([1, 3, 5, 2, 633, 524, 133, 235, 434, 23, 56, 674], 1),
    ]

    for stones, solution in test_cases:

        print("Stones:", stones)

        result = heapmax1([*stones])
        output = f"\heapmax1 = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
