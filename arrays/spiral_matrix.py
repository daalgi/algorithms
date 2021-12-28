"""
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix 
in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List
from copy import deepcopy


def print_matrix(mat):
    print()
    for row in mat:
        print("   " + " ".join(f"{v:>3}" for v in row))
    print()


def moving_boundaries(mat: List[List[int]]) -> List[int]:
    def update_boundary(move_id: int, boundary: List[int]) -> tuple:
        # Update the boundary list upon the current `move_id`
        if move_id == 0:
            # r_start += 1
            boundary[0] += 1
        elif move_id == 1:
            # c_end -= 1
            boundary[3] -= 1
        elif move_id == 2:
            # r_end -= 1
            boundary[1] -= 1
        elif move_id == 3:
            # c_start += 1
            boundary[2] += 1
        return boundary

    def valid_boundary(boundary: List[int]):
        # A boundary list is valid as long as the row and col
        # start and end don't cross:
        return boundary[0] <= boundary[1] and boundary[2] <= boundary[3]

    def point_within_boundary(r: int, c: int, boundary: List[int]):
        # A point is within the boundary when both conditions are met:
        # r_start <= r <= r_end
        # c_start <= c <= c_end
        return boundary[0] <= r <= boundary[1] and boundary[2] <= c <= boundary[3]

    arr = list()
    # Boundary list [r_start, r_end, c_start, c_end]
    boundary = [0, len(mat) - 1, 0, len(mat[0]) - 1]
    # Current pointer moves: (row, col)
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
    # Index of the current move
    move_id = 0
    # row, col of the current cell or pointer
    r, c = 0, 0
    dr, dc = moves[move_id]
    # Loop while the boundary list is valid (start and end don't cross)
    while valid_boundary(boundary):

        while point_within_boundary(r, c, boundary):
            arr.append(mat[r][c])
            r += dr
            c += dc
        # Undo the last row-col update
        r, c = r - dr, c - dc

        # Update `boundary` list and `move_id` for next iteration
        boundary = update_boundary(move_id, boundary)
        move_id = (move_id + 1) % 4
        dr, dc = moves[move_id]
        r, c = r + dr, c + dc

    return arr


def pop_and_rotate(mat: List[List[int]]) -> List[int]:
    arr = []
    # Loop over until the input matrix is empty
    while mat:
        # Pop the first row and store it in the result list `arr`
        arr += mat.pop(0)
        # Rotate the remaining matrix
        mat = (list(zip(*mat)))[::-1]
    return arr


if __name__ == "__main__":
    print("-" * 60)
    print("Spiral matrix")
    print("-" * 60)

    test_cases = [
        ([[1]], [1]),
        (
            [
                [1, 2],
                [4, 3],
            ],
            [1, 2, 3, 4],
        ),
        (
            [
                [1, 2, 3],
                [1, 2, 3],
                [1, 1, 1],
            ],
            [1, 2, 3, 3, 1, 1, 1, 1, 2],
        ),
        (
            [
                [1, 2, 3, 4],
                [12, 1, 2, 5],
                [11, 4, 3, 6],
            ],
            [1, 2, 3, 4, 5, 6, 3, 4, 11, 12, 1, 2],
        ),
        (
            [
                [10, 11],
                [9, 4],
                [8, 3],
                [7, 6],
            ],
            [10, 11, 4, 3, 6, 7, 8, 9],
        ),
    ]

    for matrix, solution in test_cases:

        print("Matrix:")
        print_matrix(matrix)

        result = moving_boundaries(deepcopy(matrix))
        output = f"\t moving_boundaries = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += "\n" + " " * 55
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = pop_and_rotate(deepcopy(matrix))
        output = f"\t    pop_and_rotate = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += "\n" + " " * 55
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
