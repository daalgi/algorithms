"""
https://leetcode.com/problems/3sum/
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

"""
def three_sum(nums: list) -> list:
    n = len(nums)
    if n < 2:
        return []

    triplets = []

    # Sort the numbers to enable a more 
    # efficient algorithm
    # (time complexity O(nlogn))
    nums.sort()

    # Auxiliary variables
    ref = 0
    prev_num = None

    # Loop through the negative numbers
    while nums[ref] <= 0 and ref < n - 2:

        # If the reference number is equal to the previous,
        # skip the iteration to avoid duplicate triplets
        if nums[ref] == prev_num:
            ref += 1
            continue

        # Look for the two remaining numbers
        # using two pointers
        left, right = ref + 1, n - 1
        while left < right:
            suma = nums[ref] + nums[left] + nums[right]
            if suma > 0:
                right -= 1
            elif suma < 0:
                left += 1
            else:
                triplets.append([nums[ref], nums[left], nums[right]])
                left += 1
                # Avoid repeated numbers
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

        # print('Update', left, right)
        # Update variables for next iter
        prev_num = nums[ref]
        ref += 1        
    
    return triplets

if __name__ == "__main__":
    print('-' * 60)
    print('Three sum')
    print('-' * 60)
    test_cases = [
        ([], []),
        ([0], []),
        ([-1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-3, 3, 4, -3, 1, 2], [[-3, 1, 2]]),
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([-5,2,4,1,-2,5,0,8,3,-1], [[-5,0,5],[-5,1,4],[-5,2,3],[-2,-1,3],[-2,0,2],[-1,0,1]])
    ]

    for nums, solution in test_cases:    

        arr_string = str(nums) if len(nums) < 7 else f'{str(nums[:6])}...truncated...'
        string = f'3sum({arr_string}) = '

        res = three_sum(nums)
        
        string += str(res)
        string += ' ' * (80 - len(string))
        string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string)

    print()