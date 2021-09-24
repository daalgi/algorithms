from collections import defaultdict

"""
COUNT TRIPLETS
You are given an array and you need to find the number of
triplets of indices (i, j, k) such that the elements at those
indices are in geometric progression for a given common ratio r
and i < j < k.
"""
def brute_force(arr, r):
    # Method 1: brute force

    # arr should be sorted, since the definition of triplet
    # states that i < j < k (i.e. [4, 2, 1] isn't a triplet)

    count = 0
    n = len(arr)
    for i in range(n-2):
        if arr[i] == 1 or arr[i] % r == 0:
            #print(arr[i])
            for j in range(i+1, n-1):
                if arr[j] % r != 0 or arr[j] / arr[i] != r:
                    continue
                for k in range(j+1, n):
                    if arr[k] % r != 0 or arr[k] / arr[j] != r:
                        continue
                    count += 1
    return count
    
    
def hashtable(arr, r, verbose: bool = False):
    # Store the count of doubles in a hashtable
    doubles = defaultdict(int)
    # Store the count of integers in a hashtable
    integers = defaultdict(int)

    # Loop through the array in reverse order
    triplets = 0
    for x in arr[::-1]:

        # Current element multiplied by r and r2
        rx = r * x
        rrx = rx * r

        # If x is the 1st element of the triplet,
        # add it to the triplets count
        triplets += doubles[(rx, rrx)]

        # If x is the 2nd element of the triplet,
        # add it to the doubles count
        doubles[(x, rx)] += integers[rx]

        # If x is the 3rd element of the triplet,
        # add it to the integers count
        integers[x] += 1

        if verbose:
            print(f'x: {x}, rx: {rx}, rrx: {rrx}')
            print('Triplets:', triplets)
            print('Doubles:', doubles)
            print('Integers:', integers)
            print()

    return triplets


if __name__ == "__main__":
    print('-' * 60)
    print('Count the triplets following a geometric progression')
    print('-' * 60)
    test_cases = [
        ([1, 2, 2, 4], 2, 2),
        ([1, 3, 9, 9, 27, 81], 3, 6),
        ([1, 5, 5, 25, 125], 5, 4),
        ([1, 25, 5, 125, 5], 5, 0),
        ([1, 25, 5, 125, 5, 25], 5, 2),
        ([1] * 100, 1, 161700),
        ([1237] * 100000, 1, 166661666700000)
    ]
    for arr, r, solution in test_cases:
        if solution < 1e8:
            res = brute_force(arr, r)
            arr_string = str(arr) if len(arr) < 7 else f'{str(arr[:6])}...truncated...'
            string = f'Brute force: array = {arr_string}, r = {r}, valid triplets = {res}'
            string += ' ' * (80 - len(string))
            string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
            print(string)

        res = hashtable(arr, r)
        string = f'  Hashtable: array = {arr_string}, r = {r}, valid triplets = {res}'
        string += ' ' * (80 - len(string))
        string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string, '\n')

    print('\n>> Verbose example:')
    case = 0
    array = test_cases[case][0]
    num = test_cases[case][1]
    print('Array:', array)
    print('Number:', num, '\n')
    hashtable(array, num, verbose=True)