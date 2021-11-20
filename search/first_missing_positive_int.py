"""
https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array nums, return the smallest 
missing positive integer.

You must implement an algorithm that runs in O(n) time and 
uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
"""


def search(array: list, verbose: bool = False) -> int:
    """
    Strategy: re-organize the elements of the array
    such as the value of a given element corresponds with
    its index+1 in the array. Then find the first element
    that vale != index + 1
    """

    n = len(array)

    # Loop over the elements of the array and change their
    # location when needed
    if verbose:
        print(array)

    for i in range(n):
        # current = array[i]
        if verbose:
            print("\nIndex:", i)

        iter = 0
        val = array[i]
        while 0 < val <= n and val != array[val - 1] and iter < 5:

            if verbose:
                print(">> Swap:", i, "\t", val, "<-->", array[val - 1])
                print(array)

            array[i], array[val - 1] = array[val - 1], val
            val = array[i]

            if verbose:
                print(array)

    # Loop over the modified array
    for i in range(n):
        if array[i] != i + 1:
            # The first time value != index + 1
            # indicates that index + 1 is the
            # missing positive integer
            return i + 1

    # If no value was returned, all the positive integers
    # are in the expected place, so the missing positive integer
    # is n + 1
    return n + 1


if __name__ == "__main__":
    print("-" * 60)
    print("First missing positive int")
    print("-" * 60)

    test_cases = [
        ([1], 2),
        ([8], 1),
        ([1, 2], 3),
        ([2, 1], 3),
        ([2, 1, 3], 4),
        ([2, 1, 2], 3),
        ([2, 1, 1, 2, 1], 3),
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([-1, 4, 2, 1, 9, 10], 3),
    ]

    for array, solution in test_cases:

        array_string = str(array)
        if len(array_string) > 20:
            array_string = array_string[:20] + "...]"

        result = search([*array])
        string = f"search{array_string} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

    case = -1
    array = test_cases[case][0]
    print("\n\n>>>Verbose example:")
    search(array, verbose=True)
