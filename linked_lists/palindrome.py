"""
CRACKING THE CODING INTERVIEW
2.6. Palindrome.
Implement a function to check if a linked list 
is a palindrome.
"""
from dataclasses import dataclass
from collections import deque

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


def reverse_with_stack(head: Node) -> Node:
    # Make a copy of a reversed linked list
    stack = deque()
    cur = head
    while cur:
        stack.append(Node(cur.val))
        cur = cur.next

    head_reversed = stack.pop()
    cur = head_reversed
    while stack:
        cur.next = stack.pop()
        cur = cur.next

    return head_reversed

def reverse_directly(node: Node) -> Node:
    head = None
    while node:
        n = Node(node.val)
        n.next = head
        head = n
        node = node.next
    return head

def compare_linked_lists(head1: Node, head2: Node) -> bool:
    # Compare the values of two linked lists node by node
    cur1 = head1
    cur2 = head2
    while cur1 and cur2:
        if cur1.val != cur2.val:
            return False
        cur1 = cur1.next
        cur2 = cur2.next
    
    return cur1 is None and cur2 is None
    
def sol1(head: Node) -> bool:
    # Make a reversed copy of the linked list
    # and compare nodes one by one until the middle
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Use a stack to reverse the linked list
    stack = deque()
    cur = head
    size = 0
    while cur:
        size += 1
        stack.append(Node(cur.val))
        cur = cur.next

    head_reversed = stack.pop()
    cur = head_reversed
    while stack:
        cur.next = stack.pop()
        cur = cur.next

    # Compare nodes
    cur = head
    cur_rev = head_reversed
    size_half = size // 2
    for i in range(size_half):
        if cur.val != cur_rev.val:
            return False
        cur = cur.next
        cur_rev = cur_rev.next

    return True


def sol1b(head: Node) -> bool:
    # Same as `sol1`, but we use the created reverse function
    # Time complexity: O(n)
    # Space complexity: O(n)
    head_reversed = reverse_with_stack(head)
    return compare_linked_lists(head, head_reversed)
    
def sol1c(head: Node) -> bool:
    # Same as `sol1b`, but reversed directly without 
    # additonal data-structures
    # Time complexity: O(n)
    # Space complexity: O(n)
    head_reversed = reverse_with_stack(head)
    return compare_linked_lists(head, head_reversed)
        
def sol2(head: Node) -> bool:
    # - Using two pointers and a stack.
    # - `fast` pointer moves 2x `slow` faster
    # - When `fast` reaches the end, `slow`
    # is at the middle of the linked list
    slow = head
    fast = head
    stack = deque()
    # Loop over up until `fast` or `fast.next`
    # reaches the end, and stack the nodes 
    # of the `slow` pointer
    while fast and fast.next:
        stack.append(slow)
        slow = slow.next
        fast = fast.next.next

    # If there's and odd number of elements,
    # skip the node at the middle
    if fast:
        slow = slow.next

    # Compare the nodes from the middle
    # with the ones stacked
    while stack and slow:
        node = stack.pop()
        if slow.val != node.val:
            return False
        slow = slow.next

    return True


if __name__ == "__main__":
    print('-' * 60)
    print('Is linked list palindrome?')
    print('-' * 60)
    
    test_cases = [
        ([1], True),
        ([1, 1], True),
        ([1, 2], False),
        ([1, 2, 2, 1], True),
        ([1, 2, 2, 2], False),
        ([1, 2, 8, 3], False),
        ([1, 2, 8, 2, 1], True),
        ([1, 2, 8, 8, 1], False),
    ]
    
    for nums, solution in test_cases:

        head = list_to_linked_list(nums)
        
        res = sol1(head)
        string = f' sol1{nums} = '
        string += ' ' * (35 - len(string))
        string += str(res)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == res else "NOT OK"}')
        
        res = sol1b(head)
        string = f'sol1b{nums} = '
        string += ' ' * (35 - len(string))
        string += str(res)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == res else "NOT OK"}')
        
        res = sol1c(head)
        string = f'sol1c{nums} = '
        string += ' ' * (35 - len(string))
        string += str(res)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == res else "NOT OK"}')
        
        res = sol2(head)
        string = f' sol2{nums} = '
        string += ' ' * (35 - len(string))
        string += str(res)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == res else "NOT OK"}')
        
        print()