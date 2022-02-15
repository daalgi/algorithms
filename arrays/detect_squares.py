"""
https://leetcode.com/problems/detect-squares/

You are given a stream of points on the X-Y plane. 
Design an algorithm that:
- Adds new points from the stream into a data 
structure. Duplicate points are allowed and should 
be treated as different points.
- Given a query point, counts the number of ways to 
choose three points from the data structure such that 
the three points and the query point form an axis-aligned 
square with positive area.

An axis-aligned square is a square whose edges are all 
the same length and are either parallel or perpendicular 
to the x-axis and y-axis.

Implement the DetectSquares class:
- DetectSquares() Initializes the object with an empty 
data structure.
- void add(int[] point) Adds a new point point = [x, y] 
to the data structure.
- int count(int[] point) Counts the number of ways to form 
axis-aligned squares with point point = [x, y] as described 
above.

Example 1:
Input
["DetectSquares", "add", "add", "add", "count", 
"count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], 
[[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
                               //   - The first, second, and third points
detectSquares.count([14, 8]);  // return 0. The query point cannot 
            // form a square with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
                               //   - The first, second, and third points
                               //   - The first, third, and fourth points
 
Constraints:
point.length == 2
0 <= x, y <= 1000
At most 3000 calls in total will be made to add and count.
"""
from typing import List
from collections import defaultdict, Counter


class DetectSquaresArray:
    def __init__(self):
        # Time complexity: O(1)
        # Space complexity: O(n)
        # Since the range of valid coordinates is rather small
        # (from 0 to 1000), we can create a matrix of 1001 x 1001,
        # where each element (x, y) contains the count of points
        # with `x` and `y` coordinates added
        self.max_size = 1001
        self.grid = [[0] * self.max_size for _ in range(self.max_size)]

    def add(self, point: List[int]):
        # Time complexity: O(1)
        self.grid[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        # Time complexity: O(1)
        x, y, count = *point, 0

        # Strategy: look for a point [i, j] that can be the
        # diagonal of a potential square. Requirements:
        # - i != x
        # - abs(x - i) == abs(y - j)
        # If we find a potential diagonal, we have to check
        # if the (x, j) and (i, y) points exist. If so,
        # to take into account all the square combinations:
        # combinations = count(i, j) * count(x, j) * count(i, y)

        # Loop over the `x` coordinates
        for i in range(self.max_size):
            if i != x and self.grid[i][y]:
                # If the current `i` is not equal to `x`,
                # Loop over the `y` coordinates
                for j in range(self.max_size):
                    if self.grid[i][j] and abs(x - i) == abs(y - j):
                        count += self.grid[i][j] * self.grid[i][y] * self.grid[x][j]
        return count


class DetectSquaresArrayHashset:
    def __init__(self):
        # Time complexity: O(1)
        # Space complexity: O(n)
        self.max_size = 1001
        self.grid = [[0] * self.max_size for _ in range(self.max_size)]

        # Same idea as before, but we add hashsets to keep track of
        # the existing `x` and `y` coordinates, so we can speed-up
        # the loops scaning the coordinates.
        self.xs = set()
        self.ys = set()

    def add(self, point: List[int]):
        # Time complexity: O(1)
        self.grid[point[0]][point[1]] += 1
        self.xs.add(point[0])
        self.ys.add(point[1])

    def count(self, point: List[int]) -> int:
        # Time complexity: O(1)
        x, y, count = *point, 0
        # Loop over the added `x`s
        for i in self.xs:
            if i != x and self.grid[i][y]:
                # Loop over the added `y`s
                for j in self.ys:
                    if self.grid[i][j] and abs(x - i) == abs(y - j):
                        count += self.grid[i][j] * self.grid[i][y] * self.grid[x][j]
        return count


class DetectSquaresHashmap:
    def __init__(self):
        # Time complexity: O(1)
        # Space complexity: O(n)

        # Same idea as before, but instead of storing the complete
        # matrix, we can store a hashmap of the points
        self.points = defaultdict(int)
        self.xs = set()
        self.ys = set()

    def add(self, point: List[int]):
        # Time complexity: O(1)
        self.points[tuple(point)] += 1
        self.xs.add(point[0])
        self.ys.add(point[1])

    def count(self, point: List[int]) -> int:
        # Time complexity: O(1)
        x, y, count = *point, 0
        for i in self.xs:
            if i != x and (i, y) in self.points:
                for j in self.ys:
                    if (i, j) in self.points and abs(x - i) == abs(y - j):
                        count += (
                            self.points[i, j] * self.points[i, y] * self.points[x, j]
                        )
        return count


class DetectSquaresCounters:
    def __init__(self):
        # Time complexity: O(1)
        # Space complexity: O(n)
        # Counter of points
        self.d = Counter()
        # Counter for each coordinate `x`, so we can quickly find
        # all points with `x` coordinate
        # x -> all `y` coordinates with frequencies
        self.x_coord = defaultdict(Counter)

    def add(self, point: List[int]):
        # Time complexity: O(1)
        x, y = point
        self.d[x, y] += 1
        self.x_coord[x][y] += 1

    def count(self, point: List[int]) -> int:
        # Time complexity: O(n)
        x, y = point
        count = 0
        # Loop over the `yy` cordinates of the existing
        # points with `x` coordinate
        for yy in self.x_coord[x]:
            if y == yy:
                # If the same y coord, can't be an area
                continue
            # Square side length
            side = yy - y
            # For the given point (x, y) and the current `yy`,
            # there are two possible squares
            # (to the right and to the left of (x, y))
            # For the first square 
            # (to the right of (x,y) assuming side > 0),
            # the other 3 corners are
            # (x, yy), (x + side, y), (x + side, yy)
            count += self.d[x, yy] * self.d[x + side, y] * self.d[x + side, yy]
            # For the second square
            # (to the left of (x,y) assuming side > 0),
            # the other 3 corners are
            # (x, yy), (x - side, y), (x - side, yy)
            count += self.d[x, yy] * self.d[x - side, y] * self.d[x - side, yy]

        return count


if __name__ == "__main__":
    print("-" * 60)
    print("Detect squares")
    print("-" * 60)

    points = [
        ([0, 0], [1, 0], [1, 1], [2, 2]),
        ([0, 0], [1, 0], [1, 1], [2, 2], [2, 1], [1, 2], [0, 2]),
    ]

    test_cases = [
        # (points, point, solution)
        (points[0], [0, 2], 0),
        (points[0], [0, 1], 1),
        (points[1], [0, 1], 2),
        (points[1], [0, 3], 0),
    ]

    for points, point, solution in test_cases:

        points_str = str(points)
        if len(points_str) > 60:
            points_str = points_str[:55] + " ...]"
        print("Points:", points_str)
        print("Point:", point)

        ds_array = DetectSquaresArray()
        ds_array_hashset = DetectSquaresArrayHashset()
        ds_hashmap = DetectSquaresHashmap()
        ds_counters = DetectSquaresCounters()

        for p in points:
            ds_array.add(p)
            ds_array_hashset.add(p)
            ds_hashmap.add(p)
            ds_counters.add(p)

        result = ds_array.count(point)
        output = f"         array = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = ds_array_hashset.count(point)
        output = f" array-hashset = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = ds_hashmap.count(point)
        output = f"       hashmap = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = ds_counters.count(point)
        output = f"      counters = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
