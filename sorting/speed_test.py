from random import randint
import time

from sorting.bubble_sort import bubble_sort
from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort
from sorting.iterative_merge_sort import iterative_merge_sort
from sorting.count_sort import count_sort


SPACES = 73

print('-' * 60)
print('Sorting algorithms - Speed tests')
print('-' * 60)

sizes = [10, 100, 1000, int(1e4), int(1e5), int(1e6)]

for size in sizes:

    test_cases = [
        ([i for i in range(size+1)][::-1], 'Reversed array'),
        ([randint(0, size+1) for i in range(size+1)], 'Random integers'),
    ]
    print(f'\n>>> Array length: {size:.0E}\n')

    for array, info in test_cases:
        
        print(f'- {info}:')

        array_string = str(array[:6])
        if len(array) > 6:
            array_string = array_string[:-1] + ', ...]'

        if size < 3000:
            t = time.time()
            result = bubble_sort([*array])
            t = time.time() - t
            string = f'bubble_sort({array_string})'
            string += ' ' * (SPACES - len(string))
            print(string, f'\t\t{t * 1e3:>10.2f} ms')

            t = time.time()
            result = insertion_sort([*array])
            t = time.time() - t
            string = f'insertion_sort({array_string})'
            string += ' ' * (SPACES - len(string))
            print(string, f'\t\t{t * 1e3:>10.2f} ms')

        t = time.time()
        result = merge_sort([*array])
        t = time.time() - t
        string = f'merge_sort({array_string})'
        string += ' ' * (SPACES - len(string))
        print(string, f'\t\t{t * 1e3:>10.2f} ms')
        
        t = time.time()
        result = iterative_merge_sort([*array])
        t = time.time() - t
        string = f'iterative_merge_sort({array_string})'
        string += ' ' * (SPACES - len(string))
        print(string, f'\t\t{t * 1e3:>10.2f} ms')

        t = time.time()
        result = count_sort([*array])
        t = time.time() - t
        string = f'count_sort({array_string})'
        string += ' ' * (SPACES - len(string))
        print(string, f'\t\t{t * 1e3:>10.2f} ms')

        t = time.time()
        result = sorted([*array])
        t = time.time() - t
        string = f'python_sorted({array_string})'
        string += ' ' * (SPACES - len(string))
        print(string, f'\t\t{t * 1e3:>10.2f} ms')

        print()

print()