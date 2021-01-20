# Euler problem 001

def sum_multiples_of(div: list, n: int, method: int = 1):
    """
    Sum of the multiples of the items in the list mult below n

    Keyword arguments:
    mult -- list of integers (length 2) with prime numbers to calculate the multiples of
    n -- integer below of which the multiples must be summed up

    Example:
    If we list all the natural numbers below 10 
    that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.
    """
    if len(div) != 2:
        raise NotImplementedError

    if method == 1:
        return sum_multiples_of_method1(div, n)
    if method == 2:
        return sum_multiples_of_method2(div, n)
    else:
        raise NotImplementedError

def sum_multiples_of_method1(div: list, n: int):
    """Iterative solution"""
    s = 0
    for i, d in enumerate(div):
        s += sum([num for num in range(d, n, d) 
            if not any(num % prev_d == 0 for prev_d in div[i+1:])])
    return s

def sum_multiples_of_method2(div: list, n: int):
    """
    Solution using the properties of the arithmetic progression:
    n (a0 + an)  / 2
    https://en.wikipedia.org/wiki/Arithmetic_progression
    """
    s = 0
    for d in div:
        remainder = (n - 1) % d
        an = n - 1 - remainder
        num_tot = an // d
        s += num_tot * (d + an) // 2
    
    # Subtract the repeated multiples
    # TODO: generalize with minimum common multiple 
    # of the combinations of values in the array
    d = div[0] * div[1]
    remainder = (n - 1) % d
    an = n - 1 - remainder
    num_tot = an // d
    s -= num_tot * (d + an) // 2
    
    return s


if __name__ == "__main__":
    numbers = [100]
    div = [3, 5]
    for n in numbers:
        s = sum_multiples_of(div, n, method=2)
        m = ','.join([str(i) for i in div])
        print(f'Sum of any multiple of [{m}] below {n} = {s}')