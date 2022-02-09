"""
https://leetcode.com/problems/rectangle-area/

Given the coordinates of two rectilinear rectangles 
in a 2D plane, return the total area covered 
by the two rectangles.

The first rectangle is defined by its bottom-left 
corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left 
corner (bx1, by1) and its top-right corner (bx2, by2).

Example 1:
Rectangle Area
Input: 
ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, 
bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45

Example 2:
Input: 
ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, 
bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16

Constraints:
-10^4 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 10^4
"""


def overlap_area(
    ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int
) -> int:
    # Time complexity: O(1)
    # Space complexity: O(1)

    # Calculate the area of both rectangles independently,
    # and if there's overlap, subtract it
    rec1 = (ax2 - ax1) * (ay2 - ay1)
    rec2 = (bx2 - bx1) * (by2 - by1)
    overlap_width = min(bx2, ax2) - max(bx1, ax1)
    overlap_height = min(by2, ay2) - max(by1, ay1)
    overlap = (
        overlap_width * overlap_height
        if overlap_width > 0 and overlap_height > 0
        else 0
    )
    return rec1 + rec2 - overlap


if __name__ == "__main__":
    print("-" * 60)
    print("Rectangle area")
    print("-" * 60)

    test_cases = [
        # (rectangle1, rectangle2, solution)
        ([0, 0, 2, 2], [0, 0, 2, 2], 4),
        ([0, 0, 2, 2], [1, 1, 3, 3], 7),
        ([0, 0, 1, 1], [1, 1, 3, 3], 5),
        ([0, 0, 1, 1], [1, 0, 2, 1], 2),
        ([0, 0, 1, 1], [2, 2, 3, 3], 2),
        ([7, 8, 13, 15], [10, 8, 12, 20], 52),
        ([-3, 0, 3, 4], [0, -1, 9, 2], 45),
        ([-2, -2, 2, 2], [-2, -2, 2, 2], 16),
    ]

    for rec1, rec2, solution in test_cases:

        print("Rectangle 1:", rec1)
        print("Rectangle 2:", rec2)

        result = overlap_area(*rec1, *rec2)
        output = f"   overlap_area = "
        test_ok = solution == result
        output += f"{str(result)}"
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
