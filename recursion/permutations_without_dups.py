"""
CRACKING THE CODING INTERVIEW
8.7 Permutations without Dups (without duplicates):
Write a method to compute all permutations of a string
of unique characters.


https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the 
possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List
import itertools


def iterative(s: str) -> List[str]:
    # Time complexity: O(n² * n!)
    # Space complexity: O(n * n!)
    # 2 characters: "12" -> "12", "21"
    # 3 characters: "123" -> "123", "132", "213", "231", "312", "321"
    # 4 characters: "1234" -> "1234", "1243", "1423", "1432", ...

    n = len(s)
    if n == 0:
        return [""]

    # Initialize the `permutations` list with the first
    # character of the string `s`. Build the respective
    # permutations by adding the following characters in `s`
    # to the different possible positions in the elements
    # of the current state of `permutations`,
    # i.e.:
    # permutations = ['a']
    # add 'b' at the different positions:
    #   'a' -> 'ba', 'ab',
    # permutations = ['ba', 'ab']
    # add 'c' at the different positions:
    #   'ba' -> 'cba', 'bca', 'bac'
    #   'ab' -> 'cab', 'acb', 'abc'
    # permutations = ['cba', 'bca', 'bac', 'cab', 'acb', 'abc']
    # etc.
    permutations = [s[0]]

    # Loop over the characters of the input string `s`
    for char_index in range(1, n):
        # Store the current permutations as we add characters
        # i.e., in the first iteration of "abcd"
        # permutations = ['a']
        # we would end up having:
        # curr = ['ba', 'ab']
        curr = []

        # Loop over the current permutations
        curr_len = len(permutations[0])
        for perm in permutations:

            # Loop over the indices of the current permutation
            for index in range(curr_len + 1):
                # The new permutation is the result of
                # adding the current character s[char_index]
                # to the current `index` in the current
                # permutation `perm`
                c = s[char_index]
                new_perm = perm[:index] + c + perm[index:]
                curr.append(new_perm)

        # Update the `permutations` list with the ones
        # computed in the current iteration
        permutations = curr[:]

    return permutations


def iterative_nums(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    permutations = [[nums[0]]]
    for i in range(1, n):
        curr = []
        curr_len = len(permutations[0])
        for perm in permutations:
            for j in range(curr_len + 1):
                p = perm[:j] + [nums[i]] + perm[j:]
                curr.append(p)
        permutations = curr[:]
    return permutations


def backtrack_nums(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(start: int, end: int) -> None:
        # Recursive function

        # Base case
        if start == end:
            # Make a deep copy of the resulting permutation
            # (the permutation will be backtracked later)
            res.append(nums[:])

        # Loop over between the current pointers `start` and `end`
        for i in range(start, end):
            # New candidate solution:
            # swap elements at `start` and `i`
            nums[start], nums[i] = nums[i], nums[start]
            # Given the candidate, explore further
            backtrack(start + 1, end)
            # Backtrack: swap back the elements
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0, len(nums))
    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Permutations without Dups")
    print("-" * 60)

    # Problem with strings
    test_cases = [
        ("", [""]),
        ("a", ["a"]),
        ("ab", ["ab", "ba"]),
        ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
        ("abcdef", itertools.permutations("abcdef")),
        ("qwerasdf", itertools.permutations("qwerasdf")),
        ("1234qwera", itertools.permutations("1234qwera")),
    ]

    for s, solution in test_cases:

        print(f">>> iterative('{s}')")
        result = iterative(s)

        result = sorted(result)
        string = str(result)
        if len(string) > 60:
            string = string[:60] + "...]"
        print(string)

        solution = sorted(["".join(sol) for sol in solution])

        string = " " * 60
        test_ok = solution == sorted(result)
        print(string, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')

    # Problem with integers
    test_cases = [
        ([0], [[0]]),
        ([1], [[1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1, 2, 3], itertools.permutations([1, 2, 3])),
    ]

    for nums, solution in test_cases:

        solution = sorted([list(p) for p in solution])

        print(f">>> iterative({nums})")
        result = iterative_nums(nums)

        result = sorted(result)
        string = str(result)
        if len(string) > 60:
            string = string[:60] + "...]"
        print(string)

        string = " " * 60
        test_ok = solution == result
        print(string, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')

        print(f">>> backtrack({nums})")
        result = backtrack_nums(nums)

        result = sorted(result)
        string = str(result)
        if len(string) > 60:
            string = string[:60] + "...]"
        print(string)

        string = " " * 60
        test_ok = solution == result
        print(string, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')

        print()
