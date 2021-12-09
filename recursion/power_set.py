"""
CRACKING THE CODING INTERVIEW
8.4 Power set:
Write a method to return all subsets of a set.

https://leetcode.com/problems/subsets/
Given an integer array nums of unique elements, return all 
possible subsets (the power set).

The solution set must not contain duplicate subsets. 
Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""


def recursion(nums: int) -> int:
    # Each element has the "choice" of either being in there or not:
    # 2 * 2 * 2 * ... = 2^n
    # There are 2^n subsets, and each element will be contained
    # in 2^(n-1) subsets. Since there are `n` elements,
    # the total number of elements accross
    # all subsets is n * 2^(n-1). We won't be able to do better!
    # Time complexity: O(n2^n)
    # Space complexity: O(n2^n)

    # Size of the list to check the base case
    n = len(nums)

    # List to store the resulting subsets
    res = list()

    # List to store current subsets
    subset = list()

    def dfs(i: int) -> None:
        # Depth First Search recursive function

        # Base case
        if i >= n:
            # Append a copy of the current subset
            res.append(subset[:])
            return

        # Decission: include the ith element
        subset.append(nums[i])
        dfs(i + 1)

        # Decission: DO NOT include the ith element
        subset.pop()
        dfs(i + 1)

    # Call the recursive function passing the first index of `nums`
    dfs(0)
    return res


def iterative(nums: int) -> int:
    # Time complexity: O(n 2^n)
    # (generate all subsets and then copy them into res list)
    # Space complexity: O(n 2^n)
    # (number of solutions for subsets multiplied by the number
    # of elements to keep each subset)

    # Output result list, with the empty subset added
    res = [[]]
    # Loop over the elements of the list
    for num in nums:
        # Each iteration takes a new element into consideration
        # and generates new subsets from the existing ones
        res += [curr + [num] for curr in res]

    return res


def lexicographic(nums: int) -> int:
    # Lexicographic (Binary sorted) subsets
    # Map each subset to a bitmask of length `n`,
    # where `1` on the ith position in bitmask means
    # the presence of nums[i] in the subset,
    # and `0` means its absence.
    n = len(nums)
    res = []

    # We need integer numbers whose bit representation
    # goes from 00...00 to 11...11 (n bits)
    first = 2 ** n  # bin(first) = "0b 100..00" (n 0s)
                    # bin(first)[3:] = "00..00"
    last = 2 ** (n + 1)  # bin(last) = "0b1000..00"  (n+1 0s)
                         # bin(last)[3:] = "000..00"
    for i in range(first, last):
        bitmask = bin(i)[3:]
        res.append([nums[j] for j in range(n) if bitmask[j] == "1"])

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Power set")
    print("-" * 60)

    test_cases = [
        ([1, 2], [[1, 2], [1], [2], []]),
        ([1, 2, 3], [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]),
    ]

    for nums, solution in test_cases:

        print(nums)
        string = f"    recursion = "
        string += " " * (25 - len(string))
        result = recursion(nums)
        string += str(result)
        print(string)
        string = " " * 60
        test_ok = sorted(solution) == sorted(result)
        print(string, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')

        string = f"    iterative = "
        string += " " * (25 - len(string))
        result = iterative(nums)
        string += str(result)
        print(string)
        string = " " * 60
        test_ok = sorted(solution) == sorted(result)
        print(string, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')

        string = f"lexicographic = "
        string += " " * (25 - len(string))
        result = lexicographic(nums)
        string += str(result)
        print(string)
        string = " " * 60
        test_ok = sorted(solution) == sorted(result)
        print(string, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')

        print()
