"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
def brute_force(nums: list, target: int) -> list:
    ref = 0
    n = len(nums)
    while ref < n - 1:
        i = ref + 1    
        while i < n:            
            if nums[ref] + nums[i] == target:
                return [ref, i]
            i += 1
        ref += 1

def hashmap(num: list, target: int) -> list:
    hashmap = dict() # value: index
    for i in range(len(num)):
        dif = target - num[i]
        if dif in hashmap:
            return [hashmap[dif], i]
        hashmap[num[i]] = i


if __name__ == "__main__":
    print('-' * 60)
    print('Two sum')
    print('-' * 60)
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 2, 4], 3, [0, 1]),
        ([1, 3, 9, 1, 27, 81], 36, [2, 4]),
        ([1, 5, 5, 25, 125], 126, [0, 4]),
        ([1, 25, 5, 125, 5], 26, [0, 1]),
        ([1, 25, 5, 3, 5, 1], 4, [0, 3]),
    ]
    
    for arr, r, solution in test_cases:
    
        res = brute_force(arr, r)
        arr_string = str(arr) if len(arr) < 7 else f'{str(arr[:6])}...truncated...'
        string = f'Brute force: array = {arr_string}, r = {r}, indices = {res}'
        string += ' ' * (80 - len(string))
        string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string)

        res = hashmap(arr, r)
        string = f'    Hashmap: array = {arr_string}, r = {r}, indices = {res}'
        string += ' ' * (80 - len(string))
        string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string, '\n')

    print()