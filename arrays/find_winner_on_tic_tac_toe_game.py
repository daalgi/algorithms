"""
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

Tic-tac-toe is played by two players A and B on a 3 x 3 grid. 
The rules of Tic-Tac-Toe are:
- Players take turns placing characters into empty 
squares ' '.
- The first player A always places 'X' characters, 
while the second player B always places 'O' characters.
- 'X' and 'O' characters are always placed into empty 
squares, never on filled ones.
- The game ends when there are three of the same (non-empty) 
character filling any row, column, or diagonal.
- The game also ends if all squares are non-empty.
- No more moves can be played if the game is over.

Given a 2D integer array moves where moves[i] = [rowi, coli] 
indicates that the ith move will be played on grid[rowi][coli]. 
return the winner of the game if it exists (A or B). In case 
the game ends in a draw return "Draw". If there are still 
movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules 
of Tic-Tac-Toe), the grid is initially empty, and A will 
play first.

Example 1:
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.

Example 2:
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.

Example 3:
Input: moves = [
    [0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there 
are no moves to make.

Constraints:
1 <= moves.length <= 9
moves[i].length == 2
0 <= rowi, coli <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
"""
from typing import List


def efficient(moves: List[List[int]]) -> str:
    # Time complexity: O(n²)
    # Space complexity: O(n)

    # Grid size set to `3` by default
    n = 3
    # Keep track of the sums at each row and col
    # instead of creating an n * n grid.
    # Player A adds 1; Player B adds -1
    rows, cols = [0] * n, [0] * n
    # Keep also the sums at the diagonals
    diagonal = antidiagonal = 0

    # Loop over the moves
    num_moves = len(moves)
    for i in range(num_moves):
        # Player A (+1) when `i` is even
        # Player B (-1) when `i` is odd
        sign = -1 if i & 1 else 1

        # Update rows, cols and diagonals for the
        # current move `i`
        r, c = moves[i]
        rows[r] += sign
        cols[c] += sign
        if r == c:
            diagonal += sign
        if r + c == n - 1:
            antidiagonal += sign

        # Check if any player has won, in O(1) time
        if (
            abs(rows[r]) == n
            or abs(cols[c]) == n
            or abs(diagonal) == n
            or abs(antidiagonal) == n
        ):
            return "A" if sign == 1 else "B"

    # If all the cells have been filled, it's a draw
    if num_moves == n * n:
        return "Draw"
    # If there're still cells to be filled
    return "Pending"


if __name__ == "__main__":
    print("-" * 60)
    print("Find winner on a Tic-Tac-Toe game")
    print("-" * 60)

    test_cases = [
        # (moves, solution)
        ([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]], "A"),
        ([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]], "B"),
        (
            [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]],
            "Draw",
        ),
        ([[0, 0], [1, 1]], "Pending"),
    ]

    for moves, solution in test_cases:

        print("Moves:", moves)

        result = efficient(moves)
        output = "    efficient = "
        print_result = str(result)
        output += print_result
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
