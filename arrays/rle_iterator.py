"""
https://leetcode.com/problems/rle-iterator/

We can use run-length encoding (i.e., RLE) to encode a 
sequence of integers. In a run-length encoded array of 
even length encoding (0-indexed), for all even i, 
encoding[i] tells us the number of times that the 
non-negative integer value encoding[i + 1] is repeated 
in the sequence.

For example, the sequence arr = [8,8,8,5,5] can be encoded 
to be encoding = [3,8,2,5]. encoding = [3,8,0,9,2,5] 
and encoding = [2,8,1,8,2,5] are also valid RLE of arr.
Given a run-length encoded array, design an iterator 
that iterates through it.

Implement the RLEIterator class:
- RLEIterator(int[] encoded) Initializes the object with the 
encoded array encoded.
- int next(int n) Exhausts the next n elements and 
returns the last element exhausted in this way. If 
there is no element left to exhaust, return -1 instead.

Example 1:
Input
["RLEIterator", "next", "next", "next", "next"]
[[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]
Output
[null, 8, 8, 5, -1]

Explanation
// This maps to the sequence [8,8,8,5,5].
RLEIterator rLEIterator = new RLEIterator([3, 8, 0, 9, 2, 5]); 
// exhausts 2 terms of the sequence, returning 8. 
The remaining sequence is now [8, 5, 5].
rLEIterator.next(2); 
// exhausts 1 term of the sequence, returning 8. 
The remaining sequence is now [5, 5].
rLEIterator.next(1); 
// exhausts 1 term of the sequence, returning 5. 
The remaining sequence is now [5].
rLEIterator.next(1); 
// exhausts 2 terms, returning -1. 
This is because the first term exhausted was 5,
rLEIterator.next(2); 
but the second term did not exist. 
Since the last term exhausted does not exist, we return -1.

Constraints:

2 <= encoding.length <= 1000
encoding.length is even.
0 <= encoding[i] <= 10^9
1 <= n <= 10^9
At most 1000 calls will be made to next.
"""
from typing import List
from bisect import bisect_left


class RLEIteratorLinearScan:
    def __init__(self, encoding: List[int]):
        # Time complexity: O(1)
        # Space complexity: O(1)
        self.encoding = encoding
        self.size = len(encoding)
        self.pointer = 0

    def next(self, n: int) -> int:
        # Time complexity: O(n)
        while self.pointer < self.size and n:
            if self.encoding[self.pointer] < n:
                n -= self.encoding[self.pointer]
                self.pointer += 2
            else:
                self.encoding[self.pointer] -= n
                break

        # Check whether the end of the list was reached
        if self.pointer >= self.size:
            return -1

        # Result integer
        num = self.encoding[self.pointer + 1]

        # If the repetitions at the current pointer
        # are zero, move the pointer forward
        if self.encoding[self.pointer] == 0:
            self.pointer += 2

        return num


class RLEIteratorBinarySearch:
    def __init__(self, encoding: List[int]):
        # Time complexity: O(n)
        # Space complexity: O(n)
        self.nums = []
        self.prefix_sum = []

        acc, i, n = 0, 0, len(encoding)
        while i < n:
            acc += encoding[i]
            self.prefix_sum.append(acc)
            self.nums.append(encoding[i + 1])
            i += 2

        self.current_n = 0
        self.prefix_sum_index = 0
        self.prefix_sum_size = len(self.prefix_sum)

    def next(self, n: int) -> int:
        # Time complexity: O(logn)
        if self.prefix_sum_index >= self.prefix_sum_size:
            return -1

        self.current_n += n

        index = bisect_left(self.prefix_sum, self.current_n, 
            lo=self.prefix_sum_index)

        if index < self.prefix_sum_size:
            return self.nums[index]
        return -1


if __name__ == "__main__":
    print("-" * 60)
    print("RLE iterator")
    print("-" * 60)

    encoding = [3, 8, 0, 9, 7, 13, 1, 25]
    iter_linear_scan = RLEIteratorLinearScan(encoding)
    iter_binary_search = RLEIteratorBinarySearch(encoding)
    print("Encoding:", encoding)

    for n in [2, 1, 1, 2, 5, 2]:
        print(f"     iter_linear_scan.next({n}) = ", iter_linear_scan.next(n))
        print(f"   iter_binary_search.next({n}) = ", iter_binary_search.next(n))
        print()
