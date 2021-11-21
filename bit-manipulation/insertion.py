"""
CRACKING THE CODING INTERVIEW
5.1 Insertion
You are given two 32-bit numbers, N and M, 
and two bit positions, i and j.
Write a method to insert M into N such that 
M starts at bit j and ends at bit i.
You can assume that the bits j through i have 
enough space to fit all of M.
That is, if M = 10011, you can assume that there 
are at least 5 bits between j and i.
You would not, for example, have j = 3 and i = 2, b
ecause M could not fully
fit betweeen bit 3 and bit 2.

Example 1:
Input:  N = 11111, M = 100, i = 1, j = 3
Output: N = 11001
Explanation
N_cleared = 10001
M_shifted = 01000

Example 2:
Input:  N = 10000000000, M = 10011, i = 2, j = 6
Output: N = 10001001100
Explanation
N_cleared = 10000000000
M_shifted = 00001001100
"""


def insertion(n: int, m: int, i: int, j: int) -> int:
    # Sequence of all 1s
    all_ones = ~0

    # 1s before position `j`, then 0s
    left = all_ones << (j + 1)

    # 1s after position `i`
    right = (1 << i) - 1

    # All 1s, except for 0s between `i` and `j`
    mask = left | right

    # Clear bits `j` through `i`
    n_cleared = n & mask

    # Move `m` into correct position
    m_shifted = m << i

    # OR them
    return n_cleared | m_shifted


if __name__ == "__main__":
    print("-" * 60)
    print("Insertion")
    print("-" * 60)

    test_cases = [
        (5, 1, 0, 0, 5),
        (5, 1, 1, 1, 7),
        (5, 1, 2, 2, 5),
        (5, 1, 3, 3, 13),
        (5, 2, 0, 1, 6),
        (5, 2, 1, 2, 5),
        (5, 2, 2, 3, 9),
        (16, 4, 0, 2, 20),
        (16, 4, 1, 3, 24),
        (16, 4, 2, 4, 16),
        (16, 4, 3, 5, 32),
        (31, 5, 0, 2, 29),
        (31, 5, 1, 3, 27),
        (31, 5, 2, 4, 23),
    ]

    for n, m, i, j, solution in test_cases:

        string = f"insertion{n, m, i, j} = "
        string += " " * (35 - len(string))
        result = insertion(n, m, i, j)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
