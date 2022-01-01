"""
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. 
The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. 
Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
The number of nodes in the list is in the range [1, 5 * 10^4].
1 <= Node.val <= 1000

"""
import sys

sys.path.insert(1, "./")

from collections import deque
from linked_list import (
    ListNode,
    list_to_linked_list,
    linked_list_to_list,
    print_linked_list,
)


def with_array(head: ListNode) -> ListNode:
    # Time complexity: O(n)
    # Space complexity: O(n)
    if not head.next:
        return head

    # Build a list with the nodes
    arr = []
    curr = head
    while curr:
        arr.append(curr)
        curr = curr.next

    # Number of elements
    n = len(arr)

    # Use two pointers (`left` and `right`) to select the next node
    # and change their relationships
    right = n - 1
    mid = right // 2 + 1
    prev = head
    for left in range(1, mid):
        prev.next = arr[right]
        arr[right].next = arr[left]
        prev = arr[left]
        right -= 1

    # Fix the tail
    if n & 1:
        # If there's an odd number of nodes,
        # the tail is the last `left` node
        prev.next = None
    else:
        # If there's an even number of nodes,
        # the tail is the last `right` node
        arr[right].next = None

    return head


def with_deque(head: ListNode) -> ListNode:
    # Time complexity: O(n)
    # Space complexity: O(n)

    if not head.next:
        return head

    # Create a `deque` (double-linked list),
    # which can pop elements from both ends in O(1) time
    q = deque()
    curr = head.next
    while curr:
        q.append(curr)
        curr = curr.next

    # Keep track of a previous node
    prev = head
    # Loop over until `q` is empty
    while q:
        # Modify the links between nodes: prev -> right -> left
        # Pop from the right: prev -> right
        prev.next = q.pop()
        # Pop from the left, if there're still nodes in `q`
        left = q.popleft() if q else None
        # Update the link between the `right` and `left` nodes
        # in the current iteration: right -> left
        prev.next.next = left
        # Update the previous node for next iteration
        prev = left

    if prev:
        # If the last node was from the left,
        # it's the tail
        prev.next = None

    return head


def reverse_half(head: ListNode) -> ListNode:
    # Time complexity: O(n)
    # Space complexity: O(1)

    if not head.next:
        return head

    # Find the middle of the linked list using two pointers:
    # `slow` and `fast`. `fast` advances two steps forward while
    # `slow` only one. When `fast` reaches the end,
    # `slow` is at the middle.
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Reverse the second half of the linked list
    prev = curr = slow
    while curr:
        next = curr.next
        curr.next = prev
        curr, prev = next, curr
    # make `slow` (previously the head of the second half of the
    # linked list) the tail
    slow.next = None

    # `prev`is the head of the second half of the linked list.
    # Use two pointer to each half, and reorder the list
    left, right = head, prev
    while left and right:
        next_left, next_right = left.next, right.next
        left.next, right.next = right, next_left
        left, right = next_left, next_right

    # The current `left` is the tail of the reordered list
    if left:
        left.next = None

    return head


if __name__ == "__main__":
    print("-" * 60)
    print("Reorder list")
    print("-" * 60)

    test_cases = [
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
    ]

    for nums, solution in test_cases:

        head = list_to_linked_list(nums)
        print_linked_list(head)
        new_head = with_array(head)
        result = linked_list_to_list(new_head)
        output = f"\t   with_array = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        head = list_to_linked_list(nums)
        new_head = with_deque(head)
        result = linked_list_to_list(new_head)
        output = f"\t   with_deque = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        head = list_to_linked_list(nums)
        new_head = reverse_half(head)
        result = linked_list_to_list(new_head)
        output = f"\t reverse_half = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
