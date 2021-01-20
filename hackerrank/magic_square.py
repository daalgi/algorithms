"""
https://www.hackerrank.com/challenges/magic-square-forming/problem
We define a magic square to be an nxn matrix of distinct positive integers
from 1 to n^2 where the sum of any row, column, or diagonal of length 
is always equal to the same number: the magic constant.

You will be given a 3x3 matrix of integers in the inclusive range [1, 9]. 
We can convert any digit `a` to any other digit `b` in the range [1, 9] 
at cost of |a - b|. Given s, convert it into a magic square at minimal cost.

Note: The resulting magic square must contain distinct integers in the inclusive range [1, 9].

Example
$s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
The matrix looks like this:
5 3 4
1 5 8
6 4 2

We can convert it to the following magic square:
8 3 4
1 5 9
6 7 2

This took three replacements at a cost of |5-8| + |8-9| + |4-7| = 7
"""
# 3x3 magic square possible solutions
solutions = [
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
]

def cost(s, r):
    return sum(abs(s[i][j]-r[i][j]) for i in range(3) for j in range(3))

def forming_magic_square(s):
    return min(cost(s, solution) for solution in solutions)


if __name__ == "__main__":
    #s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
    #print(forming_magic_square(s))

    print('-'*50)
    print('Form a magic square 3x3 at a minimum cost')
    print('-'*50)
    test_cases = [
        ([[4,9,2],[3,5,7],[8,1,5]], 1),
        ([[4,5,8],[2,4,1],[1,9,7]], 14),
        ([[2,9,8],[4,2,7],[5,6,7]], 21),
    ]
    for matrix, solution in test_cases:
        cost_min = forming_magic_square(matrix)
        print('matrix = ', matrix, f',\tminimum cost = {cost_min},', 
            f'\tTest: {cost_min == solution if solution is not None else "?"}')
    print()