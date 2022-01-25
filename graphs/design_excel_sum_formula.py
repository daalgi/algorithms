"""
https://leetcode.com/problems/design-excel-sum-formula/

Design the basic function of Excel and implement 
the function of the sum formula.

Implement the Excel class:
- Excel(int height, char width) Initializes the object 
with the height and the width of the sheet. The sheet 
is an integer matrix mat of size height x width with 
the row index in the range [1, height] and the column 
index in the range ['A', width]. All the values should 
be zero initially.
- void set(int row, char column, int val) Changes the 
value at mat[row][column] to be val.
- int get(int row, char column) Returns the value 
at mat[row][column].
- int sum(int row, char column, List<String> numbers) Sets 
the value at mat[row][column] to be the sum of cells 
represented by numbers and returns the value at mat[row][column]. 
This sum formula should exist until this cell is overlapped by 
another value or another sum formula. numbers[i] could be on 
the format:
    - "ColRow" that represents a single cell.
    For example, "F7" represents the cell mat[7]['F'].
    - "ColRow1:ColRow2" that represents a range of cells. 
    The range will always be a rectangle where "ColRow1" 
    represent the position of the top-left cell, and "ColRow2" 
    represents the position of the bottom-right cell.
    For example, "B3:F7" represents the cells mat[i][j] 
    for 3 <= i <= 7 and 'B' <= j <= 'F'.

Note: You could assume that there will not be any circular sum reference.
- For example, mat[1]['A'] == sum(1, "B") and mat[1]['B'] == sum(1, "A").
 
Example 1:
Input
["Excel", "set", "sum", "set", "get"]
[[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]
Output
[null, null, 4, null, 6]

Explanation
Excel excel = new Excel(3, "C");
 // construct a 3*3 2D array with all zero.
 //   A B C
 // 1 0 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.set(1, "A", 2);
 // set mat[1]["A"] to be 2.
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.sum(3, "C", ["A1", "A1:B2"]); // return 4
 // set mat[3]["C"] to be the sum of value at mat[1]["A"] 
 and the values sum of the rectangle range whose top-left 
 cell is mat[1]["A"] and bottom-right cell is mat[2]["B"].
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 4
excel.set(2, "B", 2);
 // set mat[2]["B"] to be 2. Note mat[3]["C"] should also be changed.
 //   A B C
 // 1 2 0 0
 // 2 0 2 0
 // 3 0 0 6
excel.get(3, "C"); // return 6
 

Constraints:

1 <= height <= 26
'A' <= width <= 'Z'
1 <= row <= height
'A' <= column <= width
-100 <= val <= 100
1 <= numbers.length <= 5
numbers[i] has the format "ColRow" or "ColRow1:ColRow2".
At most 100 calls will be made to set, get, and sum.
"""
from typing import List
from collections import defaultdict, deque


class Excel:
    def __init__(self, height: int, width: str) -> None:
        # Time complexity: O(r * c)
        # Space complexity: O((r * c)²)
        # r * c cells, and each cell might be dependent
        # on the rest of cells (r * c).

        self.rows = height
        self.cols = self._get_col_index(width) + 1

        # Values in each cell (both stored values and
        # the results of formulas)
        self.values = [[0] * self.cols for _ in range(self.rows)]

        # Formulas dict (only for sums),
        # i.e. { (2, 2): ["A1:B2", "C1"] }
        self.formulas = {}

        # Adjacency list, i.e.
        # { (0, 0): [(0, 2), (2, 2)]}
        # self.adj = defaultdict(list)

        # Indegree (how many edges reaching the cell indices (r, c))
        # i.e. { (2, 2): 2 }
        # self.indegree = defaultdict(int)

    def set(self, row: int, column: str, val: int) -> None:
        # Time complexity: O((r * c)²)
        r, c = row - 1, self._get_col_index(column)
        self.values[r][c] = val
        self._remove_formula(r, c)
        self._calc_spreadsheet()

    def get(self, row: int, column: str) -> int:
        # Time complexity: O(1)
        return self.values[row - 1][self._get_col_index(column)]

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        # Time complexity: O((r * c)²)
        r, c = row - 1, self._get_col_index(column)
        self.formulas[(r, c)] = numbers
        self._calc_spreadsheet()
        return self.values[r][c]

    def _get_col_index(self, column: str) -> int:
        return ord(column) - ord("A")

    def _get_cell_indices(self, cell: str) -> tuple:
        # Valid cells: A1, A2, ..., B1, ..., Z1, Z2, ..., Z26
        return int(cell[1:]) - 1, ord(cell[0]) - ord("A")

    def _remove_formula(self, r: int, c: int) -> None:
        if (r, c) in self.formulas:
            del self.formulas[(r, c)]

    def _calc_spreadsheet(self) -> None:
        # Time complexity: O((r * c)²)
        # All the cells might have formulas, and each cell might
        # be dependent on many others (no cycles though).

        # Build the adjacency list and the indegree list
        adj, indegree = defaultdict(list), defaultdict(int)
        for key, cells in self.formulas.items():

            # Reset the dependent cell value to 0
            self.values[key[0]][key[1]] = 0

            for cell in cells:
                if ":" in cell:
                    # Cell range
                    cell_start, cell_end = cell.split(":")
                    row_start, col_start = self._get_cell_indices(cell_start)
                    row_end, col_end = self._get_cell_indices(cell_end)
                    for r in range(row_start, row_end + 1):
                        for c in range(col_start, col_end + 1):
                            adj[(r, c)].append(key)
                            indegree[key] += 1
                else:
                    # Single cell
                    r, c = self._get_cell_indices(cell)
                    adj[(r, c)].append(key)
                    indegree[key] += 1

        # Topological sort
        # Queue: (value, row, col)
        q = deque([(r, c) for r, c in adj if indegree[(r, c)] == 0])
        while q:
            r, c = q.popleft()

            # Value of the current cell, which doesn't depend
            # on others at this point
            val = self.values[r][c]

            for nr, nc in adj[(r, c)]:
                indegree[(nr, nc)] -= 1
                self.values[nr][nc] += val
                if indegree[(nr, nc)] == 0:
                    q.append((nr, nc))

    def print_spreadsheet(self) -> None:
        for row in self.values:
            print("  " + " ".join(f"{v:3}" for v in row))
        print()


if __name__ == "__main__":
    print("-" * 60)
    print("Design excel sum formula")
    print("-" * 60)

    print("Spreadsheet A1:D5\n")
    e = Excel(height=5, width="D")

    e.set(row=1, column="A", val=1)
    e.set(row=1, column="B", val=2)
    e.sum(row=1, column="C", numbers=["A1:B1"])
    print("C1 = A1 + B1")
    e.print_spreadsheet()
    assert e.get(row=1, column="C") == 3

    e.set(row=1, column="A", val=-1)
    assert e.get(row=1, column="C") == 1

    e.set(row=1, column="C", val=8)
    assert e.get(row=1, column="C") == 8

    for r in range(1, 5):
        e.set(row=r, column="A", val=r)
        e.set(row=r, column="B", val=r * r)
        e.set(row=r, column="C", val=-3 * r)
        e.sum(row=r, column="D", numbers=[f"A{r}:C{r}"])
        assert e.get(row=r, column="D") == r + r * r - 3 * r

    for col in range(4):
        column = chr(ord("A") + col)
        e.sum(row=5, column=column, numbers=["A1", f"A1:{column}4"])

    print("After some complex relationships:")
    e.print_spreadsheet()
