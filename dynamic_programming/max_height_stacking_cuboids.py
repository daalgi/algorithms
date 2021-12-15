"""
https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

Given n cuboids where the dimensions of the ith cuboid is 
cuboids[i] = [widthi, lengthi, heighti] (0-indexed). 
Choose a subset of cuboids and place them on each other.

You can place cuboid i on cuboid j if widthi <= widthj and 
lengthi <= lengthj and heighti <= heightj. 
You can rearrange any cuboid's dimensions by rotating it to 
put it on another cuboid.

Return the maximum height of the stacked cuboids.

Example 1:
Input: cuboids = [[50,45,20],[95,37,53],[45,23,12]]
Output: 190
Explanation:
Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95.
Cuboid 0 is placed next with the 45x20 side facing down with height 50.
Cuboid 2 is placed next with the 23x12 side facing down with height 45.
The total height is 95 + 50 + 45 = 190.

Example 2:
Input: cuboids = [[38,25,45],[76,35,3]]
Output: 76
Explanation:
You can't place any of the cuboids on the other.
We choose cuboid 1 and rotate it so that the 35x3 side is facing 
down and its height is 76.

Example 3:
Input: cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
Output: 102
Explanation:
After rearranging the cuboids, you can see that all cuboids 
have the same dimension.
You can place the 11x7 side down on all cuboids so their heights are 17.
The maximum height of stacked cuboids is 6 * 17 = 102.
 
Constraints:
n == cuboids.length
1 <= n <= 100
1 <= widthi, lengthi, heighti <= 100
"""
from typing import List


def dp_iter(boxes: List[List[int]]) -> int:
    # Dynamic programming - Tabulation
    # Similar to "longest increasing subset".
    # Time complexity: O(n²)
    # Space complexity: O(n)

    n = len(boxes)

    # Create a list of box objects and sort it in reverse order:
    # if we sort the boxes (larger first), we don't have to
    # look backwards in the list.
    # Also, we can rotate the boxes to maximize the height,
    # so we sort the list of dimensions as well, so we have
    # the largest dimension in last position (height)
    boxes = sorted([sorted(b) for b in boxes], reverse=True)

    # Table to store the cumulative max height
    dp = [b[2] for b in boxes]

    for right in range(1, n):
        for left in range(right):
            if all(l >= r for l, r in zip(boxes[left], boxes[right])):
                dp[right] = max(dp[right], dp[left] + boxes[right][2])

    return max(dp)


if __name__ == "__main__":
    print("-" * 60)
    print("Maximum height by stacking cuboids")
    print("-" * 60)

    test_cases = [
        # ( [box1, box2, ...], solution)
        # where box = [width, height, depth]
        ([[1, 2, 1]], 2),
        ([[1, 2, 1], [2, 1, 2], [3, 3, 3]], 7),
        ([[2, 3, 2], [1, 2, 1], [5, 4, 5]], 10),
        ([[1, 2, 3], [2, 4, 5], [1, 2, 3]], 11),
        ([[2, 2, 20], [2, 4, 3], [3, 5, 80]], 100),
        ([[50, 45, 20], [95, 37, 53], [45, 23, 12]], 190),
        ([[38, 25, 45], [76, 35, 3]], 76),
        (
            [
                [7, 11, 17],
                [7, 17, 11],
                [11, 7, 17],
                [11, 17, 7],
                [17, 7, 11],
                [17, 11, 7],
            ],
            102,
        ),
        ([[1, 2, 3]], 3),
    ]

    for boxes, solution in test_cases:

        print("Boxes:")
        for b in boxes:
            print(b)

        result = dp_iter(boxes)
        string = f">>>   dp_iter = {result}"
        test_ok = solution == result
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')

        print()
