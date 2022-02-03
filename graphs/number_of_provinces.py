"""
https://leetcode.com/problems/number-of-provinces/

There are n cities. Some of them are connected, while some 
are not. If city a is connected directly with city b, and 
city b is connected directly with city c, then city a is 
connected indirectly with city c.

A province is a group of directly or indirectly connected 
cities and no other cities outside of the group.

You are given an n x n matrix isConnected where 
isConnected[i][j] = 1 if the ith city and the jth city are 
directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""
from copy import deepcopy
from typing import List


def print_matrix(mat):
    print()
    for row in mat:
        print(" " * 3 + " ".join(["." if v == 0 else "#" for v in row]))
    print()


class UnionFind:
    def __init__(self, size: int):
        # Time complexity: O(n)
        # Space complexity: O(n)
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        # Keep track of the count of not connected components
        self.count = size

    def find(self, x: int) -> int:
        # Time complexity: α(n) = O(1)
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        # Time complexity: α(n) = O(1)
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
            # If the two nodes `x` and `y` were not connected,
            # now they become so, therefore we have to
            # decrease the count of non-connected components.
            self.count -= 1

    def connected(self, x: int, y: int) -> bool:
        # Time complexity: α(n) = O(1)
        return self.find(x) == self.find(y)


def union_find(isConnected: List[List[int]]) -> int:
    # Time complexity: O(n³)
    #   Traverse the matrix: O(n²)
    #   Union and find: α(n)
    #   Union and find worst case: O(n)
    #   Union and find on average: O(1)
    #   (α(n) is O(1) on average)
    # Space complexity: O(n)
    n = len(isConnected)
    uf = UnionFind(n)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if isConnected[i][j]:
                uf.union(i, j)

    return uf.count


if __name__ == "__main__":
    print("-" * 60)
    print("Number of provinces")
    print("-" * 60)

    test_cases = [
        # ( connectivity_matrix, solution )
        ([[1]], 1),
        ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
        ([[1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1], [1, 1, 1, 1]], 1),
        ([[1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 0], [1, 1, 0, 1]], 2),
    ]

    for matrix, solution in test_cases:

        print("Connectivity matrix:")
        print_matrix(matrix)

        result = union_find(deepcopy(matrix))
        output = f"     union_find = "
        output += f"{result:>4}"
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
