"""
CRACKING THE CODING INTERVIEW
8.3 Magic index:
A magic index in an array A[1...n-1] is defined to be an index
such that A[i] = i. Given a sorted array of distinct integers,
write a method to find a magic index, if one exists, in array A.

What if the values are not distinct?
"""


def brute_force(array: list) -> int:
    # Time complexity: O(n)
    n = len(array)
    for i in range(n):
        if array[i] == i:
            return i
    return None


def binary_search(array: list) -> int:
    # Time complexity: O(logn)
    # Binary search-like algorithm

    def f(array: list, left: int, right: int) -> int:
        # Recursive function+
        
        # Base case
        if left > right:
            # Pointers crossed, there's no magic index
            return None

        # Middle index
        mid = (left + right) // 2

        # Determine where the magic index could be
        if array[mid] == mid:
            # Magic index found
            return mid
        if array[mid] < mid:
            # Search the right side
            return f(array, mid + 1, right)
        # Search the left side
        return f(array, left, mid - 1)

    # Call the recursive function
    return f(array, 0, len(array) - 1)


if __name__ == "__main__":
    print("-" * 60)
    print("Magic index")
    print("-" * 60)

    test_cases = [
        ([0, 3, 8], 0),
        ([1, 3, 8], None),
        ([-1, 0, 2], 2),
        ([-10, -3, -1, 3, 7, 8, 9], 3),
        ([-10, -3, -1, 0, 1, 3, 5, 6, 8], 8),
    ]

    for grid, solution in test_cases:

        string = f" brute_force = "
        string += " " * (25 - len(string))
        result = brute_force(grid)
        string += str(result)
        string += " " * (65 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f"binary_search = "
        string += " " * (25 - len(string))
        result = binary_search(grid)
        string += str(result)
        string += " " * (65 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
