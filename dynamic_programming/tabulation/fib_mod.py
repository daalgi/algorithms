"""
Implement a modified Fibonacci sequence using the following definition:
t(i+2) = t(i) + t(i+1)^2

Given three integers, t1, t2, and n, compute the nth term of 
the modified Fibonacci sequence.
"""
def fib_mod(t1: int, t2: int, n: int):
    table = [0] * n
    table[0] = t1
    table[1] = t2
    for i in range(2, n):
        table[i] = table[i-2] + table[i-1] * table[i-1]
    #print(table)
    return table[n-1]


if __name__ == "__main__":
    from datetime import datetime
    t1 = 0
    t2 = 5
    n = 7
    print('\n' + '-' * 10, f'fib_mod({t1, t2, n})', '-' * 10)    
    
    time = datetime.now()
    res = fib_mod(t1, t2, n)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'O(n) time:   {time:10.0f} ms, solution:', res)