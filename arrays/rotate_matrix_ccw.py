"""
CRACKING THE CODING INTERVIEW
1.7. Rotate matrix.
Given an image represented by an NxN matrix, where
each pixel in the image is 4 bytes, write a method to rotate 
the image by 90 degrees counter-clockwise. 
Can you do this in place?

Examples:
Input:  [
    [1, 2, 3],
    [8, 2, 4],
    [7, 6, 5],
]
Output: [
    [3, 4, 5],
    [2, 2, 6],
    [1, 8, 7],
]
"""
from copy import deepcopy

def rotate(matrix: list) -> list:
    # In-place 90-deg-rotation of the matrix
    # Time complexity: O(n2)
    # Space complexity: O(1)

    # Perform rotation of 90deg counter-clockwise
    # by layers (rows and cols)

    # Size of the matrix
    n = len(matrix)

    # Edge case
    if n == 0 or n != len(matrix[0]):
        return False

    # Number of layers, defining layer
    # as the perimeters of the successive
    # sub-matrices 
    # (i.e. a 4x4 matrix has the 4x4 and the
    # 2x2 sub-matrices `layers`)
    layers = n // 2
    # Loop over the layers
    for layer in range(layers):
        last = n - layer - 1
        for i in range(layer, last):
            offset = last - i + layer
            temp = matrix[layer][i]
            matrix[layer][i] = matrix[i][last]
            matrix[i][last] = matrix[last][offset]
            matrix[last][offset] = matrix[offset][layer]
            matrix[offset][layer] = temp

    return matrix


if __name__ == "__main__":
    print('-' * 60)
    print('Rotate matrix 90deg counter-clockwise')
    print('-' * 60)

    test_cases = [
        ([[1]], [[1]]),
        ([
            [1, 2],
            [4, 3],
        ], [
            [2, 3],
            [1, 4],
        ]),
        ([
            [1, 2, 3],
            [8, 2, 4],
            [7, 6, 5],
        ], [
            [3, 4, 5],
            [2, 2, 6],
            [1, 8, 7],
        ]),
        ([
            [ 1, 2, 3, 4],
            [12, 1, 2, 5],
            [11, 4, 3, 6],
            [10, 9, 8, 7],
        ], [
            [ 4,  5,  6,  7],
            [ 3,  2,  3,  8],
            [ 2,  1,  4,  9],
            [ 1, 12, 11, 10],
        ]),
    ]
    
    for matrix, solution in test_cases:

        mat = deepcopy(matrix)

        string = f'rotate\n{mat}'
        result = rotate(matrix)
        string += f'\n{result}'
        string += f'\nTest: {"OK" if solution == result else "NOT OK"}\n'
        print(string)