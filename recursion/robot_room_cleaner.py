"""
https://leetcode.com/problems/robot-room-cleaner/

You are controlling a robot that is located somewhere 
in a room. The room is modeled as an m x n binary grid 
where 0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the root 
that is guaranteed to be empty, and you do not have 
access to the grid, but you can move the robot using 
the given API Robot.

You are tasked to use the robot to clean the entire 
room (i.e., clean every empty cell in the room). The 
robot with the four given APIs can move forward, turn left, 
or turn right. Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper 
sensor detects the obstacle, and it stays on the current cell.

Design an algorithm to clean the entire room using the 
following APIs:

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}

Note that the initial direction of the robot will be facing up. 
You can assume all four edges of the grid are all surrounded 
by a wall.

Custom testing:
The input is only given to initialize the room and the 
robot's position internally. You must solve this problem 
"blindfolded". In other words, you must control the robot 
using only the four mentioned APIs without knowing the 
room layout and the initial robot's position.

Example 1:
Input: room = [
    [1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],
    [1,1,1,1,1,1,1,1]
], row = 1, col = 3
Output: Robot cleaned all rooms.
Explanation: All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and 
three columns right.

Example 2:
Input: room = [[1]], row = 0, col = 0
Output: Robot cleaned all rooms.

Constraints:
m == room.length
n == room[i].length
1 <= m <= 100
1 <= n <= 200
room[i][j] is either 0 or 1.
0 <= row < m
0 <= col < n
room[row][col] == 1
All the empty cells can be visited from the starting position.
"""
from typing import List
from copy import deepcopy


def print_matrix(room: List[int], start: tuple = None, initial_space: int = 3):
    if not room:
        room = []
    rows, cols = len(room), len(room[0])
    representation = [" x ", " . ", " c "]
    for r in range(rows):
        s = " " * initial_space
        for c in range(cols):
            if start and (r, c) == start:
                s += " 0 "
            else:
                s += representation[room[r][c]]

        print(s)
    print()


class Robot:
    def __init__(self, room: List[List[int]], row_start: int, col_start: int):
        """
        `room` states:
            0: obstacle
            1: free
            2: cleaned
        """
        self.room = room
        self.rows, self.cols = len(room), len(room[0])
        self.r, self.c = row_start, col_start
        self.dr, self.dc = 1, 0

    def move(self):
        nr, nc = self.r + self.dr, self.c + self.dc
        if (
            # Outside of the boundary conditions
            not 0 <= nr < self.rows
            or not 0 <= nc < self.cols
            # The cell has an obstacle
            or self.room[nr][nc] == 0
        ):
            return False

        self.r, self.c = nr, nc
        return True

    def turn_right(self):
        # Rotate 90deg counter-clockwise
        self.dr, self.dc = self.dc, -self.dr

    def turn_left(self):
        # Rotate 90deg clockwise
        self.dr, self.dc = -self.dc, self.dr

    def clean(self):
        self.room[self.r][self.c] = 2


def backtrack1(robot: Robot):
    # Time complexity: O(n - m)
    # Space complexity: O(n - m)
    # where `n` is the number of cells,
    # and `m` is the number of obstacles

    def go_back():
        # Go back to the previous position
        # (rotate 180deg, move to the previous cell,
        # and rotate 180deg again to have the same
        # previous direction)
        robot.turn_right()
        robot.turn_right()
        robot.move()
        robot.turn_right()
        robot.turn_right()

    def backtrack(r: int, c: int, direction: int):
        # Clean the current cell
        visited.add((r, c))
        robot.clean()

        # Explore next cells
        for i in range(num_directions):
            new_direction = (direction + i) % num_directions
            dr, dc = directions[new_direction]
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited and robot.move():
                backtrack(nr, nc, new_direction)
                # If we reach a cell where there are no new
                # neighbors to explore, we have to `backtrack`,
                # that is, we go back to the previous position
                go_back()

            # After exhausting the current path and bumping into
            # an obstacle, the robot needs to turn before moving.
            # Not important if we decide to `turn_left` or
            # `turn_right`, but it has to be always the same
            robot.turn_left()
            # robot.turn_right()
            # print_matrix(robot.room)

    # Hashset to keep track of the visited cells
    visited = set()

    # Both orders of the directions work
    # (clock-wise and counter-clock-wise)
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    # directions = ((1, 0), (0, -1), (-1, 0), (0, 1))

    num_directions = len(directions)
    backtrack(0, 0, 0)
    return


if __name__ == "__main__":
    print("-" * 60)
    print("Robot room cleaner")
    print("-" * 60)

    rooms = [
        [
            [1, 1, 1, 1, 0, 0, 1, 1],
            [1, 0, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ],
        [
            [1, 1, 1, 1, 0, 0, 1, 1],
            [0, 0, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ],
    ]

    test_cases = [
        # (room, row_start, col_start)
        (rooms[0], 3, 3),
        (rooms[0], 3, 0),
        (rooms[1], 3, 0),
    ]

    for room, row_start, col_start in test_cases:

        print(f">>> Room:")
        print_matrix(room, (row_start, col_start))

        robot = Robot(deepcopy(room), row_start, col_start)
        backtrack1(robot)
        print("  after backtracking:")
        print_matrix(robot.room)
