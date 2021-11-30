"""
CRACKING THE CODING INTERVIEW
8.2 Robot in a grid:
Imagine a robot sitting on the upper left corner of a grid with
r rows and c columns. The robot can only move in two directions,
right and down, but certain cells are "off limits" such that 
the robot cannot step on them. Design an algorithm to find
a path for the robot from the top left to the bottom right.
"""


def brute_force(steps: int) -> int:
    pass


def dp_recursion(steps: int) -> int:
    pass


def dp_iterative(steps: int) -> int:
    pass


if __name__ == "__main__":
    print("-" * 60)
    print("Robot in a grid")
    print("-" * 60)

    test_cases = [
        (1, 1),
        (2, 2),
        (3, 4),
        (4, 7),
        (13, 1705),
        (25, 2555757),
    ]

    for num, solution in test_cases:

        string = f" brute_force({num}) = "
        string += " " * (25 - len(string))
        result = brute_force(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f"dp_recursion({num}) = "
        string += " " * (25 - len(string))
        result = dp_recursion(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f"dp_iterative({num}) = "
        string += " " * (25 - len(string))
        result = dp_iterative(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
