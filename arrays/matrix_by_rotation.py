"""
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

Given two n x n binary matrices mat and target, 
return true if it is possible to make mat equal to target 
by rotating mat in 90-degree increments, or false otherwise.

Example 1:
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to 
make mat equal target.

Example 2:
Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to 
target by rotating mat.

Example 3:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise 
two times to make mat equal target.

Constraints:
n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.
"""
from typing import List
from copy import deepcopy


def sol1(matrix: List[List[int]], target: List[List[int]]) -> bool:
    def are_equal(a: List[List[int]], b: List[List[int]]) -> bool:
        n = len(a)
        for i in range(n):
            for j in range(n):
                if a[i][j] != b[i][j]:
                    return False
        return True

    def rotate(a: List[List[int]]) -> List[List[int]]:
        return list(zip(*a[::-1]))

    if are_equal(matrix, target):
        return True

    for _ in range(3):
        matrix = rotate(matrix)
        if are_equal(matrix, target):
            return True
    return False


def sol2(matrix: List[List[int]], target: List[List[int]]) -> bool:
    for _ in range(4):
        if matrix == target:
            return True
        matrix = [list(row) for row in zip(*matrix[::-1])]
    return False


if __name__ == "__main__":
    print("-" * 60)
    print("Determine whether matrix can be obtained by rotation")
    print("-" * 60)

    test_cases = [
        ([[1]], [[1]], True),
        ([[1, 0], [0, 0]], [[0, 0], [0, 1]], True),
        ([[0, 1], [1, 0]], [[1, 0], [0, 1]], True),
        ([[0, 1], [1, 1]], [[1, 0], [0, 1]], False),
        ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]], True),
        ([[0, 0, 0], [0, 0, 1], [0, 0, 1]], [[0, 0, 0], [0, 0, 1], [0, 0, 1]], True),
    ]

    for matrix, target, solution in test_cases:

        print("Matrix:", matrix)
        print("Target:", target)

        result = sol1(deepcopy(matrix), target)
        output = "    sol1 = "
        print_result = str(result)
        if len(print_result) > 40:
            print_result = print_result[:35] + " ...]]"
        output += print_result
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)
        
        result = sol2(deepcopy(matrix), target)
        output = "    sol2 = "
        print_result = str(result)
        if len(print_result) > 40:
            print_result = print_result[:35] + " ...]]"
        output += print_result
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
