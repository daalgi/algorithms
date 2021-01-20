def factorial(n: int):
    return 1 if n <= 0 else n * factorial(n-1)


if __name__ == "__main__":
    numbers = list(range(10))
    for n in numbers:
        print(f'{n:>3.0f}! = {factorial(n):>8.0f}')