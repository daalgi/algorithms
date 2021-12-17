"""
https://leetcode.com/problems/combination-sum-iv/

Given an array of distinct integers nums and a target 
integer target, return the number of possible 
combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different 
combinations.

Example 2:
Input: nums = [9], target = 3
Output: 0

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000


Follow up: What if negative numbers are allowed in the 
given array? How does it change the problem? 
What limitation we need to add to the question to allow 
negative numbers?
"""


def bf_recursion(nums: list, target: int) -> int:
    # Brute force with recursion
    # Time complexity: O(2^n)

    # Base cases
    if target == 0:
        return 1
    if target < 0:
        return 0

    count = 0
    for num in nums:
        count += bf_recursion(nums, target - num)

    return count


def dp_recursion(nums: list, target: int) -> int:
    # Dynamic programming with recursion
    # Time complexity: O(n * target)
    # Space complexity: O(target)

    # Memoization to avoid repeated work
    memo = [None] * (target + 1)

    def recursion(nums: list, target: int, memo: list) -> int:
        # Recursive function

        # Base cases
        if target == 0:
            return 1
        if target < 0:
            return 0

        # Already computed solution
        if memo[target] is not None:
            return memo[target]

        # Initalize the element in `memo`
        memo[target] = 0

        # Loop over the numbers in the list
        for num in nums:
            memo[target] += recursion(nums, target - num, memo)

        return memo[target]

    return recursion(nums, target, memo)


def dp_iter(nums: list, target: int) -> int:
    # Dynamic programming with tabulation
    # Time complexity: O(n * target)
    # Space complexity: O(target)

    # Table to keep partial results
    table = [0] * (target + 1)
    table[0] = 1

    # Loop over up to the last element in the table (target + 1)
    for i in range(target + 1):
        # Loop over each number in the list `nums`
        for num in nums:
            if i >= num:
                # If the current target `i` can be reached
                # with the current number `num`,
                #
                table[i] += table[i - num]

    return table[-1]


if __name__ == "__main__":
    print("-" * 60)
    print("Combination sum IV")
    print("-" * 60)

    test_cases = [
        ([1, 2, 3], 4, 7),
        ([3, 5], 9, 1),
        ([6, 3], 13, 0),
        (list(i * 10 for i in range(1, 100)), 999, 0),
        (list(i * 10 for i in range(1, 10)), 998866, 0),
    ]

    for nums, target, solution in test_cases:

        print(nums)

        if target < 50:
            result = bf_recursion(nums, target)
            string = f" bf_recursion({target}) = "
            string += " " * (45 - len(string))
            string += str(result)
            string += " " * (60 - len(string))
            print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        if target < 1000:
            result = dp_recursion(nums, target)
            string = f" dp_recursion({target}) = "
            string += " " * (45 - len(string))
            string += str(result)
            string += " " * (60 - len(string))
            print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = dp_iter(nums, target)
        string = f"      dp_iter({target}) = "
        string += " " * (45 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
