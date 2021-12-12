"""
CRACKING THE CODING INTERVIEW
8.10 Paint Fill:
Implement the "paint fill" function that one might see on many 
image editing programs. That is, given a screen (represented by 
a 2d array of colors), a point, and a new color, fill in the 
surrounding area until the color changes from the original color.
"""
from typing import List
from copy import deepcopy


def print_screen(screen: List[List[int]], ini_space: int = 3):
    for row in screen:
        s = " " * ini_space
        for c in row:
            s += f" {c} "
        print(s)


def solve(screen: List[List[int]], point: tuple) -> List[List[int]]:
    """
    screen: [[0, 1, 0, 0], [1, 1, 1, 2]] where int represents a color
    point: (row, col, color)
    """
    # Time complexity: O(mn)
    # Space complexity: O(1)

    row, col, color = point
    rows, cols = len(screen), len(screen[0])
    current_color = screen[row][col]
    moves = ((0, 1), (1, 0), (-1, 0), (0, -1))

    def dfs(r: int, c: int):
        # DFS recursive function

        # Base case
        if (
            # row out-of-bounds
            not (0 <= r < rows)
            # col out-of-bounds
            or not (0 <= c < cols)
            # color of current (r, c) not equal to the starting point
            or screen[r][c] != current_color
        ):
            # If the current pixel is out of bounds or the color
            # is not equal to the original point,
            # finish the current path
            return

        screen[r][c] = color
        for dr, dc in moves:
            dfs(r + dr, c + dc)

    dfs(row, col)
    return screen


if __name__ == "__main__":
    print("-" * 60)
    print("Parens")
    print("-" * 60)

    screen = [
        [1, 1, 2, 0, 0],
        [0, 1, 2, 0, 0],
        [0, 1, 1, 2, 0],
        [0, 0, 0, 2, 0],
    ]

    test_cases = [
        # ( screen, (row, col, color) )
        (screen, (0, 3, 8)),
        (screen, (0, 3, 9)),
        (screen, (0, 2, 1)),
        (screen, (0, 0, 0)),
        (screen, (1, 0, 8)),
    ]

    print_screen(screen, ini_space=0)
    print()

    for screen, point in test_cases:

        print(f">>> dfs{point}")
        new_screen = solve(deepcopy(screen), point)
        print_screen(new_screen)
        print()
