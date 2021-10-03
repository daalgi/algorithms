"""
Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums 
except nums[i].

The product of any prefix or suffix of nums is guaranteed to 
fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without 
using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed 
to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space 
complexity analysis.)

"""
def solve(nums: list) -> list:
    n = len(nums)
    ans = [None] * n
    ans[n-1] = 1
    for i in range(n-2, -1, -1):
        ans[i] = nums[i+1] * ans[i+1]
    
    prod = 1
    for i in range(1, n):
        prod *= nums[i-1]
        ans[i] *= prod

    return ans

if __name__ == "__main__":
    print('-' * 60)
    print('Product of array except self')
    print('-' * 60)
    
    test_cases = [
        ([1, 2], [2, 1]),
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),        
    ]
    
    for arr, solution in test_cases:
        
        result = solve(arr)        
        string = f'solve{arr} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
    # solve(test_cases[0][0])    