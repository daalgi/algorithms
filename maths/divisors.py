def divisors(n):
    # get factors and their counts
    factors = {}
    nn = n
    i = 2
    while i*i <= nn:
        while nn % i == 0:
            factors[i] = factors.get(i, 0) + 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = factors.get(nn, 0) + 1

    primes = list(factors.keys())

    # generates factors from primes[k:] subset
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k+1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                # prime_to_i iterates prime**i values, i being all possible exponents
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime

    # in python3, `yield from generate(0)` would also work
    for factor in generate(0):
        yield factor

if __name__ == "__main__":
    print('\n' + '-' * 60)
    print('Greater common divisor - Euclidean algorithm')
    print('-' * 60)

    test_cases = [
        #((x, y), result)
        (6, [1, 2, 3, 6]),
        (8, [1, 2, 4, 8]),
        (49, [1, 7, 49]),
        (90, [1, 2, 3, 6, 9, 18, 5, 10, 15, 30, 45, 90]),
        # ((0, 8), None),
        # ((7, 4), 1),
        # ((2, 1), 1)
        #((13, 5), 1)
    ]
    
    for num, result in test_cases:

        res = list(divisors(num))
        string = f'divisors({num}) = {str(res)}'
        string += ' ' * (60 - len(string))
        string += f'\tTest: {"OK" if res == result else "NOT OK"}'
        print(string)
    print()