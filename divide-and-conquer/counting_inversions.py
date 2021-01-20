"""
An inversion of an array is a pair of elements that are
“out of order,” meaning that the element that occurs earlier in the
array is bigger than the one that occurs later.

An array A that is in sorted order has no inversions.
You should convince yourself that the converse is also true: 
every array that is not in sorted order has at least one inversion.

Input: 
An array A of distinct integers.

Output: 
The number of inversions of A—the number of
pairs (i, j) of array indices with i<j and A[i] > A[j].

Time: O(n log(n))
"""
def brute_force(a: list):
    # time O(n^2)
    n = len(a)
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                count += 1
    return count


def merge_and_count_split_inv(c: list, d: list):
    """
    Returns the combined sorted list and the number of split inversions.
    
    Both `c` and `d` are already sorted.
    `c` is the first half of `a`, where every element x should be
    smaller than any element y in `d`.
    """
    i = j = split_inv = 0
    b = []
    for k in range(len(c) + len(d)):
        if i == len(c):
            b.append(d[j])
            j += 1
        elif j == len(d):
            b.append(c[i])
            i += 1
        elif c[i] < d[j]:
            b.append(c[i])
            i += 1
        else:
            # Count the remaining elements in `c` when d[j] < c[i]
            split_inv += len(c) - i
            b.append(d[j])
            j += 1
    return b, split_inv

def sort_and_count_inv(a: list):
    """
    Returns the combined sorted list and the number of inversions.
    Running time: O(n log(n))
    """
    # Base case
    n = len(a)
    if n == 0 or n == 1:
        return a, 0
    
    # Recursion ("divide" the problem in smaller ones)
    half = len(a) // 2
    c, left_inv = sort_and_count_inv(a[:half])
    d, right_inv = sort_and_count_inv(a[half:])
    b, split_inv = merge_and_count_split_inv(c, d)

    # Combine step
    return b, left_inv + right_inv + split_inv


if __name__ == '__main__':
    print('-' * 60)
    print('Count the number of inversions to sort an array')
    print('-' * 60)
    test_cases = [
        ([3, 2], 1),
        ([1, 2, 3], 0),
        ([3, 2, 1], 3),
        ([1, 3, 5, 2, 4, 6], 3),
        ([6, 5, 4, 3, 2, 1], 15), # n = 6, max_inversions = n * (n - 1) / 2 = 15
    ]
    
    for array, solution in test_cases:
        result = brute_force(array)
        string = f'   brute_force({str(array)}) = {result:2}'
        string += ' ' * (50 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = sort_and_count_inv(array)
        string = f'sort_and_count({str(array)}) = {result[1]:2}'
        string += ' ' * (50 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result[1] else "NOT OK"}\n')