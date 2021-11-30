"""
MAX SUBARRAY SUM
https://en.wikipedia.org/wiki/Maximum_subarray_problem

In computer science, the maximum sum subarray problem is the task of 
finding a contiguous subarray with the largest sum, within a given 
one-dimensional array A[1...n] of numbers. Formally, the task is to 
find indices i and j with 0 <= i <= j < n, such that the sum is as large as possible.

For example, for the array of values [−2, 1, −3, 4, −1, 2, 1, −5, 4], 
the contiguous subarray with the largest sum is [4, −1, 2, 1], with sum 6.
"""
def brute_force(arr):
    raise NotImplementedError


def kadane(arr):
    # Kadane's algorithm
    # Keep track of maximum sum contiguous segment
    # among all positive segments.
    max_so_far = max_ending_here = 0

    for a in arr:
        max_ending_here += a

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    
    return max_so_far


if __name__ == "__main__":
    print('-' * 60)
    print('Maximum subarray sum')
    print('-' * 60)
    test_cases = [
        ([-1], 0),
        ([8], 8),
        ([2, 3], 5),
        ([1, 2, 3], 6),
        ([1, 0, -3, 4], 4),
        ([1, -2, 3, 4], 7),
        ([-2, 1, 3, -4, 5, 1, 0], 6),
        ([-1, -8, 3, 0, 9], 12),
        ([-2, -3, -1], 0),
        ([3, 7, 4, 6, 5], 25),
        ([3, 5, -7, 8, 10], 19),
        ([-2, -3, 4, -1, -2, 1, 5, -3], 7)
    ]
    
    for arr, solution in test_cases:        
        #brute_force_table(arr)
        arr_string = str(arr) 
        if len(arr) > 6:
            arr_string = str(arr[:6])
            arr_string = arr_string[:-1] + ', ...]'

        # res = brute_force_max(arr)
        # string = f'    Brute force: arr = {arr_string}, '
        # string += ' ' * (53 - len(string)) + f'max sum = {res}'
        # string += ' ' * (70 - len(string))
        # string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        # print(string)
        
        res = kadane(arr)
        string = f'Kadane: arr = {arr_string}, '
        string += ' ' * (53 - len(string)) + f'max sum = {res}'
        string += ' ' * (70 - len(string))
        string += f'\tTest: {"OK" if res == solution else "NOT OK"}\n'
        print(string)

    print()
    #tabulation(test_cases[5][0])