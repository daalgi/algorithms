"""
https://leetcode.com/problems/shuffle-an-array/

Given an integer array nums, design an algorithm 
to randomly shuffle the array. All permutations 
of the array should be equally likely as a result 
of the shuffling.

Implement the Solution class:
- Solution(int[] nums) Initializes the object 
with the integer array nums.
- int[] reset() Resets the array to its original 
configuration and returns it.
- int[] shuffle() Returns a random shuffling of the array.
 
Example 1:
Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally 
                        likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original 
                        configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. 
                        Example: return [1, 3, 2]

Constraints:
1 <= nums.length <= 200
-10^6 <= nums[i] <= 10^6
All the elements of nums are unique.
At most 5 * 10^4 calls in total will be made to reset and shuffle.
"""
from typing import List
from random import randint, randrange


class ShuffleArray1:
    def __init__(self, nums: List[int]):
        # Time complexity: O(n)
        # Space complexity: O(n)
        self.size = len(nums)
        self.nums = nums
        self.original = [*nums]

    def reset(self) -> List[int]:
        # Time complexity: O(n)
        self.nums = [*self.original]
        return self.nums

    def shuffle(self) -> List[int]:
        # Time complexity: O(n)
        # Note: use `randrange` instead of `randint`.
        # Using `randint(0, self.size - 1)` has the additional
        # operation `self.size - 1`, which repeated many times
        # can influence the performance.
        for i in range(self.size):
            j = randrange(i, self.size)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


if __name__ == "__main__":
    print("-" * 60)
    print("Shuffle an array")
    print("-" * 60)

    arrays = [
        [1, 2],
        [3, 1, 3, 6],
        [2, 1, 2, 1, 8, 9, 13, 25],
    ]

    for array in arrays:

        print("Array:    ", array)

        s = ShuffleArray1(array)
        print("shuffle():", s.shuffle())
        print("shuffle():", s.shuffle())
        print("reset():  ", s.reset())

        print()
