"""
MAX ARRAY SUM
https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

Given an array of integers, find the subset of non-adjacent elements with the maximum sum. 
Calculate the sum of that subset. It is possible that the maximum sum is 0, 
the case when all elements are negative.

For example, given an array arr = [-2, 1, 3, -4, 5] we have the following possible subsets. 
These exclude the empty subset and single element subsets which are also valid.

Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8

Our maximum subset sum is 8. Note that any individual element is a subset as well.

As another example, arr = [-2, -3, -1]. 
In this case, it is best to choose no element: return 0.

Sample Input 0
5
3 7 4 6 5

Sample Output 0
13

Explanation 0
Our possible subsets are:
[3, 4, 5]
[3, 4]
[3, 6]
[3, 5]
[7, 6]
[7, 5]
[4, 5]

The largest subset sum is 13 from subset [3, 4, 5]
"""
def brute_force_combinations(arr):
    n = len(arr)
    table = []
    for i in range(n-2):

        # Skip the current `i` if the current integer not positive
        if arr[i] <= 0:
            continue
        
        # Add the reference single ith-element
        table.append([arr[i]])

        # Loop through the remaining elements of the array from i+2
        for j in range(i + 2, n):

            # Compute the maximum length of the possible combinations
            subarr_length = n - j
            length_max = subarr_length // 2
            if subarr_length % 2 != 0:
                length_max += 1

            # Add combinations with different lengths
            for length in range(1, length_max+1):
                table.append([arr[i]] + arr[j:j+length*2+1:2])

    return table

def brute_force_max(arr):
    if len(arr) < 3:
        return max(*arr, 0)

    combinations = brute_force_combinations(arr)
    return max([sum(c) for c in combinations] + [0])


def brute_force_eff(arr):
    n = len(arr)
    table = [0] * n
    for i in range(n):

        if arr[i] <= 0:
            continue
        
        table[i] = arr[i]

        if i > n - 2:
            continue

        for j in range(i + 2, n):

            # Compute the maximum length of the possible combinations
            subarr_length = n - j
            length_max = subarr_length // 2
            if subarr_length % 2 != 0:
                length_max += 1

            # Check if the possible combinations with different lengths
            # can add a greater sum than the current for the ith element
            # starting from the jth element
            for length in range(1, length_max+1):
                suma = sum(arr[j:j+length*2+1:2])
                if arr[i] + suma > table[i]:
                    table[i] = arr[i] + suma

    #print(table)
    return max(*table, 0)


def tabulation(arr):
    n = len(arr)
    if n < 3:
        return max(*arr, 0)

    table = [0] * n
    table[0] = max(arr[0], 0)
    maxi = max(table[0], arr[1])
    table[1] = maxi

    for i in range(2, n):
        table[i] = max(
            table[i-2] + arr[i],
            maxi
        )
        if table[i] > maxi:
            maxi = table[i]

    #print(table)
    return max(table[-1], 0)


def recursion(arr: list):
    n = len(arr)

    # Base case
    if n < 3:
        return max(*arr, 0)
    elif n == 3:
        return max(arr[0] + arr[2], *arr)

    return recursion(arr, start)
    

if __name__ == "__main__":
    print('-' * 60)
    print('Maximum sum of non-adjacent elements of an array')
    print('-' * 60)
    test_cases = [
        ([-1], 0),
        ([8], 8),
        ([2, 3], 3),
        ([1, 2, 3], 4),
        ([1, 2, 3, 4], 6),
        ([1, -2, 3, 4], 5),
        ([-2, 1, 3, -4, 5, 1, 0], 8),
        ([-1, -8, 3, 0, 9], 12),
        ([-2, 1, 3, -4, 5], 8),
        ([-2, -3, -1], 0),
        ([3, 7, 4, 6, 5], 13),
        ([2, 1, 5, 8, 4], 11),
        ([3, 5, -7, 8, 10], 15),
        ([1] * 10, 5),
        ([1] * 20, 10),
        ([1] * 250, 125),  # starts to be slow for brute_force and tabulation
        ([1] * 2000000, 1000000) # only O(n) algorithms!
    ]
    
    for arr, solution in test_cases:        
        #brute_force_table(arr)
        arr_string = str(arr) 
        if len(arr) > 6:
            arr_string = str(arr[:6])
            arr_string = arr_string[:-1] + ', ...]'

        if len(arr) < 100:
            res = brute_force_max(arr)
            string = f'    Brute force: arr = {arr_string}, '
            string += ' ' * (53 - len(string)) + f'max sum = {res}'
            string += ' ' * (70 - len(string))
            string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
            print(string)
        
        if len(arr) < 250:
            res = brute_force_eff(arr)        
            string = f'Brute force eff: arr = {arr_string}, '
            string += ' ' * (53 - len(string)) + f'max sum = {res}'
            string += ' ' * (70 - len(string))
            string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
            print(string)

        # res = recursion(arr)        
        # string = f'  Recursion: arr = {arr_string}, '
        # string += ' ' * (53 - len(string)) + f'max sum = {res}'
        # string += ' ' * (70 - len(string))
        # string += f'\tTest: {"OK" if res == solution else "NOT OK"}\n'
        # print(string)

        res = tabulation(arr)
        string = f'     Tabulation: arr = {arr_string}, '
        string += ' ' * (53 - len(string)) + f'max sum = {res}'
        string += ' ' * (70 - len(string))
        string += f'\tTest: {"OK" if res == solution else "NOT OK"}\n'
        print(string)
    print()
    #tabulation(test_cases[5][0])