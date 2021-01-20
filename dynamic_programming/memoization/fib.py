def fib_slow(n: int):
    if n <= 2: return 1
    return fib_slow(n-1) + fib_slow(n-2)

def fib(n: int, memo: dict = None):
    if not memo: memo = {}
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


if __name__ == "__main__":
    from datetime import datetime
    import argparse
    parser = argparse.ArgumentParser(description='Optional app description')
    
    # Required positional argument
    parser.add_argument('pos_arg', type=int, 
        help='A required integer positional argument')
    n = parser.parse_args().pos_arg
    print('\n' + '-' * 10, f'fib({n})', '-' * 10)

    time = datetime.now()
    res = fib(n)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Dynamic programming, O(n) time:  {time:10.0f} ms, solution: {res}')
    
    time = datetime.now()
    res = fib_slow(n)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Brute force, O(2^n) time:        {time:10.0f} ms, solution: {res}\n')