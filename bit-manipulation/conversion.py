"""
CRACKING THE CODING INTERVIEW
5.6 Conversion
Write a function to determine the number of bits you
would need to flip to convert integer A to integer B.

Example:
Input: 29 (or: 11101), 15 (or: 01111)
Output: 2
"""


def bit_by_bit(a: int, b: int) -> int:
    # Check bit by bit and keep track of the
    # number of non-equal bits
    count = 0
    while a or b:
        a_bit = a & 1
        b_bit = b & 1
        if a_bit != b_bit:
            count += 1

        a >>= 1
        b >>= 1

    return count


def xor(a: int, b: int) -> int:
    # Count the number of 1s in a ^ b
    count = 0
    c = a ^ b
    while c:
        count += c & 1
        c >>= 1
    return count


def remove_least_significant_bit(a: int, b: int) -> int:
    # Count the number of 1s in a ^ b,
    # but instead of checking bit-by-bit, we can
    # continuously flip the least significant bit and count
    # how long it takes `c` to reach 0.
    count = 0
    c = a ^ b
    while c:
        count += 1
        # Remove the trailing zeroes
        c &= c - 1
    return count


if __name__ == "__main__":
    print("-" * 60)
    print("Conversion")
    print("-" * 60)

    test_cases = [
        (1, 2, 2),
        (2, 4, 2),
        (3, 8, 3),
        (29, 15, 2),
    ]

    for a, b, solution in test_cases:

        print("a =", a, "=", bin(a))
        print("b =", b, "=", bin(b))
        string = f"bit_by_bit{a, b} = "
        string += " " * (25 - len(string))
        result = bit_by_bit(a, b)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f"       xor{a, b} = "
        string += " " * (25 - len(string))
        result = xor(a, b)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f"remove_lsb{a, b} = "
        string += " " * (25 - len(string))
        result = remove_least_significant_bit(a, b)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
