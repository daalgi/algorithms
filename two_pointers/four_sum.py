"""
Given an array nums of n integers, return an array of all the unique 
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

def four_sum(nums: list, target: int) -> list:
    n = len(nums)
    
    # Edge case where the length of the list is less
    # than the needed to form a quadruplet
    if n < 4:
        return []
    
    # Sort the list to use a `two-pointer` strategy
    # O(nlogn)
    nums.sort()

    # Answer stored in a dictionary to quickly avoid 
    # adding duplicate quadruplets
    hashtable = dict()

    # Loop over the two first items of the quadruplets
    # O(n2)
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            # Store the sum of the first pair
            # to avoid already done computations
            fpair = nums[i] + nums[j]
            
            # Scan the remaining items
            # with the left and right pointers
            # in O(n) time complexity
            left, right = j + 1, n - 1
            while left < right:
                suma = fpair + nums[left] + nums[right]
                if suma > target:
                    right -= 1
                elif suma < target:
                    left += 1
                else:
                    quad = (nums[i], nums[j], nums[left], nums[right])
                    if quad not in hashtable:
                        hashtable[quad] = True
                    left += 1
                    right -= 1
    
    # Overall time complexity: O(n3)
    # Convert the hashtable with tuples as keys into
    # a list of lists for presentation purposes
    return list(list(k) for k in hashtable.keys())


if __name__ == "__main__":
    print('-' * 60)
    print('Four sum')
    print('-' * 60)
    test_cases = [
        ([], 8, []),
        ([0], 8, []),
        ([0, 1, 2, 3], 8, []),
        ([1, 0,-1, 0,-2, 2], 0, [[-2,-1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]])
    ]

    for nums, target, solution in test_cases:    

        arr_string = str(nums) if len(nums) < 7 else f'{str(nums[:6])}...truncated...'
        string = f'4sum({arr_string}, {target}) = '

        res = four_sum(nums, target)
        
        string += str(res)
        string += ' ' * (80 - len(string))
        string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string)

    print()