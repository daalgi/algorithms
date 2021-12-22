"""
https://leetcode.com/problems/find-median-from-data-stream/

The median is the middle value in an ordered integer list. If the size of 
the list is even, there is no middle value and the median is the mean 
of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the 
data structure.
double findMedian() returns the median of all elements so far. 
Answers within 1e-5 of the actual answer will be accepted.

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:
-105 <= num <= 105
There will be at least one element in the data structure before 
calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.

Follow up:
If all integer numbers from the stream are in the range [0, 100], 
how would you optimize your solution?
If 99% of all integer numbers from the stream are in the 
range [0, 100], how would you optimize your solution?
"""
from typing import List
import heapq


def heap0(nums: List[int], val: int) -> float:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)

    # Note: algorithm implemented as a function
    # instead of a class

    # Convert list to a min-heap
    # O(n)
    heap = nums
    heapq.heapify(heap)

    # Add new value
    heapq.heappush(heap, val)

    # Return the median
    # O(nlogn)
    size = len(heap)
    if size & 1:
        # If there's an odd number of elements in the heap,
        # the median it's the element at the middle of the heap, i.e.
        #   0123456 (7 elements)
        #  -1001345
        #      x    (middle value at index 3 = size / 2)
        #   xxxx    (nsmallest(4, heap), index 3 + 1 elements = (size/2+1))
        return heapq.nsmallest(size // 2 + 1, heap)[-1]

    # If there's an even number of elements in the heap,
    # the median is the mean of the two middle values, i.e.
    #   012345 (6 elements)
    #  -100134
    #     xx   (middle values at indices 2 and 3 = from (size/2-1) to (size/2))
    #   xxxx   (nsmallest(4, heap), just up to index 3 = size/2+1)
    arr = heapq.nsmallest(size // 2 + 1, heap)[-2:]
    return sum(arr) / 2


class MedianFinder:
    def __init__(self) -> None:
        # min-heap: heap with the larger half of the numbers,
        # so we can get the minimum in O(1).
        # The length of self.top will always be equal or +1
        # of the length of self.bottom
        self.top = []
        # max-heap: heap with the smaller half of the numbers,
        # so we can get the maximum in O(1)
        self.bottom = []

    def add(self, num: int) -> None:
        # Time complexity: O(logn)

        if not len(self.top) and not len(self.bottom):
            # First element to be added to the top heap
            heapq.heappush(self.top, num)

        elif len(self.top) == len(self.bottom):
            # If both heaps have the same length
            if -self.bottom[0] <= num:
                # If the new number belongs to the top half,
                # it will be added to the top heap.
                heapq.heappush(self.top, num)
            else:
                # If the new number belongs to the bottom half,
                # we have to pop the largest number from the bottom heap
                # to be added to the top, and then add the new
                # number to the bottom
                val = heapq.heappop(self.bottom)
                heapq.heappush(self.top, -val)  # from max-heap to min-heap
                heapq.heappush(self.bottom, -num)  # add to max-heap

        elif len(self.top) > len(self.bottom):
            # If the length of the top half is larger (+1)
            if self.top[0] > num:
                # If the new number belongs to the bottom half, add it
                heapq.heappush(self.bottom, -num)
            else:
                # If the new number belongs to the top half,
                # we have to pop the smallest number from the top heap
                # to be added to the bottom, and then add the new
                # number to the top
                val = heapq.heappop(self.top)
                heapq.heappush(self.bottom, -val)
                heapq.heappush(self.top, num)

    def find_median(self) -> float:
        # Time complexity: O(1)
        if len(self.top) > len(self.bottom):
            # If there's an odd number of elements, the median
            # is at the middle (the smallest number in the top half)
            return self.top[0]

        # If there's an even number of elements, the median
        # is the mean of the smallest in the top half (self.top[0]) and the
        # largest in the bottom half (-self.bottom[0])
        return (self.top[0] - self.bottom[0]) / 2


def heap1(nums: List[int], val: int) -> float:
    # Add number  - Time complexity: O(logn)
    # Find median - Time complexity: O(1)
    # Space complexity: O(n)

    mf = MedianFinder()
    # Add the original numbers
    for num in nums:
        mf.add(num)

    # Add the new number
    mf.add(val)

    return mf.find_median()


class MedianFinder2:
    def __init__(self) -> None:
        # min-heap: heap with the larger half of the numbers,
        # so we can get the minimum in O(1).
        # The length of self.top will always be equal or +1
        # of the length of self.bottom
        self.top = []
        # max-heap: heap with the smaller half of the numbers,
        # so we can get the maximum in O(1)
        self.bottom = []

    def add(self, num: int) -> None:
        # Time complexity: O(logn)
        # Much more simplified version

        if len(self.bottom) == len(self.top):
            # If equal size, add the new number to the bottom heap,
            # and pop the maximum number from the bottom heap to push it
            # into the top heap.
            heapq.heappush(self.bottom, -num)
            heapq.heappush(self.top, -heapq.heappop(self.bottom))
        else:
            # If not equal size, add the new number to the top heap,
            # and pop the minimum number from the top heap to push it
            # into the bottom heap
            heapq.heappush(self.top, num)
            heapq.heappush(self.bottom, -heapq.heappop(self.top))

    def find_median(self) -> float:
        # Time complexity: O(1)
        if len(self.top) > len(self.bottom):
            # If there's an odd number of elements, the median
            # is at the middle (the smallest number in the top half)
            return self.top[0]

        # If there's an even number of elements, the median
        # is the mean of the smallest in the top half (self.top[0]) and the
        # largest in the bottom half (-self.bottom[0])
        return (self.top[0] - self.bottom[0]) / 2


def heap2(nums: List[int], val: int) -> float:
    # Add number  - Time complexity: O(logn)
    # Find median - Time complexity: O(1)
    # Space complexity: O(n)

    mf = MedianFinder2()
    # Add the original numbers
    for num in nums:
        mf.add(num)

    # Add the new number
    mf.add(val)

    return mf.find_median()


if __name__ == "__main__":
    print("-" * 60)
    print("Find median from data stream")
    print("-" * 60)

    test_cases = [
        ([1], 2, 1.5),
        ([1, 2], 2, 2),
        ([1, 2, 2], -8, 1.5),
        ([-8, 1, 2, 2], 0, 1),
        ([-8, 0, 1, 2, 2], 8, 1.5),
    ]

    for nums, val, solution in test_cases:

        output = f"Nums: {nums}"
        if len(output) > 30:
            output = output[:60] + "...]"
        print(output)

        result = heap0([*nums], val)
        output = f"\t heap1({val}) = "
        output += " " * (15 - len(output))
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = heap1([*nums], val)
        output = f"\t heap1({val}) = "
        output += " " * (15 - len(output))
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = heap2([*nums], val)
        output = f"\t heap2({val}) = "
        output += " " * (15 - len(output))
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
