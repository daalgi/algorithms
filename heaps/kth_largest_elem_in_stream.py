"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class to find the kth largest element in a stream. Note that it is 
the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k 
and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the 
element representing the kth largest element in the stream.

Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
 

Constraints:
1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the 
array when you search for the kth element.
"""
from typing import List
import heapq


def heapmax(nums: List[int], k: int, val: int) -> int:
    # Time complexity: O(n + nlogk)
    # Constructor: O(n) (heapify turns a list into a heap in O(n))
    # Add function: O(logn + (n-k)logn)
    # Space complexity: O(n)

    # Note: implemented as a function instead of a class

    # Strategy: use a min-heap with its values' sign changed,
    # so effectively we can consider it a max-heap.
    # Not optimal as the stream accumulated values grow.

    # Initialize the `class`
    # Transform to negative values to have a "heapmax"
    # (remember to multiply by -1 again when operating with them)
    # O(n)
    heap = [-n for n in nums]
    # O(n)
    heapq.heapify(heap)

    # Function `add(val)`
    # O(logn)
    heapq.heappush(heap, -val)
    # O((n-k) logn)
    return -heapq.nsmallest(k, heap)[-1]


def heapmin_eff(nums: List[int], k: int, val: int) -> int:
    # Time complexity: O(nlogn + nlogk)
    # Constructor: O(nlogn) (heapify turns a list into a heap in O(n))
    # Add function: O(logn + n logk)
    # Space complexity: O(n)

    # Note: implemented as a function instead of a class

    # Strategy: keep a min-heap of length `k`, so the elements remaining
    # will be the k largest elements in the stream.
    # Much more optimized as the stream accumulated values grow.

    # Initialize the `class`
    # O(1)
    heap = nums
    # O(n)
    heapq.heapify(heap)
    # Remove the smallest elements until we only
    # have `k` elements in the heap
    # O(nlogn)
    while len(heap) > k:
        heapq.heappop(heap)

    # Function `add(val)`
    if len(heap) < k:
        # If the heap has less than `k` elements, push `val`
        # O(logk)
        heapq.heappush(heap, val)
    elif val > heap[0]:
        # If the heap has more than `k` elements and the minimum
        # is smaller than `val`,
        # pop and push, equivalent to `heapreplace`
        # O(2logk)
        heapq.heapreplace(heap, val)

    # Kth largest element is currently at the top of the heap
    # (minimum of the heap)
    return heap[0]


if __name__ == "__main__":
    print("-" * 60)
    print("Kth largest element in a stream")
    print("-" * 60)

    test_cases = [
        # (nums, k, val, solution)
        ([1], 1, 8, 8),
        ([1], 2, 8, 1),
        ([1], 1, -1, 1),
        ([4, 5, 8, 2], 3, 3, 4),
        ([4, 5, 8, 2, 3], 3, 5, 5),
        ([4, 5, 8, 2, 3, 5], 3, 10, 5),
        ([4, 5, 8, 2, 3, 5, 10], 3, 9, 8),
        ([4, 5, 8, 2, 3, 5, 10, 9], 3, 4, 8),
    ]

    for nums, k, val, solution in test_cases:

        print("Nums:", nums)
        print("k:", k)
        print("Add val:", val)

        result = heapmax(nums, k, val)
        output = f"\t     heapmax = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = heapmin_eff(nums, k, val)
        output = f"\t heapmin_eff = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
