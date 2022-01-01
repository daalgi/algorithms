"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the 
end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?
"""
import sys

sys.path.insert(1, "./")

from linked_list import (
    ListNode,
    list_to_linked_list,
    linked_list_to_list,
    print_linked_list,
)


def one_pass(head: ListNode, n: int) -> ListNode:
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Special case: only one node
    # (by definition the passed linked list will
    # have at least one node)
    if not head.next:
        # Remove the only node in the linked list
        return None

    # Use two pointers. The `fast` pointer will go ahead of `slow`
    # so there's a gap of `n` steps between them. When `fast` reaches
    # the end of the linked list, we can change the reference
    # from `slow.next` to `slow.next.next`,
    # effectively removing the nth node from the end.
    # Note: n = 1 implies remove the last node (n = 0 is invalid)
    slow = fast = head

    # Loop over until n == 1
    while fast and n > -1:
        fast = fast.next
        n -= 1

    # If `n` didn't reach `-1`, it means that `fast`
    # reached the end of the linked list first,
    # so the node to remove is the `head`
    if n > -1:
        return head.next

    # Once there's a gap of `n` nodes between `slow` and `fast`,
    # move both `slow` and `fast` forward until `fast` reaches the end.
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove the reference of the nth-node from the end
    slow.next = slow.next.next

    return head


if __name__ == "__main__":
    print("-" * 60)
    print("Remove nth node from end of list")
    print("-" * 60)

    test_cases = [
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 4, [1, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 3, [1, 2, 4, 5]),
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
    ]

    for nums, n, solution in test_cases:

        head = list_to_linked_list(nums)
        print_linked_list(head)

        new_head = one_pass(head, n)
        result = linked_list_to_list(new_head)
        output = f"\t one_pass({n}) = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
