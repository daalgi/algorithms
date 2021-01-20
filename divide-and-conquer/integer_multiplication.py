def digits(n: int):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

def power(x: int, y: int):
    if y == 0:
        return 1
    elif y == 1:
        return x
    return x * power(x, y-1)

def get_digit(num: int, index: int):
    return num // power(10, index) % 10

def split_at(num: int, index: int):
    # Index starting from the right
    return int(str(num)[:-index]), int(str(num)[-index:])

def third_grade_multiplication(a: int, b: int):
    suma = 0
    for i in range(digits(b)):
        digit = get_digit(b, i)
        suma += a * digit * power(10, i)
    return suma

def rec_int_mult(a: int, b:int):
    pass

def karatsuba_multiplication(a: int, b: int):
    if a < 10 or b < 10:
        return a * b
    
    # Size of the numbers
    m = min(digits(a), digits(b)) // 2

    # Split the digit sequences in the middle
    high1, low1 = split_at(a, m)
    high2, low2 = split_at(b, m)

    # Recursive calls to numbers approximately half the size
    z0 = karatsuba_multiplication(low1, low2)
    z1 = karatsuba_multiplication(low1 + high1, low2 + high2)
    z2 = karatsuba_multiplication(high1, high2)
    
    return z2 * power(10, m * 2) + (z1 - z2 - z0) * power(10, m) + z0


if __name__ == '__main__':

    test_cases = [
        (3, 4, 3 * 4),
        (11, 12, 11 * 12),
        (111, 12, 111 * 12),
        (123456, 33, 123456 * 33),
        (654, 987654, 654 * 987654),
    ]
    
    for a, b, solution in test_cases:
        result = third_grade_multiplication(a, b)
        string = f'third_grade_multiplication({a:6}, {b:6}) = {result:9}'
        string += ' ' * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = karatsuba_multiplication(a, b)
        string = f'  karatsuba_multiplication({a:6}, {b:6}) = {result:9}'
        string += ' ' * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}\n')