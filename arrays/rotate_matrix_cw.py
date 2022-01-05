"""
CRACKING THE CODING INTERVIEW
1.7. Rotate matrix.
Given an image represented by an NxN matrix, where
each pixel in the image is 4 bytes, write a method to rotate 
the image by 90 degrees. Can you do this in place?

Examples:
Input:  [
    [1, 2, 3],
    [1, 2, 3],
    [1, 1, 1],
]
Output: [
    [3, 3, 1],
    [2, 2, 1],
    [1, 1, 1],
]
"""
from typing import List
from copy import deepcopy


def layers_1(matrix: List[int]) -> List[int]:
    # In-place 90-deg-rotation of the matrix
    # Time complexity: O(n2)
    # Space complexity: O(1)

    # Perform rotation of 90deg clockwise
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
            matrix[layer][i] = matrix[offset][layer]
            matrix[offset][layer] = matrix[last][offset]
            matrix[last][offset] = matrix[i][last]
            matrix[i][last] = temp

    return matrix


def layers_2(matrix: list) -> list:
    # Book's solution
    # In-place 90-deg-rotation of the matrix
    # Time complexity: O(n2)
    # Space complexity: O(1)

    # Perform rotation of 90deg clockwise
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
        # Last index of the layer
        last = n - 1 - layer
        # Loop over the items of the layer
        for i in range(layer, last):
            # Offset
            offset = i - layer
            # Save the top item
            top = matrix[layer][i]
            # left -> top
            matrix[layer][i] = matrix[last - offset][layer]
            # bottom -> left
            matrix[last - offset][layer] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top

    return matrix


def pythonic(matrix: List[int]) -> List[int]:
    # `matrix[:]` keeps the reference to matrix, but updates the rows,
    # so it can be considered that they're modified in-place
    # matrix[:] = zip(*matrix[::-1])
    matrix[:] = map(list, zip(*matrix[::-1]))
    return matrix


if __name__ == "__main__":
    print("-" * 60)
    print("Rotate matrix 90deg clockwise")
    print("-" * 60)

    test_cases = [
        ([[1]], [[1]]),
        (
            [
                [1, 2],
                [4, 3],
            ],
            [
                [4, 1],
                [3, 2],
            ],
        ),
        (
            [
                [1, 2, 3],
                [1, 2, 3],
                [1, 1, 1],
            ],
            [
                [1, 1, 1],
                [1, 2, 2],
                [1, 3, 3],
            ],
        ),
        (
            [
                [1, 2, 3, 4],
                [12, 1, 2, 5],
                [11, 4, 3, 6],
                [10, 9, 8, 7],
            ],
            [
                [10, 11, 12, 1],
                [9, 4, 1, 2],
                [8, 3, 2, 3],
                [7, 6, 5, 4],
            ],
        ),
    ]

    for matrix, solution in test_cases:

        print("Matrix:", matrix)

        result = layers_1(deepcopy(matrix))
        output = "  layers_1 = "
        print_result = str(result)
        if len(print_result) > 40:
            print_result = print_result[:35] + " ...]]"
        output += print_result
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = layers_2(deepcopy(matrix))
        output = "  layers_2 = "
        print_result = str(result)
        if len(print_result) > 40:
            print_result = print_result[:35] + " ...]]"
        output += print_result
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = pythonic(deepcopy(matrix))
        output = "  pythonic = "
        print_result = str(result)
        if len(print_result) > 40:
            print_result = print_result[:35] + " ...]]"
        output += print_result
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
