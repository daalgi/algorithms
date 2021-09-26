def brute_force(height: list) -> int:
    maxi = 0
    n = len(height)
    for i in range(n-1):
        for j in range(i+1, n):
            q = min(height[i], height[j]) * (j - i)
            if q > maxi:
                maxi = q
    return maxi

def two_pointers(height: list) -> int:
    maxi, left, right = 0, 0, len(height)-1
    while left < right:
        q = min(height[left], height[right]) * (right - left)
        if q > maxi:
            maxi = q
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxi

if __name__ == "__main__":
    print('-' * 60)
    print('Container with most water')
    print('-' * 60)
    
    test_cases = [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1),
        ([4,3,2,1,4], 16),
        ([1,2,1], 2)
    ]
    
    for a, solution in test_cases:
        
        string = f'brute_force{a} = '
        result = brute_force(a)
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f'two_pointers{a} = '
        result = two_pointers(a)
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()

