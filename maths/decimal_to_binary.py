def decimal_to_binary(n: int):
    """
    Transforms a possitive decimal integer into a binary number
    n -- possitive integer number
    """
    if n == 0:
        return '0'
    b = []
    while n > 0:
        remainder = n % 2
        n = n // 2
        b.append(str(remainder))
    return ''.join(b[::-1])


def max_number_of_consecutive_ones(binary: str):
    """
    Returns the maximum number of consecutive ones in a binary number
    """
    return max([len(i) for i in binary.split('0')])


if __name__ == "__main__":
    numbers = list(range(10)) + list(range(20,200,20))
    for n in numbers:
        b = decimal_to_binary(n)
        res = f'{" " * (6-len(str(n)))}({n})_10 = ({b})_2{" " * (10-len(b))}'
        res += f' --> max consecutive ones = {max_number_of_consecutive_ones(b)}'
        print(res)