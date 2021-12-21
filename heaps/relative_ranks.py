"""
https://leetcode.com/problems/relative-ranks/

You are given an integer array score of size n, where score[i] is 
the score of the ith athlete in a competition. All the scores are 
guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place 
athlete has the highest score, the 2nd place athlete has the 2nd 
highest score, and so on. The placement of each athlete 
determines their rank:

- The 1st place athlete's rank is "Gold Medal".
- The 2nd place athlete's rank is "Silver Medal".
- The 3rd place athlete's rank is "Bronze Medal".
- For the 4th place to the nth place athlete, their rank is their 
placement number (i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of 
the ith athlete.

Example 1:
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Example 2:
Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

Constraints:
n == score.length
1 <= n <= 104
0 <= score[i] <= 10^6
All the values in score are unique.
"""
from typing import List
import heapq


def heap(scores: List[int]) -> List[str]:
    # Time complexity: O()
    # Space complexity: O()

    # Create a min-heap with the sign of the values changed
    # (effectively a max-heap)
    # O(nlogn)
    heap = []
    for i, score in enumerate(scores):
        heapq.heappush(heap, (-score, i))

    # Rank the `scores`
    # O(nlogn)
    place = 1
    while heap:
        score, i = heapq.heappop(heap)
        if place == 1:
            scores[i] = "Gold Medal"
        elif place == 2:
            scores[i] = "Silver Medal"
        elif place == 3:
            scores[i] = "Bronze Medal"
        else:
            scores[i] = str(place)
        place += 1

    return scores


if __name__ == "__main__":
    print("-" * 60)
    print("Relative ranks")
    print("-" * 60)

    test_cases = (
        ([1], ["Gold Medal"]),
        ([5, 4, 3, 2, 1], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]),
        ([10, 3, 8, 9, 4], ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]),
        (
            [1, 2, 3, 4, 34, 75, 5, 757, 13, 25],
            [
                "10",
                "9",
                "8",
                "7",
                "Bronze Medal",
                "Silver Medal",
                "6",
                "Gold Medal",
                "5",
                "4",
            ],
        ),
    )

    for nums, solution in test_cases:

        output = f"Scores: {nums}"
        if len(output) > 30:
            output = output[:60] + "...]"
        print(output)

        result = heap([*nums])
        output = f"\t heap = "
        output += " " * (15 - len(output))
        output += str(result)
        print(output)
        test_ok = solution == result
        output = " " * 60
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
