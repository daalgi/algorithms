"""
Check if an integer is even using bitwise operators: XOR, AND, OR

"""
def using_xor(a: int, verbose: bool = False):
    if verbose:
        bit = a ^ 1
        string = f'{a:>8} ^ 1 = {bit}\t'
        if bit < a:
            string += f'> {a:>8} --> not even'
        else:
            string += f'< {a:>8} --> even'
        print(string)

    if a ^ 1 == a + 1:
        return True
    return False

def using_and(a: int, verbose: bool = False):
    if verbose:
        bit = a & 1
        string = f'{a:>8} & 1 = {bit}\t'
        if bit == 1:
            string += f'= {1:>8} --> not even'
        else:
            string += f'= {0:>8} --> even'
        print(string)

    if a & 1 == 0:
        return True
    return False

def using_or(a: int, verbose: bool = False):
    if verbose:
        bit = a | 1
        string = f'{a:>8} | 1 = {bit}\t'
        if bit == a:
            string += f'= {a:>8} --> not even'
        else:
            string += f'> {a:>8} --> even'
        print(string)

    if a | 1 > a:
        return True
    return False


if __name__ == "__main__":
    print('-' * 60)
    print('Checking if an integer is even with the bitwise XOR operator')
    print('-' * 60)
    
    test_cases = [
        (1, False),
        (2, True),
        (3, False),
        (88, True),
        (12345, False)
    ]
    
    for a, solution in test_cases:
        
        result = using_xor(a)
        string = f'using_xor({a}) = '
        string += ' ' * (20 - len(string))
        string += f'{"Even" if result else "Not even"}'
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = using_and(a)
        string = f'using_and({a}) = '
        string += ' ' * (20 - len(string))
        string += f'{"Even" if result else "Not even"}'
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = using_or(a)
        string = f'using_or({a}) = '
        string += ' ' * (20 - len(string))
        string += f'{"Even" if result else "Not even"}'
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
        
        print()

    print()

    for a, _ in test_cases[-2:]:

        print(f'>>> Verbose example using XOR (^):\nInteger: {a}')
        res = using_xor(a, verbose=True)
        print()

        print(f'>>> Verbose example using AND (&):\nInteger: {a}')
        res = using_and(a, verbose=True)
        print()

        print(f'>>> Verbose example using OR (|):\nInteger: {a}')
        res = using_or(a, verbose=True)
        print()