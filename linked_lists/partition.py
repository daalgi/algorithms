"""
CRACKING THE CODING INTERVIEW
2.4. Partition.
https://leetcode.com/problems/partition-list/

Given the head of a linked list and a value x, partition it 
such that all nodes less than x come before nodes greater 
than or equal to x.

You should preserve the original relative order of the nodes 
in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""
from dataclasses import dataclass


@dataclass
class Node:
    val: int = 0
    next = None


def list_to_linked_list(nums: list) -> Node:
    n = len(nums)
    if n == 0:
        return Node(None)
    head = Node(nums[0])
    cur = head
    for num in nums[1:]:
        cur.next = Node(num)
        cur = cur.next
    return head


def linked_list_to_list(head: Node) -> list:
    res = list()
    cur = head
    while cur and cur.val:
        res.append(cur.val)
        cur = cur.next
    return res


def partition(head: Node, num: int) -> Node:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Edge case, 0 or 1 nodes
    if head is None or head.next is None:
        return head

    # References to the first linked list (< num)
    first_head = None
    first_tail = None
    # References to the second linked list (>= num)
    second_head = None
    second_tail = None
    
    # Loop over the passed linked list
    cur = head
    while cur:

        if cur.val < num:
            # Add to the first list (< num)
            if first_head is None:
                # Initiliaze it
                first_head = cur
                first_tail = cur
            else:
                first_tail.next = cur
                first_tail = first_tail.next
        else:
            # Add to the second list (>= num)
            if second_head is None:
                # Initiliaze it
                second_head = cur
                second_tail = cur
            else:
                second_tail.next = cur
                second_tail = second_tail.next
        
        # Update the current cursor of the passed linked list
        cur = cur.next

    # Edge case: first linked list not initialized
    if second_head is None:
        # Last node of the first linked list is the tail
        first_tail.next = None
        return first_head

    # Last node of the second linked list is the tail
    second_tail.next = None
    
    # Edge case: first linked list not initialized
    if first_head is None:
        return second_head
    
    # Merge first and second linked lists
    first_tail.next = second_head
    return first_head


def partition2(head: Node, num: int) -> Node:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Edge case, 0 or 1 nodes
    if head is None or head.next is None:
        return head

    # Initialize the head to a dummy node
    # to reduce the checks in the loop and later.
    # References to the first linked list (< num)
    first_head = Node(0)
    first_tail = first_head
    # References to the second linked list (>= num)
    second_head = Node(0)
    second_tail = second_head
    
    # Loop over the passed linked list
    cur = head
    while cur:

        if cur.val < num:
            first_tail.next = cur
            first_tail = first_tail.next
        else:
            second_tail.next = cur
            second_tail = second_tail.next
        
        # Update the current cursor of the passed linked list
        cur = cur.next

    # Last node of the second linked list is the tail
    second_tail.next = None
    
    # Merge first and second linked lists
    first_tail.next = second_head.next
    return first_head.next


if __name__ == "__main__":
    print("-" * 60)
    print("Partition list")
    print("-" * 60)

    test_cases = [
        ([], 1, []),
        ([1], 1, [1]),
        ([2, 1], 1, [2, 1]),
        ([2, 1], 2, [1, 2]),
        ([1, 4, 3, 2, 5, 2], 1, [1, 4, 3, 2, 5, 2]),
        ([1, 4, 3, 2, 5, 2], 2, [1, 4, 3, 2, 5, 2]),
        ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
        ([1, 4, 3, 2, 5, 2], 4, [1, 3, 2, 2, 4, 5]),
        ([1, 4, 3, 2, 5, 2], 5, [1, 4, 3, 2, 2, 5]),
    ]

    for nums, num, solution in test_cases:

        head = list_to_linked_list(nums)
        res = partition(head, num)
        result = linked_list_to_list(res)

        string = f"partition{nums, num} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
        
        head = list_to_linked_list(nums)
        res = partition2(head, num)
        result = linked_list_to_list(res)

        string = f"partition{nums, num} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()