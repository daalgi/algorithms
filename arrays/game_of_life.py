"""
https://leetcode.com/problems/game-of-life/

According to Wikipedia's article: "The Game of Life, 
also known simply as Life, is a cellular automaton 
devised by the British mathematician John Horton 
Conway in 1970."

The board is made up of an m x n grid of cells, 
where each cell has an initial state: live (represented 
by a 1) or dead (represented by a 0). Each cell 
interacts with its eight neighbors (horizontal, 
vertical, diagonal) using the following four rules 
(taken from the above Wikipedia article):
- Any live cell with fewer than two live neighbors 
dies as if caused by under-population.
- Any live cell with two or three live neighbors 
lives on to the next generation.
- Any live cell with more than three live neighbors 
dies, as if by over-population.
- Any dead cell with exactly three live neighbors becomes 
a live cell, as if by reproduction.

The next state is created by applying the above rules 
simultaneously to every cell in the current state, where 
births and deaths occur simultaneously. Given the current 
state of the m x n grid board, return the next state.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 
Follow up:
- Could you solve it in-place? Remember that the board 
needs to be updated simultaneously: You cannot update 
some cells first and then use their updated values to 
update other cells.
- In this question, we represent the board using a 2D array. 
In principle, the board is infinite, which would cause 
problems when the active area encroaches upon the border 
of the array (i.e., live cells reach the border). 
How would you address these problems?
"""
from typing import List
from copy import deepcopy
from collections import Counter


def print_board(board: List[List[int]]):
    ini_space = 3
    for row in board:
        print(" " * ini_space + " ".join(str(r) for r in row))


def in_place(board: List[List[int]]) -> List[List[int]]:
    # Time complexity: O(mn)
    # Space complexity: O(m)

    def count_neighbors(r: int, c: int) -> int:
        count = 0
        # Previous row
        if r:
            if c:
                count += prev[c - 1]
            count += prev[c]
            if c + 1 < cols:
                count += prev[c + 1]

        # Current row
        if c:
            count += curr[c - 1]
        if c + 1 < cols:
            count += curr[c + 1]

        # Next row
        if r + 1 < rows:
            if c:
                count += board[r + 1][c - 1]
            count += board[r + 1][c]
            if c + 1 < cols:
                count += board[r + 1][c + 1]

        return count

    def update_cell(r: int, c: int):
        num_neighbors = count_neighbors(r, c)
        if board[r][c]:
            # Live cell
            if num_neighbors < 2 or num_neighbors > 4:
                # Under or over-population
                board[r][c] = 0
            else:
                # Lives
                board[r][c] = 1

        else:
            # Dead cell
            if num_neighbors == 3:
                # Reproduction
                board[r][c] = 1

    rows, cols, prev = len(board), len(board[0]), []
    for r in range(rows):
        curr = board[r][:]
        for c in range(cols):
            update_cell(r, c)
        prev = curr

    return board


def in_place_opt(board: List[List[int]]) -> List[List[int]]:
    # Time complexity: O(mn)
    # Space complexity: O(1)

    # Strategy: use integer values at each cell, and by means
    # of bitwise operations, keep track of the current
    # and new states:
    # current state at bit 0, new state at bit 1.

    def count_neighbors(r: int, c: int) -> int:
        count = 0
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    # Skip the current cell
                    continue

                nr, nc = r + dr, c + dc
                if (
                    # Boundary checks
                    0 <= nr < rows
                    and 0 <= nc < cols
                    # Check if the current cell is live (bit at pos. 0)
                    and get_bit(board[nr][nc], 0)
                ):
                    count += 1

        return count

    def set_bit(x: int, k: int) -> int:
        return x | (1 << k)

    def get_bit(x: int, k: int) -> int:
        return (x >> k) & 1

    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbors(r, c)
            # Check if the current cell will be alive
            # in the new state
            if (
                # if 3 neighbors, it'll be always alive
                neighbors == 3
                # if 2 neighbors and currently alive
                or (neighbors == 2 and get_bit(board[r][c], 0))
            ):
                # Store the new state in bit at pos. 1
                board[r][c] = set_bit(board[r][c], 1)

    # Scan all the cells to get their new state,
    # stored in the bit at pos. 1
    for r in range(rows):
        for c in range(cols):
            board[r][c] = get_bit(board[r][c], 1)

    return board


def infinite_board(board: List[List[int]]) -> List[List[int]]:
    # Time complexity: O(a)
    # Space complexity: O(a)
    # where `a` is the number of cells alive

    # Given an infinite board, we can't construct a `board` list,
    # so we should have an input like a set of cells alive
    rows, cols = len(board), len(board[0])
    alive = set([(i, j) for i in range(rows) for j in range(cols) if board[i][j]])

    # List of relative neighbors (differential dr and dc)
    # (don't exclude (0, 0), as aisolated alive cells need
    # to be updated as well)
    neighbors = [(dr, dc) for dr in range(-1, 2) for dc in range(-1, 2)]

    # Counter of the alive neighbors that each cell has
    # the cell (r, c) influences all the neighboring
    # cells (including itself, take it into account later)
    counter = Counter()
    for r, c in alive:
        for dr, dc in neighbors:
            counter[r + dr, c + dc] += 1

    # Loop over the influenced cells, stored as keys in `counter`
    for r, c in counter:
        # Boundary check
        if 0 <= r < rows and 0 <= c < cols:
            # Check if there's a change in the status of the
            # current cell (r, c)
            if counter[r, c] == 3 and not board[r][c]:
                # Reproduction (currently board[r][c] = 0)
                board[r][c] = 1
            elif counter[r, c] not in [3, 4] and board[r][c]:
                # Under or over-populated
                # (the counter adds the 8 neighbors plus itself, so
                # under-populated is < 3
                # over-populated is > 4)
                board[r][c] = 0

    return board


if __name__ == "__main__":
    print("-" * 60)
    print("Game of life")
    print("-" * 60)

    test_cases = [
        # (board, solution)
        ([[1]], [[0]]),
        (
            [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
            [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
        ),
        ([[1, 1], [1, 0]], [[1, 1], [1, 1]]),
    ]

    for board, solution in test_cases:

        print("Board:")
        print_board(board)
        print("Next state:")
        print_board(solution)

        result = in_place(deepcopy(board))
        output = f"        in_place ---> "
        test_ok = solution == result
        output += " " * (45 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = in_place_opt(deepcopy(board))
        output = f"    in_place_opt ---> "
        test_ok = solution == result
        output += " " * (45 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = infinite_board(deepcopy(board))
        output = f"  infinite_board ---> "
        test_ok = solution == result
        output += " " * (45 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
