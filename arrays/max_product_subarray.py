"""
https://leetcode.com/problems/maximum-product-subarray/
Given an integer array nums, find a contiguous non-empty 
subarray within the array that has the largest product, 
and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is 
not a subarray.
 
Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed 
to fit in a 32-bit integer.
"""

def brute_force(nums: list) -> bool:
    # O(n2)
    n = len(nums)
    current_max = nums[0]
    for i in range(n - 1):
        current_prod = nums[i]
        for j in range(i + 1, n):
            current_prod *= nums[j]
            if current_prod > current_max:
                current_max = current_prod
    return current_max

def efficient(nums: list) -> bool:
    # O(2n) = O(n)

    # Maximum individual number: O(n)
    res = max(nums)

    # Loop over the array: O(n)
    cur_max, cur_min = 1, 1
    for num in nums:
        
        # Edge case
        if num == 0:
            # Re-initialize `cur_max` and `cur_min`,
            # as if computing a different subarray
            cur_max, cur_min = 1, 1
            continue

        # Multiply previous prods by the current number
        temp_max = cur_max * num
        temp_min = cur_min * num
        
        # Re-evaluate the current max and min
        cur_max = max(temp_max, temp_min, num)
        cur_min = min(temp_max, temp_min, num)
        
        # Global maximum
        res = max(res, cur_max)

    return res
    
    
if __name__ == "__main__":
    print('-' * 60)
    print('Maximum product subarray')
    print('-' * 60)
    
    test_cases = [
        ([1], 1),
        ([1, 1], 1),
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
        ([2, 3,-2, 4, 1,-2], 96),
        ([-1, 2,-1, -3, 3, 5], 90),
        ([-50, 2,-1, -3, 3, 5], 100),
        ([-50, 2,-1, 0, 3, 5], 100),
        ([-50, 0,-1, 0, 3, 5], 15),
    ]
    
    for arr, solution in test_cases:
        
        result = brute_force(arr)        
        string = f'brute_force{arr} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = efficient(arr)        
        string = f'  efficient{arr} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()