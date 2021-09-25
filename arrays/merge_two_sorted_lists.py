def mergeTwoLists(l1: list, l2: list) -> list:
    n = len(l1)
    m = len(l2)
    i, j = 0, 0
    res = []
    for k in range(n + m):
        if i >= n:
            res.append(l2[j])
            j += 1
        elif j >= m:
            res.append(l1[i])
            i += 1
        elif l2[j] <= l1[i]:
            res.append(l2[j])
            j += 1
        elif l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
    return res


if __name__ == "__main__":
    print('-' * 60)
    print('Merge two sorted lists and return a sorted list')
    print('-' * 60)
    
    test_cases = [
        ([1, 2], [2], [1, 2, 2]),
        ([1, 6, 9], [2, 10], [1, 2, 6, 9, 10]),        
    ]
    
    for a, b, solution in test_cases:
        
        result = mergeTwoLists(a, b)
        string = f'merge{a, b} = '
        string += ' ' * (30 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')