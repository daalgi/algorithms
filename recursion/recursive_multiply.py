"""
CRACKING THE CODING INTERVIEW
8.5 Recursive multiply:
Write a recursive function to multiply two positive integers
without using the * operator (or / operator). You can use
addition, subtraction, and bit shifting, but you should
minimize the number of those operators.
"""


def recursion(a: int, b: int) -> int:
    # Time complexity: O(logn) where n is the smallest number
    # Space complexity: O(1)

    # a * b = a + a + a + ... (b times)
    # We can reduce the sum operations multiplying by 2 using
    # the shift operator

    def rec(mini: int, maxi: int) -> int:
        # Base case
        if mini == 1:
            return maxi

        if mini & 1 == 0:
            # If even, we can shift left `maxi` (x2)
            # and shift right `mini` (/2)
            maxi <<= 1
            mini >>= 1
            return rec(mini, maxi)

        # If odd, we can decompose the result as i.e.: 
        # 20 * 5 = 20 * (4 + 1) = 20 * 4 + 20 * 1
        return rec(mini - 1, maxi) + maxi

    # Identify the minimum and maximum values to reduce
    # the number of operations
    mini, maxi = (a, b) if a < b else (b, a)
    # Edge case, when there's a zero
    if mini == 0:
        return 0
    # Call the recursive function
    return rec(mini, maxi)


if __name__ == "__main__":
    print("-" * 60)
    print("Recursive multiply")
    print("-" * 60)

    test_cases = [
        (2, 0, 0),
        (2, 1, 2),
        (3, 2, 6),
        (5, 5, 25),
        (5, 25, 125),
        (86, 13, 86 * 13),
        (93, 25, 93 * 25),
    ]

    for a, b, solution in test_cases:

        string = f"recursion {a, b} ="
        string += " " * (25 - len(string))
        result = recursion(a, b)
        string += str(result)
        string += " " * 30
        test_ok = solution == result
        print(string, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')

        print()
