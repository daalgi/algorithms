"""
CRACKING THE CODING INTERVIEW
1.8. Zero matrix.
Write an algorithm such that if an element in an MxN matrix
is 0, its entire row and column are set to 0.

Examples:
Input:  [
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]
Output: [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 1],
]
"""

def zero_matrix(matrix: list) -> list:
    # In-place modification of the matrix
    # Time complexity: O(m * n)
    # Space complexity: O(m + n)

    # Size of the matrix
    m, n = len(matrix), len(matrix[0])

    # Store the indices containing zeros
    row_zeros = set()
    col_zeros = set()

    # Loop over the elements of the matrix
    # to find the indices of the zeros
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row_zeros.add(i)
                col_zeros.add(j)
    
    # Loop over the row indices with zeros:
    for row in row_zeros:
        for col in range(n):
            matrix[row][col] = 0
    
    # Loop over the col indices with zeros:
    for col in col_zeros:
        for row in range(m):
            matrix[row][col] = 0

    return matrix


if __name__ == "__main__":
    print('-' * 60)
    print('Zero matrix')
    print('-' * 60)

    test_cases = [
        ([[1]], [[1]]),
        ([
            [1, 2, 0], 
            [1, 1, 1]
        ], [
            [0, 0, 0], 
            [1, 1, 0]
        ]),
        ([
            [1, 0, 1], 
            [1, 1, 1]
        ], [
            [0, 0, 0], 
            [1, 0, 1]
        ]),
        ([
            [0, 1, 1], 
            [1, 1, 1]
        ], [
            [0, 0, 0], 
            [0, 1, 1]
        ]),
        ([
            [0, 1, 0], 
            [1, 1, 1]
        ], [
            [0, 0, 0], 
            [0, 1, 0]
        ]),
        ([
            [1, 2, 0, 1], 
            [1, 1, 1, 1]
        ], [
            [0, 0, 0, 0], 
            [1, 1, 0, 1]
        ]),
        ([
            [1, 2, 1], 
            [1, 1, 1]
        ], [
            [1, 2, 1], 
            [1, 1, 1]
        ]),
        ([
            [1, 2, 1], 
            [1, 2, 1], 
            [1, 0, 1]
        ], [
            [1, 0, 1], 
            [1, 0, 1], 
            [0, 0, 0]
        ]),
        ([
            [1, 0, 1, 2, 1], 
            [1, 1, 1, 2, 1], 
            [1, 1, 1, 0, 1], 
            [1, 1, 1, 2, 1],
        ], [
            [0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 1], 
            [0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 1],
        ]),
    ]
    
    for matrix, solution in test_cases:

        string = f'zero_matrix\n{matrix}'
        result = zero_matrix(matrix)
        string += f'\n{result}'
        string += f'\nTest: {"OK" if solution == result else "NOT OK"}\n'
        print(string)