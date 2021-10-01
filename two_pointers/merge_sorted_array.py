"""
https://leetcode.com/problems/merge-sorted-array/
You are given two integer arrays nums1 and nums2, sorted in non-decreasing 
order, and two integers m and n, representing the number of elements in 
nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead 
be stored inside the array nums1. To accommodate this, nums1 has a 
length of m + n, where the first m elements denote the elements that 
should be merged, and the last n elements are set to 0 and should be ignored. 
nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. 
The 0 is only there to ensure the merge result can fit in nums1.

Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""

def overly_complex(nums1: list, nums2: list, m: int, n: int) -> None:
    # Modifies `a` in-place

    # if `nums2` is empty, `nums1` is already ok
    if n == 0:
        return

    total_length = m + n    
    # Initialize pointers for each list
    i1, i2 = 0, 0

    # Initialize queue to store the items to be moved
    # from `num1`
    queue = []

    # Loop over the items
    # print(queue, nums1, nums2)
    while i1 < total_length:
        # print('--', i1, i2, '--', m, n)

        if i1 >= m:
            # Pointer `i1` already out of the original `nums1` length
            if not len(queue) or (i2 < n and nums2[i2] < queue[0]):
                nums1[i1] = nums2[i2]
                i2 += 1

            else:
                nums1[i1] = queue.pop(0)

            i1 += 1

        elif len(queue):
            # There's some item in the `queue`
            if i2 >= n or (queue[0] < nums1[i1] and queue[0] < nums2[i2]):
                queue.append(nums1[i1])
                nums1[i1] = queue.pop(0)

            elif nums2[i2] < nums1[i1]:
                queue.append(nums1[i1])
                nums1[i1] = nums2[i2]
                i2 += 1

            i1 += 1

        elif nums2[i2] < nums1[i1]:
            # There's no queue and the current item in `nums2`
            # is smaller than the current item in `nums1`
            queue.append(nums1[i1])
            nums1[i1] = nums2[i2]
            i1 += 1
            i2 += 1

        else:
            # The current item in `nums1` is correct
            i1 += 1

        # print(queue, nums1, nums2)
    return


def merge(nums1: list, nums2: list, m: int, n: int) -> None:
    # Modifies `a` in-place
    
    # Start placing the largest numbers at the end of `num1`,
    # where we already have the space to store them,
    # and go to the left of both arrays searching for the next
    # largest numbers.
    # Use the array sizes `m` and `n` as pointers, 
    # decreasing their value as new numbers are put in their place.
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    
    while n > 0:
        nums1[n - 1] = nums2[n - 1]
        n -= 1   


if __name__ == "__main__":
    print('-' * 60)
    print('Merge sorted array')
    print('-' * 60)
    test_cases = [
        ([], [], 0, 0, []),
        ([0], [1], 0, 1, [1]),
        ([1], [], 1, 0, [1]),
        ([1, 0], [8], 1, 1, [1, 8]),
        ([3, 0], [2], 1, 1, [2, 3]),
        ([2, 3, 0], [4], 2, 1, [2, 3, 4]),
        ([2, 3, 0, 0], [4, 8], 2, 2, [2, 3, 4, 8]),
        ([3, 5, 0, 0], [4, 4], 2, 2, [3, 4, 4, 5]),
        ([1, 1, 2, 3, 0], [2], 4, 1, [1, 1, 2, 2, 3]),
        ([3, 4, 0], [2], 2, 1, [2, 3, 4]),
        ([3, 4, 0, 0], [1, 2], 2, 2, [1, 2, 3, 4]),
        ([3, 4, 8, 0, 0, 0, 0], [1, 1, 2, 5], 3, 4, [1, 1, 2, 3, 4, 5, 8])        
    ]

    for nums1, nums2, m, n, solution in test_cases:    

        arr_string = str(nums1) if len(nums1) < 7 else f'{str(nums1[:6])}...truncated...'
        string = f'merge({arr_string}, {nums2}) = '

        merge(nums1, nums2, m, n)
        
        string += str(nums1)
        string += ' ' * (80 - len(string))
        string += f'\tTest: {"OK" if nums1 == solution else "NOT OK"}'
        print(string)

    print()