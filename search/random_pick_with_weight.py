"""
https://leetcode.com/problems/random-pick-with-weight/

You are given a 0-indexed array of positive integers w 
where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which 
randomly picks an index in the range [0, w.length - 1] 
(inclusive) and returns it. The probability of picking an 
index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking 
index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the 
probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 
Example 1:
Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]
Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to 
return 0 since there is only one element in w.

Example 2:
Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]
Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the 
second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the 
first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
 
Constraints:

1 <= w.length <= 10^4
1 <= w[i] <= 10^5
pickIndex will be called at most 10^4 times.
"""
from typing import List
from copy import deepcopy
from random import randint


class BruteForce:
    def __init__(self, nums: List[int]):
        # Time complexity: O(max(x) n)
        # Space complexity: O(max(x) n)
        # Construct a list where the numbers are repeated
        # the times of the number itself, i.e.
        # nums = [2, 5, 3]
        # weights = [2, 2, 5, 5, 5, 5, 5, 3, 3, 3]
        self.weights = []
        n = len(nums)
        for i in range(n):
            for _ in range(nums[i]):
                self.weights.append(i)
        self.last_index = len(self.weights) - 1

    def pick_index(self) -> int:
        # Time complexity: O(1)
        # Pick an index by generating a random integer
        rnd = randint(0, self.last_index)
        return self.weights[rnd]


class PrefixSumLinearScan:
    def __init__(self, nums: List[int]):
        # Time complexity: O(n)
        # Space complexity: O(n)
        # Construct a list with the prefix sums of `nums`
        self.prefix_sums = []
        self.size = len(nums)
        prefix_sum = 0
        for i in range(self.size):
            prefix_sum += nums[i]
            self.prefix_sums.append(prefix_sum)

        self.total_sum = prefix_sum

    def pick_index(self) -> int:
        # Time complexity: O(n)

        # Generate a randon index
        target = randint(1, self.total_sum)

        # Loop over the `prefix_sums`
        for i in range(self.size):
            if target <= self.prefix_sums[i]:
                return i


class PrefixSumBinarySearch:
    def __init__(self, nums: List[int]):
        # Time complexity: O(n)
        # Space complexity: O(n)
        # Construct a list with the prefix sums of `nums`
        self.prefix_sums = []
        prefix_sum = 0
        n = len(nums)
        for i in range(n):
            prefix_sum += nums[i]
            self.prefix_sums.append(prefix_sum)

        self.total_sum = prefix_sum
        self.last_index = n - 1

    def pick_index(self) -> int:
        # Binary search
        # Time complexity: O(logn)
        target = randint(1, self.total_sum)
        left, right = 0, self.last_index
        while left < right:
            mid = (left + right) // 2
            if target <= self.prefix_sums[mid]:
                right = mid
            else:
                left = mid + 1
        return right


if __name__ == "__main__":
    print("-" * 60)
    print("Random pick with weight")
    print("-" * 60)

    test_cases = [
        # (nums), no tests
        ([1, 1]),
        ([1, 2]),
        ([1, 8]),
        ([100, 100]),
        ([100, 1000]),
        ([1000, 1, 1000]),
        ([1000, 100000, 1000]),
        ([1, 1, 1, 2, 8, 100]),
        ([1] * 88 + [1000]),
        (list(range(10, 2000, 10))),
    ]

    num_picks = 8

    for nums in test_cases:

        nums_str = str(nums)
        if len(nums_str) > 60:
            nums_str = nums_str[:55] + " ...]"
        print("nums:", nums_str)

        brute_force = BruteForce(nums)
        prefix_sum_linear_scan = PrefixSumLinearScan(nums)
        prefix_sum_binary_search = PrefixSumBinarySearch(nums)

        result = []
        for i in range(num_picks):
            result.append(brute_force.pick_index())
        output = f"               brute_force = "
        output += str(result)
        print(output)

        result = []
        for i in range(num_picks):
            result.append(prefix_sum_linear_scan.pick_index())
        output = f"    prefix_sum_linear_scan = "
        output += str(result)
        print(output)

        result = []
        for i in range(num_picks):
            result.append(prefix_sum_binary_search.pick_index())
        output = f"  prefix_sum_binary_search = "
        output += str(result)
        print(output)

        print()
