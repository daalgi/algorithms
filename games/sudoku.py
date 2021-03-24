from random import shuffle, randint, choice
from copy import deepcopy
import os


def random_int_within_block(i: int):
    """
    Returns a random int within the interval to which the
    block to which `i` belongs, excluding `i` itself.
    Only valid for 9x9 grids
    """
    arr = []
    if i in [0, 1, 2]:
        arr = [0, 1, 2]
    elif i in [3, 4, 5]:
        arr = [3, 4, 5]
    else:
        arr = [6, 7, 8]
    return choice([x for x in arr if x != i])

def empty_board(size: int):
    r = range(size)
    arr = [[0 for _ in r] for _ in r]
    return arr

def generate_by_shifting(size: int = 9):
    row = list(range(1, size + 1))
    shuffle(row)
    arr = [row]
    for i in range(1, size):
        gap = 1 if i % 3 == 0 else 3
        arr.append(arr[-1][-gap:] + arr[-1][:-gap])
    return arr

def swap_rows(arr: list, i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

def swap_columns(arr: list, i: int, j: int):
    for row in range(len(arr)):
        arr[row][i], arr[row][j] = arr[row][j], arr[row][i]
    return arr

def rotate(arr: list):
    n = len(arr)
    copy = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            copy[j][n-1-i] = arr[i][j]
    return copy

def vertical_mirroring(arr: list):
    n = len(arr)
    return [arr[n-1-i] for i in range(n)]

def horizontal_mirroring(arr: list):
    return [row[::-1] for row in arr]

def print_matrix(arr: list):
    print()
    for row in arr:
        out = ''
        for val in row:
            out += f'  {val if val else "."}  '
        print(out + '\n')

class Board:

    def __init__(self, array: list = None):
        self.size = len(array) if array else 9
        self.num_cells = self.size * self.size if array else 81
        self.array = deepcopy(array)
        self.solution = []
        
    def get_row(self, index: int):
        return self.array[index]

    def get_column(self, index: int):
        return [self.array[row][index] for row in range(self.size)]

    def get_block(self, row: int, col: int):
        """
        Keyword arguments:
        row -- row of the cell within the block
        col -- column of the cell within the block
        returns a list of the values of the block
        """
        block = []
        row_start, col_start = None, None
        if row < 3:     row_start = 0
        elif row < 6:   row_start = 3
        else:           row_start = 6

        if col < 3:     col_start = 0
        elif col < 6:   col_start = 3
        else:           col_start = 6

        for row in range(row_start, row_start+3):
            for col in range(col_start, col_start+3):
                block.append(self.array[row][col])
        return block

    def get_cell(self, row: int, col: int):
        return self.array[row][col]

    def is_valid_row(self, row: int):
        return len(set(self.get_row(row))) == self.size

    def is_valid_column(self, col: int):
        return len(set(self.get_column(col))) == self.size

    def is_valid_block(self, row: int, col: int):
        return len(set(self.get_block(row, col))) == self.size

    def is_valid(self):
        for i in range(self.size):
            if not self.is_valid_row(i):
                return False
            if not self.is_valid_column(i):
                return False
            if (i+2) % 3 == 0 and not self.is_valid_block(i, i):
                return False
        return True

    def is_original_solution(self):
        r = range(self.size)
        for i in r:
            for j in r:
                if self.array[i][j] != self.solution[i][j]:
                    return False
        return True

    def row_missing_values(self, row: int):
        return [x for x in range(1, self.size+1) if x not in self.get_row(row)]
    
    def column_missing_values(self, col: int):
        return [x for x in range(1, self.size+1) if x not in self.get_column(col)]

    def block_missing_values(self, row: int, col: int):
        return [x for x in range(1, self.size+1) if x not in self.get_block(row, col)]

    def cell_possible_values(self, row: int, col: int):
        r = self.row_missing_values(row)
        c = self.column_missing_values(col)
        b = self.block_missing_values(row, col)
        return list(set.intersection(set(r), set(c), set(b)))

    def swap_rows(self, i: int, j: int):
        swap_rows(self.array, i, j)
        swap_rows(self.solution, i, j)
        return self

    def swap_columns(self, i: int, j: int):
        swap_columns(self.array, i, j)
        swap_columns(self.solution, i, j)
        return self

    def shuffle_rows(self, num: int):
        while num > 0:
            i = randint(0, self.size-1)
            self.swap_rows(i, random_int_within_block(i))
            num -= 1
        return self

    def shuffle_columns(self, num: int):
        while num > 0:
            i = randint(0, self.size-1)
            self.swap_columns(i, random_int_within_block(i))
            num -= 1
        return self

    def shuffle(self, num: int = 7):
        while num > 0:
            i = randint(0, self.size-1)
            if randint(0, 1):
                self.swap_rows(i, random_int_within_block(i))
            else:
                self.swap_columns(i, random_int_within_block(i))
            num -= 1
        return self

    def rotate(self):
        self.array = rotate(self.array)
        self.solution = rotate(self.solution)
        return self

    def vertical_mirroring(self):
        self.array = vertical_mirroring(self.array)
        self.solution = vertical_mirroring(self.solution)
        return self

    def horizontal_mirroring(self):
        self.array = horizontal_mirroring(self.array)
        self.solution = horizontal_mirroring(self.solution)
        return self

    def cipher(self):
        c = list(range(1, self.size+1))
        shuffle(c)
        r = range(self.size)
        for i in r:
            for j in r:
                self.array[i][j] = c[self.array[i][j]-1]
        return self

    def generate(self, non_empty_cells: int = 81):
        arr = generate_by_shifting()
        self.solution = deepcopy(arr)
        self.array = arr
        return self.empty_random_cells(num=self.num_cells-non_empty_cells)
    
    def empty_board(self):
        self.array = empty_board(size=self.size)
        return self

    def empty_random_cells(self, num: int):
        while num > 0:
            row, col = randint(0, self.size-1), randint(0, self.size-1)
            if self.array[row][col] > 0:
                self.array[row][col] = 0
                num -= 1
        return self

    def empty_random_pairs(self, pairs: int):
        while pairs > 0:
            row, col = randint(0, self.size-1), randint(0, self.size-1)
            if self.array[row][col] > 0:
                self.array[row][col] = 0
                self.array[self.size-1-row][self.size-1-col] = 0
                pairs -= 1
        return self

    def find_next_empty_cell(self):
        r = range(self.size)
        for i in r:
            for j in r:
                if self.array[i][j] == 0:
                    return i, j
        return None

    def find_next_naked_single(self):
        """
        Returns the (row, column) of the first empty cell with a naked single,
        that is, there's only one value that can go into the cell.
        """
        r = range(self.size)
        for i in r:
            for j in r:
                if self.array[i][j] == 0:
                    values = self.cell_possible_values(i, j)
                    if len(values) == 1:
                        return i, j, values[0]
        return None

    def solve(self):
        # Find the next empty cell with a naked single value
        # --> May be bot valid if previous iterations didn't have naked single values
        # nsingle = self.find_next_naked_single()
        # if nsingle:
        #     row, col, value = nsingle
        #     self.array[row][col] = value
        #     print(f'---> Naked single: \t{row, col} = {value}')
        #     if self.solve():
        #         return True
            
        # Find the next empty cell (with multiple possible valid values)
        loc = self.find_next_empty_cell()
        if not loc:
            return True        
        row, col = loc
        
        # Loop through the cell possible values
        valid_values = self.cell_possible_values(row, col)
        for val in valid_values:

            # Try to solve with the first valid value
            self.array[row][col] = val
            # print(f'---> Brute force:  \t{row, col} = {self.array[row][col]}')
            if self.solve():
                return True

            # If it didn't reach a solution, undo
            self.array[row][col] = 0


        return False

    def print_board(self):
        print_matrix(self.array)

    def print_solution(self):
        print_matrix(self.solution)


def read_sudokus(file: str):
    """
    Parameters
    ----------
    file: str
        name of the txt file containing sudokus (including path).
        It may contain multiple sudoku grids, separated by an empty line.
        Example of one sudoku:
            308062015
            400000060
            060070008
            802400107
            000008300
            000053280
            000500670
            200000000
            010020540
    
    Returns
    -------
    list
        list of Board instances, each one containing a sudoku grid
    """
    if not os.path.isfile(file):
        raise ValueError(f"File {file} doesn't exist.")

    sudokus = []
    grid = []
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            grid.append([int(c) for c in line if c.isnumeric()])
            line = f.readline()
            if len(line.split()) == 0:
                sudokus.append(Board(grid))
                grid = []
                line = f.readline()

    return sudokus

if __name__ == '__main__':
    b = Board([
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [9, 1, 2, 3, 4, 5, 6, 7, 8],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
    ])
    c = Board([
        [0, 2, 3, 4, 5, 6, 7, 0, 9],
        [0, 0, 9, 1, 2, 3, 4, 5, 6],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [9, 1, 2, 3, 4, 5, 6, 7, 8],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
    ])
    # d = Board()
    # c.print_board()
    # print(c.generate().is_valid())
    # print(c.size)
    # print()
    # print(c.cell_possible_values(0, 0))
    # print(c.cell_possible_values(1, 0))
    # print(c.empty_board().array)
    # print(c.cell_possible_values(0, 0))
    # d.generate(non_empty_cells=81)
    # d.print_solution()
    # d.print_board()
    # d.swap_rows(1, 2).print_board()
    # d.swap_columns(0, 2).print_board()
    # d.shuffle(5)
    # d.cipher()
    # d.rotate()
    # d.vertical_mirroring()
    # d.horizontal_mirroring()
    # d.empty_random_pairs(pairs=30)
    # d.print_board()
    # # next = d.find_next_empty_cell()
    # # print(f'{next}: {d.cell_possible_values(*next)}')
    # c.solve()
    # c.print_board()
    # print(d.is_valid())
    # # print(d.is_original_solution())

    # Read a sudoku from a txt file and solve it
    s = read_sudokus('.\\games\\sudokus-medium.txt')[1]
    s.solve()
    s.print_board()