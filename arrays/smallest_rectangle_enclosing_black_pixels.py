"""
https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

You are given an m x n binary matrix image where 0 
represents a white pixel and 1 represents a black pixel.

The black pixels are connected (i.e., there is only 
one black region). Pixels are connected horizontally 
and vertically.

Given two integers x and y that represents the 
location of one of the black pixels, return the 
area of the smallest (axis-aligned) rectangle that 
encloses all black pixels.

You must write an algorithm with less than O(mn) 
runtime complexity

Example 1:
Input: image = [
    ["0","0","1","0"],
    ["0","1","1","0"],
    ["0","1","0","0"]
], x = 0, y = 2
Output: 6

Example 2:
Input: image = [["1"]], x = 0, y = 0
Output: 1

Constraints:
m == image.length
n == image[i].length
1 <= m, n <= 100
image[i][j] is either '0' or '1'.
1 <= x < m
1 <= y < n
image[x][y] == '1'.
The black pixels in the image only form one component.
"""
from typing import List
from copy import deepcopy
from collections import deque


def print_image(grid: List[List[int]]):
    for row in grid:
        print(" " * 4 + " ".join(str(v) for v in row))


def linear_search(image: List[List[int]], row: int, col: int) -> int:
    # Time complexity: O(mn)
    # Space complexity: O(1)

    rows, cols = len(image), len(image[0])

    min_r = max_r = row
    min_c = max_c = col

    for r in range(rows):
        for c in range(cols):
            if image[r][c]:
                # Update rectangle limits
                if r < min_r:
                    min_r = r
                if r > max_r:
                    max_r = r
                if c < min_c:
                    min_c = c
                if c > max_c:
                    max_c = c

    return (max_r - min_r + 1) * (max_c - min_c + 1)


def bfs_linear_search(image: List[List[int]], row: int, col: int) -> int:
    # Time complexity: O(k)
    # Space complexity: O(k)
    # where `k` is the number of 1s, but in the worst case,
    # when the number of 1s is closee to m*n, the time complexity
    # is asymptotically the same as the naive approach, and
    # the space complexity is much bigger.

    rows, cols = len(image), len(image[0])

    # Variables to keep track of the rectangle size
    min_r = max_r = x
    min_c = max_c = y

    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))

    # Mark the pixel as seen
    image[row][col] = 0

    # BFS
    q = deque([(x, y)])
    while q:
        r, c = q.popleft()

        # Explore the neighbors
        for dr, dc in moves:
            nr, nc = r + dr, c + dc

            if (
                not 0 <= nr < rows 
                or not 0 <= nc < cols 
                or not image[nr][nc]
            ):
                continue

            # Mark the pixel as seen
            image[nr][nc] = 0

            # Update rectangle limits
            if nr < min_r:
                min_r = nr
            if nr > max_r:
                max_r = nr
            if nc < min_c:
                min_c = nc
            if nc > max_c:
                max_c = nc

            # Add the current neighbor to the queue for
            # further exploration
            q.append((nr, nc))

    return (max_r - min_r + 1) * (max_c - min_c + 1)


def binary_search(image: List[List[int]], row: int, col: int) -> int:
    # Time complexity: O(nlogm + mlogn)
    # Space complexity: O(1)

    def has_black_pixel(ref: int, is_column: bool) -> bool:
        # Determines whether a row or column has a black pixel
        if is_column:
            # Check the column `ref`
            return any(image[r][ref] for r in range(rows))

        # Check the row `ref`
        return any(image[ref][c] for c in range(cols))

    def search_min(low: int, high: int, is_column: bool) -> int:
        # Binary search
        while low < high:
            mid = (low + high) // 2
            if has_black_pixel(mid, is_column):
                # If the row/column `mid` has a 1,
                # update the `high` pointer
                high = mid
            else:
                low = mid + 1
        return high

    def search_max(low: int, high: int, is_column: bool) -> int:
        # Binary search
        while low < high:
            # Force the `mid` element to tend to the right
            mid = (low + high + 1) // 2

            if has_black_pixel(mid, is_column):
                # If the row/column `mid` has a 1,
                # move the `low` pointer
                low = mid
            else:
                high = mid - 1
        return high

    rows, cols = len(image), len(image[0])
    left = search_min(0, col, is_column=True)
    right = search_max(col, cols - 1, is_column=True)
    top = search_min(0, row, is_column=False)
    bottom = search_max(row, rows - 1, is_column=False)
    return (bottom - top + 1) * (right - left + 1)


if __name__ == "__main__":
    print("-" * 60)
    print("Smallest rectangle enclosing black pixels")
    print("-" * 60)

    test_cases = [
        # (image, x, y, solution)
        ([[1]], 0, 0, 1),
        ([[1, 0], [1, 0]], 1, 0, 2),
        ([[1, 0], [1, 1]], 1, 0, 4),
        ([[0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 0]], 0, 2, 6),
        ([
            [0, 0, 1, 1, 0, 1, 0], 
            [0, 1, 1, 1, 1, 1, 0], 
            [0, 1, 0, 0, 0, 0, 0]
        ], 0, 2, 15),
    ]

    for image, x, y, solution in test_cases:

        print("Image:")
        print_image(image)
        print(f"One black point: {x, y}")

        result = linear_search(deepcopy(image), x, y)
        output = f"         linear_search = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = bfs_linear_search(deepcopy(image), x, y)
        output = f"     bfs_linear_search = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = binary_search(deepcopy(image), x, y)
        output = f"         binary_search = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
