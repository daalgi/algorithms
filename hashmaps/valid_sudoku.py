"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled 
cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
from collections import defaultdict


def get_block(i: int, j: int) -> int:
    if i < 3:
        if j < 3:   return 0
        elif j < 6: return 1
        else:       return 2
    elif i < 6:
        if j < 3:   return 3
        elif j < 6: return 4
        else:       return 5
    else:
        if j < 3:   return 6
        elif j < 6: return 7
        else:       return 8
    raise ValueError("Incorrect indices")

class Locations:
    def __init__(self):
        self.rows = {}
        self.cols = {}
        self.blocks = {}

    def add(self, x: int, y: int) -> bool:
        # Check if the new location is not valid
        # Same row
        if x in self.rows: return False
        # Same col
        if y in self.cols: return False
        # Same block
        block = get_block(x, y)
        if block in self.blocks: return False

        # Add valid location
        self.rows[x] = True
        self.cols[y] = True
        self.blocks[block] = True

        return True

def valid_sudoku(board: list) -> bool:
    # Fill a hashtable with the numbers (1, 2, 3, ..., 9)
    # and their locations in the board, 
    # i.e. number 5 in locations (0, 0), (5, 3), (8, 1) 
    # { 
    #   5: Locations({ 
    #       rows:   { 0: True, 5: True, 8: True}
    #       cols:   { 0: True, 3: True, 1: True}
    #       blocks: { 0: True, 5: True, 6: True}
    #       })
    # }
    ht = defaultdict(Locations)
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val != ".":
                is_valid = ht[int(val)].add(x=i, y=j)
                if not is_valid:
                    return False
    return True


if __name__ == "__main__":
    print('-' * 60)
    print('Valid sudoku')
    print('-' * 60)
    
    board0 = [
         ["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
    ]
    board1 = [
         ["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
    ]
    test_cases = [
        (board0, True),
        (board1, False),
    ]
    
    # valid_sudoku(board)
    for board, solution in test_cases:
        
        result = valid_sudoku(board)
        
        string = 'valid_sudoku = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

