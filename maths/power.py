def brute_force(a: int, b: int):
    res = a
    while b > 1:
        res *= a
        b -= 1
    return res

def binary_exp(a: int, b: int):
    res = 1
    while b > 0:
        if b & 1:       # equivalent to "if b is odd"
            res *= a
        a *= a          # when b is even
        b >>= 1         # equivalent to floor(b / 2^1)
    return res

if __name__ == "__main__":
    print('-' * 60)
    print('Exponentiation')
    print('-' * 60)
    
    test_cases = [
        (2, 2, 4),
        (2, 3, 8),
        (3, 3, 27),
        (3, 4, 81)
    ]
    
    for a, b, solution in test_cases:
        
        result = brute_force(a, b)
        string = f'brute_force{a, b} = '
        string += ' ' * (30 - len(string))
        string += f'{result:>5.0f}'
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = binary_exp(a, b)
        string = f'binary_exp{a, b} = '
        string += ' ' * (30 - len(string))
        string += f'{result:>5.0f}'
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
        print()