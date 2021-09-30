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
"""

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linkedlist_to_list(l: ListNode):
    arr = []
    while l:
        if l.val is not None:
            arr.append(l.val)
        l = l.next
    return arr

def list_to_linkedlist(l: list):
    if len(l) == 0:
        return None
    first = ListNode(l[0])
    curr = first
    for v in l[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return first

def remove_from_end(head: ListNode, n: int) -> ListNode:
    # Node counters
    ifast, islow = 0, 0

    # Node pointers
    fast = head
    slow = head

    # Loop over the nodes to get the reference of the
    # node whose `next` attribute will be updated to
    # skip the node to be removed and point to the
    # following node (`slow`)
    while fast.next:
        
        # Update the fast pointer
        ifast += 1
        fast = fast.next
        
        # If the distance between fast and slow
        # pointers is equal to `n`, 
        # update the slow pointer
        if n < ifast - islow:
            islow += 1
            slow = slow.next

    # print(islow, ifast, n)
    if ifast == 0:
        # If the linked list only had one node
        # (so `n` can only be equal to 1),
        # them remove it
        head = None

    elif n == 1:
        # If removing the last node, 
        # the `slow.next` will point to nothing
        slow.next = None

    elif ifast == n - 1:
        # If removing the first node,
        # the `head` should be updated to the next node
        # (note that `ifast` is a zero-based index and 
        # `n` is a one-based index starting from the end,
        # so the first element is at 
        # the (n-1) zero-based index from the end)
        head = head.next

    else:
        # If removing other than last node, 
        # `slow.next` should skip a node and 
        # point to the after-next
        after_next = slow.next.next
        slow.next = after_next

    return head


if __name__ == "__main__":
    print('-' * 60)
    print('Remove Nth node from end of list')
    print('-' * 60)
    test_cases = [
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [1, 2, 4, 5]),
        ([1, 2, 3, 4, 5], 4, [1, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
    ]
    
    for arr, n, solution in test_cases:
    
        # For convenience, convert from and to `list`
        head = list_to_linkedlist(arr)
        new_head = remove_from_end(head, n)
        res = linkedlist_to_list(new_head)
        
        arr_string = str(arr) if len(arr) < 7 else f'{str(arr[:6])}...truncated...'
        string = f'array = {arr_string}, n = {n}, res = {res}'
        string += ' ' * (80 - len(string))
        string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string)

    print()