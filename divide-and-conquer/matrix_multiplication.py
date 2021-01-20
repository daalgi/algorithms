"""
Suppose X and Y are nxn matrices of integers —n2 entries in each.
In the product Z = X·Y, the entry z_ij in the ith row and jth column
of Z is defined as the dot product of the ith row of X and the jth
column of Y.

Input: two nxn integer matrices.

Output: the matrix product X · Y

The input size is proportional to n2, the number of entries in each of
X and Y. Since we presumably have to read the input and write out
the output, the best we can hope for is an algorithm with running
time O(n2) —linear in the input size, and quadratic in the dimension.

"""
def brute_force(x: list, y: list):
    # time O(n^3)
    n = len(x)
    z = []
    for i in range(n):
        z.append([])
        for j in range(n):
            z[i].append(0)
            for k in range(n):
                z[i][j] += x[i][k] * y[k][j]
    return z


def recursive_mat_mult(x: list, y: list):
    """
    Strassen algorithm.

    Returns the matrix multiplication Z = X · Y.
    Running time: subcubic O(n2.8074)
    """
    # TODO
    # Base case
    n = len(a)
    if n == 1:
        return x[0][0] * y[0][0]
    
    # Recursion ("divide" the problem in smaller ones)
    half = len(a) // 2
    

    # Combine step
    raise NotImplementedError


if __name__ == '__main__':
    print('-' * 60)
    print('Count the number of inversions to sort an array')
    print('-' * 60)
    test_cases = [
        ([[3, 2], [2, 5]], [[1, 0], [0, 1]], [[3, 2], [2, 5]]),
        ([[3, 2], [2, 5]], [[1, 1], [2, 1]], [[7, 5], [12, 7]]),
    ]
    
    case = 1
    for x, y, solution in test_cases:
        result = brute_force(x, y)
        string = f'   brute_force({case}) = {str(result)}'
        string += ' ' * (50 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
        """
        result = recursive_mat_mult(x, y)
        string = f'sort_and_count({str(array)}) = {result[1]:2}'
        string += ' ' * (50 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result[1] else "NOT OK"}\n')
        """
        case += 1