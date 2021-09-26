"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element 
appears only once. The relative order of the elements should 
be kept the same.

Since it is impossible to change the length of the array in 
some languages, you must instead have the result be placed 
in the first part of the array nums. More formally, if there 
are k elements after removing the duplicates, then the first 
k elements of nums should hold the final result. It does not 
matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do 
this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two 
elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k 
(hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five 
elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k 
(hence they are underscores).
"""
def remove_duplicates(nums: list) -> int:
    n = len(nums)
    if n == 0:
        return 0, []
    # Keep track of the unique items index
    k = 1
    temp = nums[0]
    # Loop over the items of the list
    for i in range(1, n):
        if nums[i] != temp:
            if k < i:
                nums[k] = nums[i]
            # Update next iter
            k += 1
            temp = nums[i]
    
    # Slice the original list
    nums = nums[:k]
    return k, nums


if __name__ == "__main__":
    print('-' * 60)
    print('Remove duplicates from sorted array')
    print('-' * 60)
    
    test_cases = [
        ([], 0, []),
        ([0, 1], 2, [0, 1]),
        ([0, 0, 0, 1], 2, [0, 1]),
        ([0, 0, 1, 1, 2, 2, 2], 3, [0, 1, 2]),
        ([0, 1, 1, 1, 1, 2], 3, [0, 1, 2]),        
    ]
    
    for a, sol_k, sol_nums in test_cases:
        
        string = f'sol{a} = '
        k, nums = remove_duplicates(a)        
        string += ' ' * (35 - len(string))
        string += str(k) + " " + str(nums)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if k == sol_k and nums == sol_nums else "NOT OK"}')