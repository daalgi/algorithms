"""
Given an integer array nums and an integer val, remove all occurrences of 
val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array 
nums. More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. It does not 
matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying 
the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements 
of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
def remove_element(nums: list, val: int) -> int:
    n = len(nums)
    if n == 0:
        return 0, []
    # Keep track of the unique items index
    k = 0
    # Loop over the items of the list
    for i in range(n):
        if nums[i] != val:
            nums[k] = nums[i]
            # Update next iter
            k += 1
    
    # Slice the original list
    nums = nums[:k]
    return k, nums


if __name__ == "__main__":
    print('-' * 60)
    print('Remove element')
    print('-' * 60)
    
    test_cases = [
        ([], 0, 0, []),
        ([0, 1], 2, 2, [0, 1]),
        ([0, 2, 0, 1], 2, 3, [0, 0, 1]),
        ([0, 0, 1, 1, 2, 2, 2], 0, 5, [1, 1, 2, 2, 2]),
        ([0, 1, 1, 1, 1, 2], 1, 2, [0, 2]),
        ([0, 1, 0, 2, 0], 0, 2, [1, 2])
    ]
    
    for nums, val, sol_k, sol_nums in test_cases:
        
        string = f'remove{nums, val} = '
        k, nums = remove_element(nums, val)        
        string += ' ' * (35 - len(string))
        string += str(k) + " " + str(nums)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if k == sol_k and nums == sol_nums else "NOT OK"}')