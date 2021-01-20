"""
The function `fib(n)` takes in a number as an argument.

The function returns the n-th number of the Fibonacci sequence.

The 0th number of the sequence is 0.
the 1th number of the sequence is 1.

To generate the next number of the sequence, we sum the previous two.

--------------
Analysis:

time: O(n)
space: O(n)

"""
def fib(n: int):
    table = [0] * (n+1)
    table[1] = 1
    for i in range(n):
        table[i+1] += table[i]
        if i < n - 1:
            table[i+2] += table[i]

    return table[-1]


if __name__ == "__main__":
    from datetime import datetime
    n = 6
    print('\n' + '-' * 10, f'fib({n})', '-' * 10)    
    
    time = datetime.now()
    res = fib(n)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'O(n) time:   {time:10.0f} ms, solution:', res)
    
    print('\n' + '-' * 10, 'tests', '-' * 10)
    test_cases = [
        6,  # 8
        7,  # 13
        8,  # 21
        50  # 12586269025
    ]
    for n in test_cases:
        print(f'fib({n}) = {fib(n)}')