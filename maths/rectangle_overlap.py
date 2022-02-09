"""
https://leetcode.com/problems/rectangle-overlap/

An axis-aligned rectangle is represented as a 
list [x1, y1, x2, y2], where (x1, y1) is the 
coordinate of its bottom-left corner, and (x2, y2) 
is the coordinate of its top-right corner. Its top 
and bottom edges are parallel to the X-axis, and 
its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their 
intersection is positive. To be clear, two rectangles 
that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, 
return true if they overlap, otherwise return false.

Example 1:
Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true

Example 2:
Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false

Example 3:
Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false

Constraints:
rect1.length == 4
rect2.length == 4
-10^9 <= rec1[i], rec2[i] <= 10^9
rec1 and rec2 represent a valid rectangle with a 
non-zero area.
"""
from typing import List


def valid_overlap_area(rec1: List[int], rec2: List[int]) -> bool:
    # Time complexity: O(1)
    # Space complexity: O(1)

    # Calculate the coordinates of the overlapping area
    left = max(rec1[0], rec2[0])
    right = min(rec1[2], rec2[2])
    bottom = max(rec1[1], rec2[1])
    top = min(rec1[3], rec2[3])

    # Check if the overlapping area is valid
    # (equivalent to width > 0 and height > 0)
    return left < right and bottom < top


if __name__ == "__main__":
    print("-" * 60)
    print("Rectangle overlap")
    print("-" * 60)

    test_cases = [
        # (rectangle1, rectangle2, solution)
        ([0, 0, 2, 2], [0, 0, 2, 2], True),
        ([0, 0, 2, 2], [1, 1, 3, 3], True),
        ([0, 0, 1, 1], [1, 1, 3, 3], False),
        ([0, 0, 1, 1], [1, 0, 2, 1], False),
        ([0, 0, 1, 1], [2, 2, 3, 3], False),
        ([7, 8, 13, 15], [10, 8, 12, 20], True),
    ]

    for rec1, rec2, solution in test_cases:

        print("Rectangle 1:", rec1)
        print("Rectangle 2:", rec2)

        result = valid_overlap_area(rec1, rec2)
        output = f"   valid_overlap_area = "
        test_ok = solution == result
        output += f"{str(result)}"
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
