"""
Fibonnaci numbers
"""
import time
from functools import lru_cache
from typing import Generator


def brute_force(n: int) -> int:
    if n < 2:
        return n
    return brute_force(n - 1) + brute_force(n - 2)


def memoization_recursion(n: int) -> int:
    memo = [None] * (n + 1)

    def f(n: int) -> int:
        if memo[n] is not None:
            return memo[n]
        if n < 2:
            return n
        memo[n] = f(n - 1) + f(n - 2)
        return memo[n]

    return f(n)


def memoization_iterative(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    memo = [0, 1] + [None] * (n - 2)

    for i in range(2, n):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n - 1] + memo[n - 2]


def iterative_memory_o1(n: int) -> int:
    if n < 2:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        curr, prev = curr + prev, curr

    return curr


@lru_cache(maxsize=None)
def python_cached(n: int) -> int:
    """
    Python has a built-it decorator for memoizing any
    function automatically: @functools.lru_cache().
    Each time the function with the decorator is called causes
    the return value to be cached. Upon future calls with the
    same argument, the previous return value for that argument
    is retrieved from the cache and returned.
    """
    if n < 2:
        return n
    return python_cached(n - 1) + python_cached(n - 2)


def generator(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        next, last = next + last, next
        yield next


if __name__ == "__main__":

    print("-" * 60)
    print("Fibonnaci numbers")
    print("-" * 60)

    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (8, 21),
    ]

    for n, solution in test_cases:

        result = brute_force(n)
        string = f"brute_force({n}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = memoization_recursion(n)
        string = f"memoization_recursion({n}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = memoization_iterative(n)
        string = f"memoization_iterative({n}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = iterative_memory_o1(n)
        string = f"iterative_memory_O(1)({n}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = python_cached(n)
        string = f"python_cached({n}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()

    print("\n>>> Generating Fibonacci numbers with a generator:")
    i = 0
    for n in generator(40):
        print(f"fib({i:>3}) = {n:>20}")
        i += 1

    print("\n\n>>> Performance tests:")
    for n in [37, 200, 9988]:

        if n < 40:
            t = time.time()
            print(f"\nBrute force: f({n}) = {brute_force(n)}")
            t = time.time() - t
            print(f"Computation time: {t*1e3:>8.0f} ms")

        if n < 250:
            t = time.time()
            print(f"\nMemoization - Recursion: f({n}) = {memoization_recursion(n)}")
            t = time.time() - t
            print(f"Computation time: {t*1e3:>8.0f} ms")

            t = time.time()
            print(f"\nMemoization - Python decorator: f({n}) = {python_cached(n)}")
            t = time.time() - t
            print(f"Computation time: {t*1e3:>8.0f} ms")

        t = time.time()
        print(f"\nMemoization - Iterative: f({n}) = {memoization_iterative(n)}")
        t = time.time() - t
        print(f"Computation time: {t*1e3:>8.0f} ms")

        print("----------")
