"""
CRACKING THE CODING INTERVIEW
5.7 Pairwise swap
Write a program to swap odd and even bits in an integer
with as few instructions as possible (e.g., bit 0 and bit 1
are swapped, bit 2 and bit 3 are swapped, and so on).
"""


def swap(a: int) -> int:
    # 1) Create two masks:
    # - A mask for the pair numbers: 0xaa = 10101010 (8 bits)
    # - A mask for the even numbers: 0x55 = 01010101 (8 bits)
    # 2) Perform the AND bit operation `a & mask` to
    # extract only the pair and even numbers
    # 3) Shift operations:
    # - a_pair_bits >> 1
    # - a_odd_bits << 1
    # 4) "Join" the result with an OR bit operation
    # a_pair_shifted | b_odd_shifted
    return ((a & 0xAAAAAAAA) >> 1) | ((a & 0x5555555555) << 1)


if __name__ == "__main__":
    print("-" * 60)
    print("Pairwise swap")
    print("-" * 60)

    test_cases = [
        (1, 2),
        (2, 1),
        (3, 3),
        (7, 11),
        (29, 46),
        (761622921, 513454662),
    ]

    for a, solution in test_cases:

        string = f"swap({a}) = "
        string += " " * (25 - len(string))
        result = swap(a)
        string += str(result)
        string += " " * (60 - len(string))
        print(f"     a = {a:>4} = {bin(a)}")
        print(f"result = {result:>4} = {bin(result)}")
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
