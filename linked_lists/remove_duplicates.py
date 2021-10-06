"""
CRACKING THE CODING INTERVIEW
2.1. Remove duplicates from an unsorted linked list.

A temporary buffer is not allowed.

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


def sol(head: Node) -> int:
    # We can use a hashset to keep track
    # of the numbers already see:
    # Time complexity: O(n)
    # Space complexity: O(n)
    # However, if we can't use temporary buffer,
    # we can only achieve:
    # Time complexity: O(n2)
    # Space complexity: O(1)

    # Pointer to the reference node
    ref = head
    # Compare `ref` with the rest of the following nodes
    while ref:
        # Pointer to the previous node
        prev = ref
        # Pointer to the current node
        cur = ref.next
        while cur:
            if ref.val == cur.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        ref = ref.next

    return head

def solb(head: Node) -> int:
    # Same solution but removing the reference to 
    # the previous node `prev`

    # Pointer to the reference node
    ref = head
    # Compare `ref` with the rest of the following nodes
    while ref:        
        # Pointer to the current node
        cur = ref
        while cur.next:
            if ref.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next            
        ref = ref.next

    return head


if __name__ == "__main__":
    print('-' * 60)
    print('Remove duplicates from an unsorted linked list')
    print('-' * 60)
    
    test_cases = [
        ([1], [1]),
        ([1, 2, 8, 3], [1, 2, 8, 3]),
        ([1, 2, 2, 3], [1, 2, 3]),
        ([1, 2, 2, 2], [1, 2]),
        ([1, 1, 3, 2, 3], [1, 3, 2]),
        ([8, 2, 2, 2, 2], [8, 2]),
        ([2, 2, 2, 2, 2], [2]),
        ([2, 2, 2, 8, 2, 8], [2, 8]),
    ]
    
    for nums, solution in test_cases:

        head = list_to_linked_list(nums)
        res = sol(head)
        result = linked_list_to_list(res)

        string = f' sol{nums} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        head = list_to_linked_list(nums)
        res = solb(head)
        result = linked_list_to_list(res)

        string = f'solb{nums} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()