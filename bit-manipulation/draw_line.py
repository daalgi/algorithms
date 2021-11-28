"""
CRACKING THE CODING INTERVIEW
5.8 Draw Line
A monochrome screen is stored as a single array of bytes,
allowing eight consecutive pixels to be stored in one byte.
The screen has width w, where w is divisible by 8 (that is,
no byte will be split across rows). The height of the screen,
of course, can be derived from the length of the array and 
the width. Implement a function that draws a horizontal
line from (x1, y) to (x2, y).

The method signature should look something like:
draw_line(screen: list, width: int, x1: int, x2: int, y: int)
"""


def draw_line(screen: list, width: int, x1: int, x2: int, y: int) -> int:
    n = len(screen)  # bytes
    height = n * 8 // width  # bits

    # Check for out-of-boundaries errors
    if y >= height:
        return None
    if not (0 <= x1 < width) or not (0 <= x2 < width):
        return None

    # Force x1 <= x2
    if x2 < x1:
        x1, x2 = x2, x1

    # Get the leftmost bit in the current element to be set
    left_pointer = x1 % 8
    # Pointer to the start of the current element
    current_x0 = x1 // 8 * 8
    # Loop until all the bits in the horizontal line have
    # been set
    while current_x0 <= x2:
        # Get the leftmost bit in the element to be set
        right_pointer = x2 % 8 if x2 - current_x0 < 8 else 7
        # print("left_pointer", left_pointer)
        # print("right_pointer", right_pointer)

        left = (1 << (8 - left_pointer)) - 1
        right = 0xFF << (8 - right_pointer - 1)
        # print(bin(left))
        # print(bin(right))
        # print(bin(left & right))

        # Get the first element in the `screen` list of bytes
        # where the line starts
        index = current_x0 // 8 + y * width // 8
        # print('index', index)
        screen[index] = left & right

        # In the following iterations, the left bit to be set
        # will always start at the rightmost bit
        left_pointer = 0
        # Update the pointer to the current x coordinate
        current_x0 += 8

    return screen


if __name__ == "__main__":
    print("-" * 60)
    print("Draw line")
    print("-" * 60)

    test_cases = [
        # (screen, width, x1, x2, y, solution)
        # input:
        # 00000000 00000000
        # 00000000 00000000
        ([0, 0, 0, 0], 16, 16, 7, 0, None),
        ([0, 0, 0, 0], 16, 10, 17, 0, None),
        ([0, 0, 0, 0], 16, 2, 7, 2, None),
        # output:
        # 11111111 00000000
        # 00000000 00000000
        ([0, 0, 0, 0], 16, 0, 7, 0, [255, 0, 0, 0]),
        # output:
        # 11000000 00000000
        # 00000000 00000000
        ([0, 0, 0, 0], 16, 0, 1, 0, [128 + 64, 0, 0, 0]),
        # output:
        # 00010000 00000000
        # 00000000 00000000
        ([0, 0, 0, 0], 16, 3, 3, 0, [16, 0, 0, 0]),
        # output:
        # 00001111 00000000
        # 00000000 00000000
        ([0, 0, 0, 0], 16, 4, 7, 0, [8 + 4 + 2 + 1, 0, 0, 0]),
        # output:
        # 00000001 00000000
        # 00000000 00000000
        ([0, 0, 0, 0], 16, 7, 7, 0, [1, 0, 0, 0]),
        # output:
        # 00000000 11000000
        # 00000000 00000000
        ([0, 0, 0, 0], 16, 8, 9, 0, [0, 128 + 64, 0, 0]),
        # output:
        # 00000000 00000111
        # 00000000 00000000
        ([0, 0, 0, 0], 16, 13, 15, 0, [0, 4 + 2 + 1, 0, 0]),
        # output:
        # 00000000 00000000
        # 01111110 00000000
        ([0, 0, 0, 0], 16, 1, 6, 1, [0, 0, 255 - 128 - 1, 0]),
        # output:
        # 00000000 00000000
        # 00000000 00000110
        ([0, 0, 0, 0], 16, 13, 14, 1, [0, 0, 0, 4 + 2]),
        # output:
        # 00001111 11000000
        # 00000000 00000000
        ([0, 0, 0, 0], 16, 4, 9, 1, [0, 0, 8 + 4 + 2 + 1, 128 + 64]),
        # output:
        # 00000000 00000000
        # 00000011 11000000
        ([0, 0, 0, 0], 16, 6, 9, 1, [0, 0, 2 + 1, 128 + 64]),
        # output:
        # 11111111 11111111
        # 00000000 00000000
        ([0, 0, 0, 0], 16, 0, 15, 0, [255, 255, 0, 0]),
        # output:
        # 00000000 00000000
        # 11111111 11111111
        ([0, 0, 0, 0], 16, 0, 15, 1, [0, 0, 255, 255]),
        # input:
        # 00000000 00000000 00000000
        # 11111111 11111111 11111111
        ([0, 0, 0, 0, 0, 0], 24, 0, 23, 1, [0, 0, 0, 255, 255, 255]),
    ]

    for screen, width, x1, x2, y, solution in test_cases:

        input_str = f"input  = {screen}"
        result = draw_line(screen, width, x1, x2, y)
        output_str = f"output = {result}"
        string = f"draw_line{x1, x2, y}"
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
        print(input_str)
        print(output_str)

        print()
