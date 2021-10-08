"""
CRACKING THE CODING INTERVIEW
2.8. Given a circular linked list, implement an algorithm that
returns the node at the beginning of the loop.

A circular linked list is a corrupt list in which a node's 
next pointer points to an earlier node, so as to make a 
loop in the linked list.

Example:
Input: A -> B -> C -> D -> E -> C (the same C as earlier)
Output: C
"""
from dataclasses import dataclass
from datetime import datetime
from random import random

@dataclass
class Node:
    val: int = 0
    next = None

    def __hash__(self):
        # In theory, if we want to have unique
        # hashes for each Node, even if their attributes
        # are the same, we should make them value-independent,
        # introducing some randomness, like:
        # return hash(f'{random()}{datetime.now()}')
        
        # But in this example, 
        # we assume that two nodes are the same (instance)
        # if their value is the same, so:
        return hash(self.val)

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.val == other.val
        )

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

def create_cycle(vals: list, cycle_index: int) -> Node:
    head = Node(vals[0])
    cur = head
    earlier_node = None if cycle_index > 0 else head
    n = len(vals)
    for i in range(1, n):

        cur.next = Node(vals[i])

        if i == cycle_index:
            # First time in what will be later on
            # identified as the starting node of the cycle
            earlier_node = cur.next

        elif cycle_index != -1 and vals[i] == vals[cycle_index]:
            # End of the Linked list,
            # the loop starts at the next node
            cur.next = earlier_node
            return head
        
        cur = cur.next

    # If there was no loop, return
    return head


def sol1(head: Node) -> any:
    # Use a hashset to track
    # the nodes already visited
    # Note: custom objects like `Node` 
    # are not hashable by default, so 
    # you need make it "hashable" to be able
    # to add it to a set or dictionary
    hashset = set()
    cur = head
    while cur:
        # print(cur)
        if cur in hashset:
            # Return the current node
            # if it's already in the hashset
            return cur.val
        
        # Add the current node to the hashset
        hashset.add(cur)

        # Update node for next iteration
        cur = cur.next

    # If no loop found, return False
    return False

def sol2(head: Node) -> any:
    # Slow and fast pointers
    slow = head
    fast = head
    
    # `slow` speed = 1 step/iter
    # `fast` speed = 2 steps/iter
    # Distance from head to loop_start = `k` steps
    # Given the 2x speed, if they started both
    # at the loop_start, they would collide
    # at the same Node.
    # Since the fast node is `k` steps ahead
    # when the slow node enters the loop,
    # they will collide at `loop_length - k`
    # which equals `k` steps from revisiting loop_start
    
    # Iterate until collision, 
    # or until end the linked list
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        # print(slow.val, fast.val)
        if fast == slow:
            # Exit the loop when they collide
            break

    # If reached the end of the linked list,
    # there's no cycle
    if not fast or not fast.next:
        return False

    # `slow` goes back to `head`
    # `fast` now moves one step/iter
    # They'll collide at the loop start
    # Iterate until collision
    slow = head
    while slow != fast:        
        # Both pointers move at step/iter
        slow = slow.next
        fast = fast.next
    
    # Both pointers are at the start of the loop
    return fast


if __name__ == "__main__":
    print('-' * 60)
    print('Loop detection in linked list')
    print('-' * 60)

    test_cases = [
        #(vals, loop_index, result)
        # `loop_index = -1` means that there's no loop
        ([1], -1, False),
        ([1, 2, 8, 3], -1, False),
        ([1, 2, 3, 4, 5], -1, False),
        ([1, 3, 1], 0, 1),
        ([1, 2, 3, 4, 1], 0, 1),
        ([1, 2, 3, 4, 2], 1, 2),
        ([1, 2, 3, 4, 3], 2, 3),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 4], 3, 4),
    ]
    
    for nums, cycle_index, solution in test_cases:

        head = create_cycle(nums, cycle_index)
        
        result = sol1(head)
        string = f' sol1{nums} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = sol2(head)
        if result is not False:
            result = result.val

        string = f' sol2{nums} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()