"""
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is 
sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""
from typing import List
import heapq
from copy import deepcopy


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def copy(self):
        root_copy = ListNode()
        curr_copy = root_copy
        curr = self
        while curr:
            curr_copy.next = ListNode(curr.val)
            curr = curr.next
            curr_copy = curr_copy.next

        return root_copy.next

    def print(self):
        output = f"root: {self.val}"
        curr = self.next
        while curr:
            output += f" -> {curr.val}"
            curr = curr.next
        print(output)


def list_to_list_of_ListNode(nums: List[List[int]]) -> List[ListNode]:
    res = list()
    for list_i in nums:
        root = ListNode()
        curr = root
        for n in list_i:
            curr.next = ListNode(n)
            curr = curr.next

        res.append(root.next)

    return res


def listNodes_to_list(list_nodes: ListNode) -> List[int]:
    res = list()
    curr = list_nodes
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


def brute_force(lists: List[ListNode]) -> ListNode:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)

    # Populate a list with all the values from the nodes
    # O(n)
    heap = list()
    k = len(lists)
    i = 0
    while i < k:
        while lists[i]:
            heap.append(lists[i].val)
            lists[i] = lists[i].next
        i += 1

    # Turn the list into a min-heap
    # O(n)
    heapq.heapify(heap)

    # Pop the elements of the heap and create the ListNode
    # O(nlogn)
    root = ListNode()
    prev = root
    while heap:
        prev.next = ListNode(heapq.heappop(heap))
        prev = prev.next

    return root.next


def heap(lists: List[ListNode]) -> List[ListNode]:
    # Time complexity: O(nlogk)
    # Space complexity: O(n)

    # Build a list of tuples with the k root nodes
    # (node.val, i, node)
    # where `i` is an additional index to avoid errors
    # with duplicated `node.val` in the heap
    # (ListNode doesn't support '<', so we need another number
    # to decide which one is "smaller")
    # O(k)
    heap = list()
    for i, node in enumerate(lists):
        if node:
            heap.append((node.val, i, node))

    # Convert the list into a min-heap
    # O(k)
    heapq.heapify(heap)

    #
    # O(nlogk)
    root = ListNode()
    tail = root
    while heap:
        node = heapq.heappop(heap)[2]  # (node.val, i, node)
        tail.next = node
        tail = tail.next
        if node.next:
            i += 1  #
            heapq.heappush(heap, (node.next.val, i, node.next))

    return root.next


if __name__ == "__main__":
    print("-" * 60)
    print("Merg K sorted lists")
    print("-" * 60)

    test_cases = [
        ([], []),
        ([[]], []),
        ([[1, 2]], [1, 2]),
        ([[1, 8], [3, 13]], [1, 3, 8, 13]),
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([[1, 3, 4, 8], [3, 4, 5, 13]], [1, 3, 3, 4, 4, 5, 8, 13]),
    ]

    for nums, solution in test_cases:

        output = f"Nums: {nums}"
        if len(output) > 60:
            output = output[:60] + "...]"
        print(output)

        nodes_list = list_to_list_of_ListNode(nums)

        result = brute_force([n.copy() for n in nodes_list if n])
        result = listNodes_to_list(result)
        output = f"\t brute_force = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        if len(result) > 30:
            result = result[:30] + " ...]"
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = heap([n.copy() for n in nodes_list if n])
        result = listNodes_to_list(result)
        output = f"\t        heap = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        if len(result) > 30:
            result = result[:30] + " ...]"
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
