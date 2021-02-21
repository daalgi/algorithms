from unittest import TestCase
from sudoku import (
    random_int_within_block, swap_rows, swap_columns,
    rotate, vertical_mirroring, horizontal_mirroring,
    Board
)


class TestMethods(TestCase):
    def test_random_int_within_block(self):
        # Only for 9x9 grids
        for i in [0, 1, 2]:
            r = random_int_within_block(i)
            self.assertNotEqual(r, i)
            self.assertLess(r, 3)

        for i in [3, 4, 5]:
            r = random_int_within_block(i)
            self.assertNotEqual(r, i)
            self.assertGreater(r, 2)
            self.assertLess(r, 6)

        for i in [6, 7, 8]:
            r = random_int_within_block(i)
            self.assertNotEqual(r, i)
            self.assertGreater(r, 5)
            self.assertLess(r, 9)

    def test_swap_rows(self):
        arr = [[1, 2], [8, 9]]
        res = swap_rows(arr, 0, 1)
        self.assertEqual(res, [[8, 9], [1, 2]])

    def test_swap_columns(self):
        arr = [[1, 2], [8, 9]]
        res = swap_columns(arr, 0, 1)
        self.assertEqual(res, [[2, 1], [9, 8]])

    def test_rotate(self):
        arr = [[1, 2], [8, 9]]
        res = rotate(arr)
        self.assertEqual(res, [[8, 1], [9, 2]])

    def test_vertical_mirroring(self):
        arr = [[1, 2], [8, 9]]
        res = vertical_mirroring(arr)
        self.assertEqual(res, [[8, 9], [1, 2]])

    def test_horizontal_mirroring(self):
        arr = [[1, 2], [8, 9]]
        res = horizontal_mirroring(arr)
        self.assertEqual(res, [[2, 1], [9, 8]])


class TestBoard(TestCase):
    def test_valid_sudoku(self):
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
        self.assertTrue(b.is_valid())

        # Make the sudoku invalid in the first row, column and block
        b.array[0][0] = 8
        self.assertFalse(b.is_valid_row(0))
        self.assertFalse(b.is_valid_column(0))
        self.assertFalse(b.is_valid_block(0, 0))
        self.assertFalse(b.is_valid_block(0, 2))
        self.assertFalse(b.is_valid_block(2, 2))
        self.assertFalse(b.is_valid())

        # The rest of the rows and columns are still valid
        for i in range(1, 9):
            self.assertTrue(b.is_valid_row(i))
            self.assertTrue(b.is_valid_column(i))        

    def test_create_valid_sudoku(self):
        b = Board()
        b.generate()
        self.assertTrue(b.is_valid())

        b.shuffle(7)
        self.assertTrue(b.is_valid())

        b.rotate()
        self.assertTrue(b.is_valid())

        b.vertical_mirroring()
        self.assertTrue(b.is_valid())

        b.horizontal_mirroring()
        self.assertTrue(b.is_valid())

        b.cipher()
        self.assertTrue(b.is_valid())

    def solve(self):
        b = Board([
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
        b.solve()
        self.assertTrue(b.is_valid())