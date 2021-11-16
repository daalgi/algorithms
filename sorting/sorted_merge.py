"""
CRACKING THE CODING INTERVIEW
10.1 Sorted merge:
You are given two sorted arrays, A and B, where A has a large
enough buffer at the end to hold B. Write a method to merge B
into A in sorted order.
"""


def sorted_merge(a: list, b: list) -> list:
    # Sorted merge in place
    # (`a` has enough buffer to allocate additional space).
    # Compare elements of `a` and `b` and insert them in order,
    # but starting from the back of the array, where there's empty space.

    # Use three pointers:
    # - A pointer to iterate over `a`
    # - A pointer to iterate over `b`
    # - A pointer to the current write location in `a`

    # Pointer starting at the last element in `a`
    write_a = len(a) - 1

    # Pointer starting at the last not None element in `a`
    read_a = write_a
    while read_a >= 0 and a[read_a] is None:
        read_a -= 1

    # Pointer starting at the last element in `b`
    read_b = len(b) - 1

    # Loop over until the start of `b` is reached. Once `b` is finished,
    # the array `a` already has its elements sorted, so no need to continue.
    while read_b >= 0:
        if read_a >= 0 and a[read_a] > b[read_b]:
            # Still haven't exhausted `a` and a > b
            a[write_a] = a[read_a]
            read_a -= 1
        else:
            # Exhausted `a` or b > a
            a[write_a] = b[read_b]
            read_b -= 1
        write_a -= 1

    return a


if __name__ == "__main__":
    print("-" * 60)
    print("Sorted merge")
    print("-" * 60)

    test_cases = [
        ([1, 3, 5], [], [1, 3, 5]),
        ([None, None, None], [1, 3, 5], [1, 3, 5]),
        ([1, 3, 5, None, None], [0, 2], [0, 1, 2, 3, 5]),
        ([1, 3, 5, None, None], [2, 3], [1, 2, 3, 3, 5]),
        ([1, 3, 5, None, None], [-1, 0], [-1, 0, 1, 3, 5]),
        ([1, 3, 5, None, None], [6, 7], [1, 3, 5, 6, 7]),
    ]

    for a, b, solution in test_cases:

        result = sorted_merge([*a], [*b])

        string = f"sol{a, b} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
