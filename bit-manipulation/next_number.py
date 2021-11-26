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

        # string = f"next_numbers({num}) = "
        # string += " " * (25 - len(string))
        # result = next_numbers(num)
        # string += str(result)
        # string += " " * (60 - len(string))
        # print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
