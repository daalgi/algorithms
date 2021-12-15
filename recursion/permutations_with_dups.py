"""
CRACKING THE CODING INTERVIEW
8.8 Permutations with Dups (with duplicates):
Write a method to compute all permutations of a string
whose characters are not necessarily unique. The list of
permutations should not have duplicates.


https://leetcode.com/problems/permutations-ii/
Given a collection of numbers, nums, that might contain 
duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
from typing import List
import itertools


def backtrack_list(nums: List[any]) -> List[List[any]]:
    n = len(nums)
    res = []

    # Integer counter
    counter = dict()
    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    def dfs(comb: List[int], counter: dict):
        # Recursive function
        # `comb` is a list representing the current combination

        # Base case
        if len(comb) == n:  # len(nums)
            res.append(comb[:])
            return

        for num in counter:
            if counter[num] > 0:
                # Only add the current number if the count is > 0

                # New candidate solution: add current number
                # to the current combination
                comb.append(num)
                counter[num] -= 1
                # Continue the exploration
                dfs(comb, counter)
                # Revert the choice for the next exploration
                comb.pop()
                counter[num] += 1

    dfs([], counter)
    return res


def backtrack_string(s: str) -> List[str]:
    # Convert the string to a list
    string = list(s)
    res = backtrack_list(string)
    return ["".join(p) for p in res]


def iterative_nums(nums: List[int]) -> List[List[int]]:
    # TODO
    pass


if __name__ == "__main__":
    print("-" * 60)
    print("Permutations with Dups")
    print("-" * 60)

    # Permutations of a string
    test_cases = [
        ("", [""]),
        ("a", ["a"]),
        ("ab", ["ab", "ba"]),
        ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
        ("abcdef", itertools.permutations("abcdef")),
        # Repeated characters
        ("aaa", ["aaa"]),
        ("aab", ["baa", "aba", "aab"]),
        ("aaab", ["baaa", "abaa", "aaba", "aaab"]),
    ]

    # print(["".join(p) for p in itertools.permutations("aab")])
    for s, solution in test_cases:

        solution = sorted(["".join(sol) for sol in solution])

        print(f">>> backtrack_string('{s}')")
        result = backtrack_string(s)

        result = sorted(result)
        string = str(result)
        if len(string) > 60:
            string = string[:60] + "...]"
        print(string)

        string = " " * 60
        test_ok = solution == result
        print(string, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')

    # Permutations of a list of integers
    test_cases = [
        ([0], [[0]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([0, 0, 1], [[0, 0, 1], [0, 1, 0], [1, 0, 0]]),
        ([1, 2, 1], [[1, 2, 1], [2, 1, 1], [1, 1, 2]]),
    ]

    for nums, solution in test_cases:

        solution = sorted(solution)

        print(f">>> backtrack_list({nums})")
        result = backtrack_list(nums)

        result = sorted(result)
        string = str(result)
        if len(string) > 60:
            string = string[:60] + "...]"
        print(string)

        string = " " * 60
        test_ok = solution == result
        print(string, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')

        # print(f">>> iterative_nums({nums})")
        # result = iterative_nums(nums)

        # result = sorted(result)
        # string = str(result)
        # if len(string) > 60:
        #     string = string[:60] + "...]"
        # print(string)

        # string = " " * 60
        # test_ok = solution == result
        # print(string, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')
