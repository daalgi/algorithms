def grid_traveler_slow(m: int, n: int):
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    return grid_traveler_slow(m-1, n) + grid_traveler_slow(m, n-1)

def grid_traveler(m: int, n: int, memo: dict = None):
    if not memo: memo = {}
    if (m, n) in memo: return memo[m, n]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    memo[m, n] = grid_traveler(m-1, n, memo) + grid_traveler(m, n-1, memo)
    return memo[m, n]


if __name__ == "__main__":
    from datetime import datetime
    import argparse
    parser = argparse.ArgumentParser(description='Optional app description')
    
    # Required positional argument
    parser.add_argument('m', type=int, 
        help='A required integer positional argument')
    parser.add_argument('n', type=int, 
        help='A required integer positional argument')
    m, n = parser.parse_args().__dict__.values()
    
    print('\n' + '-' * 10, f'grid_traveler{m, n}', '-' * 10)

    time = datetime.now()
    res = grid_traveler(m, n)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Dynamic programming, O(m*n) time: {time:10.0f} ms, solution: {res}')    
    
    time = datetime.now()
    res = grid_traveler_slow(m, n)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Brute force, O(2^(m+n)) time:     {time:10.0f} ms, solution: {res}\n')