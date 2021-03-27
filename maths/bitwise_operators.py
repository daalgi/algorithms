if __name__ == "__main__":
    print('-' * 60)
    print('Bitwise operations')
    print('-' * 60)
    
    test_cases = [
        (1, 1),
        (1, 2),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 1),
        (3, 2),
    ]
    
    for x, y in test_cases:
        
        print(f'{x:>3}   & {y:>3}   =   {x & y}')

        string = f'{x:>3}  << {y:>3}   =   {x << y}'
        string += ' ' * (30 - len(string)) + f'equivalent to {x} * 2^{y}'
        print(string)

        string = f'{x:>3}  >> {y:>3}   =   {x >> y}'
        string += ' ' * (30 - len(string)) + f'equivalent to floor({x} / 2^{y})'
        print(string)

        string = f'{x:>3}   ^ {y:>3}   =   {x ^ y}'
        print(string)

        string = f'{x:>3}   | {y:>3}   =   {x | y}'
        print(string)

        print()