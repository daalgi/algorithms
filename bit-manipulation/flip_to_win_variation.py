"""
CRACKING THE CODING INTERVIEW
5.3 Flip bit to win.
You have an integer and you can flip exactly one bit from
a 0 to a 1. Write code to find the length of the longest
sequence of 1s you could create.

VARIATION: 
You can flip one exactly one bit from a 0 to a 1 or viceversa.
Find the length of the longest sequence of 0s or 1s you
could create
"""


def brute_force(num: int) -> int:
    # Time complexity: O(b)
    # Space complexity: O(b)
    #   where b is the length of the sequence

    # List to keep track of the count of consecutive
    # repeated 0s or 1s
    count = []
    # Pointers to the current and previous bits
    cur, prev = None, None
    # Loop over the bits of the number
    while num > 0:
        # Current bit
        cur = num & 1
        # Compare current bit with the previous one
        if cur == prev:
            # If are equal, add one to the previous count
            count[-1] += 1
        else:
            # If they're not equal, add a new element
            # to the count list
            count.append(1)
        prev = cur
        num >>= 1

    # Find the longest sequence of 0s and 1s.
    # Keep track of the maximums
    single_max = count[0]
    combined_max = single_max
    # Loop over the elements of `count`
    for i in range(1, len(count)):

        if single_max < count[i]:
            # Update single maximum sequence
            single_max = count[i]

        if count[i - 1] == 1 and i > 1:
            # Update combined maximum sequence
            # if we flip one bit, only valid when
            # the previous count is exactly `1`
            current_combined_max = count[i - 2] + 1 + count[i]
            if combined_max < current_combined_max:
                combined_max = current_combined_max

    if len(count) > 1:
        # If there are multiple sequences
        return max(single_max + 1, combined_max)
    # If there's only one sequence
    return single_max


def optimal(num: int) -> int:
    # The Best Conceivable Runtime (BCR) is O(b), since
    # we'll always have to read through the sequence.
    # However, we can reduce the memory usage.
    # Instead of using an array to record the length of
    # each sequence, we can just compare it with the
    # immediately preceding sequence.
    pass


if __name__ == "__main__":
    print("-" * 60)
    print("Flip bit to win (variation)")
    print("-" * 60)

    test_cases = [
        (1775, 8),  # 11011101111
        (3, 2),  # 11
        (22, 4),  # 10110
        (8, 4),  # 1000
    ]

    for num, solution in test_cases:

        string = f"brute_force({num}) = "
        string += " " * (25 - len(string))
        result = brute_force(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
