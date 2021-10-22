"""
CRACKING THE CODING INTERVIEW
2.2. Return Kth to last:
Implement an algorithm to find the kth to 
last element of a single linked list.
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
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


def sol(head: Node, k_to_last: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Use two pointers
    slow = head
    fast = head

    # Loop over to get the fast pointer
    # at a distance `k_to_last` nodes
    # from the head
    while fast.next and k_to_last > 0:
        fast = fast.next
        k_to_last -= 1

    # If the end of the linked list has been
    # reached before achieving a distance of
    # `k_to_last` to the slow pointer,
    # then the linked list is not long enough
    # for the `k_to_last` value passed.
    if k_to_last > 0:
        return False

    # Loop over until the end of the
    # linked list in the fast pointer,
    # updating the slow pointer at the same rate
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Return the value of the slow pointer
    return slow.val


def solb(head: Node, k_to_last: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Use two pointers
    slow = head
    fast = head

    # Loop over to get the fast pointer
    # at a distance `k_to_last` nodes
    # from the head
    for i in range(k_to_last):
        if fast.next is None:
            return False
        fast = fast.next

    # Loop over until the end of the
    # linked list in the fast pointer,
    # updating the slow pointer at the same rate
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Return the value of the slow pointer
    return slow.val


if __name__ == "__main__":
    print('-' * 60)
    print('Kth to last in a singly-linked list')
    print('-' * 60)
    
    test_cases = [
        ([1], 0, 1),
        ([1], 1, False),
        ([1, 2, 8, 3], 0, 3),
        ([1, 2, 8, 3], 1, 8),
        ([1, 2, 8, 3], 2, 2),
        ([1, 2, 8, 3], 3, 1),
        ([1, 2, 8, 3], 4, False),
    ]
    
    for nums, k_to_last, solution in test_cases:

        head = list_to_linked_list(nums)
        res = sol(head, k_to_last)

        string = f'   kth_to_last{nums} = '
        string += ' ' * (35 - len(string))
        string += str(res)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == res else "NOT OK"}')

        res = solb(head, k_to_last)

        string = f' kth_to_last_b{nums} = '
        string += ' ' * (35 - len(string))
        string += str(res)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == res else "NOT OK"}')

        print()