"""
CRACKING THE CODING INTERVIEW
5.5 Debugger
Explain what the following code does:
n & (n - 1) == 0

Explanation:
Checks whether `n` and `n-1` never share a 1 bit in
the same place. Therefore, it's equivalent to check if
`n` is a power of 2 (or if `n` is 0).
"""


def f(num: int) -> int:
    return num & (num - 1) == 0


if __name__ == "__main__":
    print("-" * 60)
    print("Debugger")
    print("-" * 60)

    test_cases = [
        (1, True),
        (2, True),
        (3, False),
        (4, True),
        (5, False),
        (6, False),
        (7, False),
        (8, True),
    ]

    for num, solution in test_cases:

        print(bin(num))
        string = f"f({num}) = "
        string += " " * (25 - len(string))
        result = f(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
        print()
