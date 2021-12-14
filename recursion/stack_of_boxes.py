"""
CRACKING THE CODING INTERVIEW
8.13 Stack of Boxes:
You have a stack of n boxes, width widths wi, heights hi,
and depths di. The boxes cannot be rotated and can only be 
stacked on top of one another if each box in the stack is
strictly larger than the box above it in width, height, and depth.
Implement a method to compute the height of the tallest
possible stack. The height of a stack is the sum of the 
heights of each box.

"""
from typing import List
from dataclasses import dataclass


@dataclass
class Box:
    width: int
    height: int
    depth: int

    def __gt__(self, other) -> bool:
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (
            self.width > other.width
            and self.height > other.height
            and self.depth > other.depth
        )


def backtrack(widths: List[int], heights: List[int], depths: List[int]) -> int:
    # Time complexity: O()
    # Space complexity: O(n)
    n = len(heights)
    max_height = 0

    # Create a list of box objects and sort it in reverse order:
    # if we sort the boxes (larger first), we don't have to
    # look backwards in the list
    boxes = [Box(w, h, d) for w, h, d in zip(widths, heights, depths)]
    boxes = sorted(boxes, reverse=True)

    def dfs(current_height: int, index: int, last_box: Box = None):
        nonlocal max_height
        # print('>Start of dfs:', last_box, index, n)
        # Base case: no elements left
        if index == n:
            # print('Index -->', index, last_box, current_height)
            if current_height > max_height:
                max_height = current_height
            return

        box = boxes[index]
        if last_box is None or last_box > box:
            # If it's the first box, or the last box was larger
            # Explore considering the current box
            dfs(current_height + box.height, index + 1, box)

        # Explore not considering the current box
        # (pass `last_box` to the recursive function)
        dfs(current_height, index + 1, last_box)

    dfs(0, 0)
    return max_height


if __name__ == "__main__":
    print("-" * 60)
    print("Stack of boxes")
    print("-" * 60)

    test_cases = [
        # ( widths, heights, depths, solution)
        ([1], [2], [1], 2),
        ([1, 3], [2, 1], [1, 1], 2),
        ([1, 3], [2, 5], [1, 2], 7),
        ([1, 2, 3], [2, 4, 5], [1, 2, 3], 11),
        ([1, 3, 2], [2, 4, 5], [1, 2, 3], 7),
        ([2, 2, 20], [2, 4, 3], [3, 5, 80], 4),
    ]

    for widths, heights, depths, solution in test_cases:

        # boxes = [Box(w, h, d) for w, h, d in zip(widths, heights, depths)]
        # boxes = sorted(boxes, reverse=True)
        # print(boxes)

        print("Widths:", widths)
        print("Heights:", heights)
        print("Depths:", depths)
        result = backtrack(widths, heights, depths)
        string = f">>> backtrack = {result}"
        print(string)

        test_ok = solution == result
        print(" " * 60, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')
