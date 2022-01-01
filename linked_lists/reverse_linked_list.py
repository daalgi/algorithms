"""
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, 
and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively 
or recursively. Could you implement both?
"""
import sys

sys.path.insert(1, "./")

from linked_list import (
    ListNode,
    list_to_linked_list,
    linked_list_to_list,
    print_linked_list,
)


def iterative(head: ListNode) -> ListNode:
    # Time complexity: O(n)
    # Space complexity: O(1)
    if not head:
        return None

    # Use three pointers to store the
    # previous, current and next nodes, so we can
    # re-assign their relationships
    prev = curr = head
    while curr:
        next = curr.next
        curr.next = prev
        curr, prev = next, curr

    head.next = None
    return prev


def recursive(head: ListNode) -> ListNode:
    # Time complexity: O(n)
    # Space complexity: O(n)

    def recursion(node: ListNode, prev: ListNode = None) -> ListNode:
        # Base case:
        if not node:
            # If we've reached the end of the linked list,
            # return the previous node
            return prev

        next = node.next
        node.next = prev
        return recursion(next, node)

    return recursion(head)


if __name__ == "__main__":
    print("-" * 60)
    print("Reverse linked list")
    print("-" * 60)

    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ]

    for nums, solution in test_cases:

        head = list_to_linked_list(nums)
        print_linked_list(head)
        new_head = iterative(head)
        result = linked_list_to_list(new_head)
        output = f"\t iterative = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        head = list_to_linked_list(nums)
        new_head = recursive(head)
        result = linked_list_to_list(new_head)
        output = f"\t recursive = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
