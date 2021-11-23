"""
CRACKING THE CODING INTERVIEW
5.3 Flip bit to win.
You have an integer and you can flip exactly one bit from
a 0 to a 1. Write code to find the length of the longest
sequence of 1s you could create.
"""


def optimal(num: int) -> int:
    # Time complexity: O(b)
    # Space complexity: O(1)
    #   where b is the length of the sequence

    if num == 0:
        # 
        return 1

    elif (num + 1) & num == 0:
        # If all bits are 1s, 
        # count the number of bits
        count = 0
        while num:
            count += 1
            num >>= 1
        return count

    # Keep track of the lenghts
    current_length = 0
    previous_length = 0
    max_length = 1
    while num:

        # Current bit
        cur = num & 1

        if cur == 1:
            # if the current bit is 1
            current_length += 1

        else:
            # If the current bit is 0

            # If the previous bit was 1 (2 = 10), make
            # the previous length equal to the current of 1s
            previous_length = 0 if num & 2 == 0 else current_length
            # Update the current length of 1s
            current_length = 0

        # Update maximum length so far
        max_length = max(previous_length + 1 + current_length, max_length)

        # Remove last bit of the number
        num >>= 1

    return max_length


if __name__ == "__main__":
    print("-" * 60)
    print("Flip bit to win")
    print("-" * 60)

    test_cases = [
        (1775, 8),  # 11011101111
        (3, 2),     # 11
        (22, 4),    # 10110
        (8, 2),     # 1000
    ]

    for num, solution in test_cases:

        string = f"optimal({num}) = "
        string += " " * (25 - len(string))
        result = optimal(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
