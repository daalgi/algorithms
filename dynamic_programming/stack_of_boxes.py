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


def backtrack(boxes: List[List[int]]) -> int:
    # Time complexity: O(2^n)
    # Space complexity: O(n)
    n = len(boxes)
    max_height = 0

    # Create a list of box objects and sort it in reverse order:
    # if we sort the boxes (larger first), we don't have to
    # look backwards in the list
    boxes = sorted([Box(*b) for b in boxes], reverse=True)

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


def dp_iter(boxes: List[List[int]]) -> int:
    # Dynamic programming - Tabulation
    # Similar to "longest increasing subset".
    # Time complexity: O(n²)
    # Space complexity: O(n)

    n = len(boxes)

    # Create a list of box objects and sort it in reverse order:
    # if we sort the boxes (larger first), we don't have to
    # look backwards in the list
    boxes = sorted([Box(*b) for b in boxes], reverse=True)

    # Table to store the partial results of maximum stack height
    dp = [b.height for b in boxes]

    for i in range(1, n):
        for j in range(i):
            if boxes[j] > boxes[i] and dp[i] < dp[j] + boxes[i].height:
                dp[i] = dp[j] + boxes[i].height

    return max(dp)


if __name__ == "__main__":
    print("-" * 60)
    print("Stack of boxes")
    print("-" * 60)

    test_cases = [
        # ( [box1, box2, ...], solution)
        # where box = [width, height, depth]
        ([[1, 2, 1]], 2),
        ([[1, 2, 1], [2, 1, 2], [3, 3, 3]], 5),
        ([[2, 3, 2], [1, 2, 1], [5, 4, 5]], 9),
        ([[1, 2, 3], [2, 4, 5], [1, 2, 3]], 6),
        ([[2, 2, 20], [2, 4, 3], [3, 5, 80]], 9),
    ]

    for boxes, solution in test_cases:

        print("Boxes:")
        for b in boxes:
            print(b)

        result = backtrack(boxes)
        string = f">>> backtrack = {result}"
        test_ok = solution == result
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')

        result = dp_iter(boxes)
        string = f">>>   dp_iter = {result}"
        test_ok = solution == result
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')

        print()
