"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= first < second <= numbers.length.

Return the indices of the two numbers, index1 and index2, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3.
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2.

"""
def two_pointers(numbers: list, target: int) -> list:
    hashmap = dict()
    left = 0
    right = len(numbers) - 1
    while left < right:
        suma = numbers[left] + numbers[right]
        if suma > target:
            right -= 1
        elif suma < target:
            left += 1
        else:
            return [left+1, right+1]


if __name__ == "__main__":
    print('-' * 60)
    print('Two sum in a ascending sorted array')
    print('-' * 60)
    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([3, 8, 9], 11, [1, 2]),
        ([3, 4], 7, [1, 2]),
        ([1, 2, 3, 4], 7, [3, 4]),
        ([1, 3, 9, 11, 27, 81], 30, [2, 5]),
        ([1, 5, 10, 25, 125], 35, [3, 4]),
        ([1, 25, 35, 125, 155], 60, [2, 3]),
        ([1, 2, 3, 5, 8, 9], 7, [2, 4]),
    ]

    for arr, r, solution in test_cases:    
        res = two_pointers(arr, r)
        arr_string = str(arr) if len(arr) < 7 else f'{str(arr[:6])}...truncated...'
        string = f'Two pointers: array = {arr_string}, r = {r}, indices = {res}'
        string += ' ' * (80 - len(string))
        string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string)

    print()