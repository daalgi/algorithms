"""
CRACKING THE CODING INTERVIEW
5.2 Binary to string
Given a real number between 0 and 1 (e.g., 0.72) that is passed
in as a double, print the binary representation.
If the number cannot be represented accurately in binary with
at most 32 characters, print "ERROR".
"""


def binary(num: float) -> str:
    # Problem statement limits
    if num <= 0 or num >= 1:
        return "ERROR"

    res = []
    while num > 0:

        if len(res) >= 32:
            # If the binary representation needs
            # more than 32 bits, return an error
            return "ERROR"

        r = num * 2
        if r >= 1:
            res.append("1")
            num = r - 1
        else:
            res.append("0")
            num = r

    return "." + "".join(res)


if __name__ == "__main__":
    print("-" * 60)
    print("Binary to string")
    print("-" * 60)

    test_cases = [
        (0.5, ".1"),
        (0.25, ".01"),
        (0.625, ".101"),
        (0.33, "ERROR"),
        (0.123456, "ERROR"),
    ]

    for num, solution in test_cases:

        string = f"binary({num}) = "
        string += " " * (35 - len(string))
        result = binary(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
