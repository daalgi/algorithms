"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

There are several cards arranged in a row, and each 
card has an associated number of points. The points 
are given in the integer array cardPoints.

In one step, you can take one card from the beginning 
or from the end of the row. You have to take 
exactly k cards.

Your score is the sum of the points of the cards 
you have taken.

Given the integer array cardPoints and the integer k, 
return the maximum score you can obtain.

Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. 
However, choosing the rightmost card first will maximize your 
total score. The optimal strategy is to take the three cards 
on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your 
score will always be 4.

Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is 
the sum of points of all cards.

Constraints:
1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length
"""
from typing import List


def sliding_window(cards: List[int], k: int) -> int:
    # Time complexity: O(k)
    # Space complexity: O(1)

    # First possible score:
    # `k` elements from the left of the list
    score = sum(cards[:k])

    # Pointer to the right side of the list
    right = len(cards) - 1

    # Remove iteratively `k` indices from the
    # left and add them from the right
    # (sliding window)
    max_score = score
    for i in range(k - 1, -1, -1):
        score += cards[right] - cards[i]
        if score > max_score:
            max_score = score
        right -= 1

    return max_score


def sliding_window2(cards: List[int], k: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    max_points = curr_points = sum(cards[:k])
    for i in range(1, k + 1):
        curr_points += cards[-i] - cards[k - i]
        if curr_points > max_points:
            max_points = curr_points

    return max_points


if __name__ == "__main__":
    print("-" * 60)
    print("Maximum points you can obtain from cards")
    print("-" * 60)

    test_cases = [
        # (cards, k, solution)
        ([1], 1, 1),
        ([1, 2], 1, 2),
        ([1, 2, 3], 2, 5),
        ([1, 2, 8, 3, 3, 3], 3, 11),
        ([1, 2, 1, 3, 3, 3], 3, 9),
    ]

    for cards, k, solution in test_cases:

        print("Cards:", cards)
        print("k:", k)

        result = sliding_window(cards, k)
        output = f"     sliding_window = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sliding_window2(cards, k)
        output = f"    sliding_window2 = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
