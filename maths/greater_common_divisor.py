"""
Greater common divisor - Euclidean algorithm
https://en.wikipedia.org/wiki/Euclidean_algorithm
"""
def gcd_euclidean_algorithm(x: int, y: int):
    if x <= 0 or y <= 0:
        return None

    if x == y:
        return x
    return gcd_euclidean_algorithm(abs(x-y), min(x, y))

def gcd(x: int, y: int):
    """
    x > y
    """
    if x < y:
        return gcd(y, x)
    
    if x <= 0 or y <= 0:
        return None

    while y:
        x, y = y, x % y

    return x

if __name__ == "__main__":
    print('\n' + '-' * 60)
    print('Greater common divisor - Euclidean algorithm')
    print('-' * 60)

    test_cases = [
        #((x, y), result)
        ((49, 56), 7),
        ((128, 2048), 128),
        ((57, 6), 3),
        ((17, 90), 1),
        ((0, 8), None),
        ((7, 4), 1),
        ((2, 1), 1),
        ((13, 5), 1)
    ]
    
    for (x, y), result in test_cases:

        res = gcd_euclidean_algorithm(x, y)
        string = f'gcd_euclidean{x, y} = {res}'
        string += ' ' * (60 - len(string))
        string += f'\tTest: {"OK" if res == result else "NOT OK"}'
        print(string)

        res = gcd(x, y)
        string = f'gcd_efficient{x, y} = {res}'
        string += ' ' * (60 - len(string))
        string += f'\tTest: {"OK" if res == result else "NOT OK"}\n'
        print(string)