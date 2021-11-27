"""
CRACKING THE CODING INTERVIEW
5.4 Next number:
Given a positive integer, print the next smallest and the
next largest number that have the same number of 1 bits
in their binary representation.
"""


def brute_force(num: int) -> int:
    def number_of_1s(num: int) -> int:
        count = 0
        while num:
            num &= num - 1
            count += 1
        return count

    res = []
    num_ones = number_of_1s(num)

    cur = num
    while len(res) < 2:
        cur += 1
        if number_of_1s(cur) == num_ones:
            res.append(cur)

    # return tuple(res)
    return res[0]


def next_number(num: int) -> int:
    # Strategy: flip the rightmost non-trailing zero at p.
    # Then, clear all the bits to the right of p.
    # Finally, count the number of ones (n) up to p, and
    # set n 1s starting from the rightmost bit.
    # The result will be the next greater number
    # with the same number of 1s.

    # Temporary variable to perform shifts on the original
    # value of `num`
    temp = num

    # Number of trailing zeroes
    zeroes = 0

    # Loop until the rightmost one
    while temp & 1 == 0:
        zeroes += 1
        temp >>= 1

    # Number of ones until the rightmost non-trailing zero
    ones = 0

    # Loop until the rightmost non-trailing zero
    while temp & 1:
        ones += 1
        temp >>= 1

    # Position where a 0-bit will be flipped into a 1-bit,
    # that is, the rightmost non-trailing zero
    p = zeroes + ones

    # print(p, ones, zeroes)
    # print(bin(num))

    # Flip the rightmost non-trailing zero
    num |= 1 << p
    # print(bin(num))

    # # All zeros except for a 1 at position p
    # a = 1 << p
    # # All zeros, followed by p ones
    # b = a - 1
    # # All ones, followed by p zeros
    # mask = ~b
    # # Clear rightmost p bits
    # num &= mask

    # Which is equivalent to:
    # All zeros to the right of `p`
    num &= ~((1 << p) - 1)
    # print(bin(num))

    # Add the counted number of 1s, minus 1, at the right
    # # 0s with a 1 at position ones - 1
    # a = 1 << (ones - 1)
    # # 0s with 1s at positions 0 through `ones - 1`
    # b = a - 1
    # # Insert 1s at positions 0 through `ones - 1`
    # num |= b

    # which is equivalent to:
    # `ones - 1` 1s at the right
    num |= (1 << (ones - 1)) - 1
    # print(bin(num))

    return num


def prev_number(num: int) -> int:
    pass


if __name__ == "__main__":
    print("-" * 60)
    print("Next number")
    print("-" * 60)

    test_cases = [
        # (1, (2, 4)),  # 1 = 1, 2 = 10, 4 = 100
        # (3, (5, 6)),  # 3 = 11, 5 = 101, 6 = 110
        # (22, (25, 26)),  # 22 = 10110, 25 = 11001, 26 = 11010
        (1, 2),  # 1 = 1, 2 = 10
        (2, 4),  # 2 = 10, 4 = 100
        (4, 8),  # 4 = 100, 8 = 1000
        (3, 5),  # 3 = 11, 5 = 101
        (5, 6),  # 5 = 101, 6 = 110
        (7, 11),  # 7 = 111, 6 = 1011
        (22, 25),  # 22 = 10110, 25 = 11001
    ]

    for num, solution in test_cases:

        string = f"brute_force({num}) = "
        string += " " * (25 - len(string))
        result = brute_force(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f"next_number({num}) = "
        string += " " * (25 - len(string))
        result = next_number(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
