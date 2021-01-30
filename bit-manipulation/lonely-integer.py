"""
SOLUTION 1: hashmap
O(n) time
O(n) space

SOLUTION 2: bitwise XOR operator
O(n) time
O(1) space

--> Main idea: 
Think of the array of integers bitwise, not as integers.
- Write the integers in binary, each one in a line.
- Perform the XOR operation on each column.
    - If the number of `1` is even, the result on the column is `0`.
    - If the number of `1` is odd, the result on the column is `1`.
    --> result is just the non-repeated integer.

Also, given the commutative and associative properties:
a1 ^ (a2 ^ a2) ^ (a3 ^ a3) ^ (a4 ^ a4) = a1
where a2 ^ a2 = 0, a1 ^ 0 = a1
"""

import operator, functools

def f(a: list):
    res = 0
    for i in a:
        res = res ^ i
    return res

def reduce_operator(a: list):
    return functools.reduce(operator.xor, a)

def reduce_int_method(a: list):
    return functools.reduce(int.__xor__, a)

def f_verbose(a: list):
    res = 0
    for i, elem in enumerate(a):
        string = f'index ={i:>3}\telement = {elem:>4}\t\tres_prev = {res:>4}'
        res = res ^ elem
        string += f'\t\tres = res_prev ^ element = {res:>4}'
        print(string)
    return res


if __name__ == "__main__":
    print('-' * 60)
    print('Identification of the only non-repeated integer')
    print('-' * 60)
    
    test_cases = [
        ([1, 2, 3, 1, 4, 2, 3], 4),
        ([3, 1, 1, 2, 4, 2, 3], 4),
        ([101018, 94324234, 94324234], 101018),
        ([32248, 987, 987, 32248, 88], 88),
        ([-1, 1, -2, -2, 1], -1)
    ]
    
    for array, solution in test_cases:
        
        array_string = str(array[:7])
        if len(array) > 7:
            array_string = array_string[:-1] + ', ...]'

        result = f(array)
        string = f'f({array_string}) = '
        string += ' ' * (50 - len(string))
        string += f'{result:>8.0f}'
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = reduce_operator(array)
        string = f'reduce_operator({array_string}) = '
        string += ' ' * (50 - len(string))
        string += f'{result:>8.0f}'
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = reduce_int_method(array)
        string = f'reduce_int_method({array_string}) = '
        string += ' ' * (50 - len(string))
        string += f'{result:>8.0f}'
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
        print()

    print()

    array = test_cases[0][0]
    print(f'>>> Verbose example:\nArray: {array}')
    res = f_verbose([*array])
    print(f'--> returns {res}')
    print()