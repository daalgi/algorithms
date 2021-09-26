"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linkedlist_to_list(l: LinkNode):
    arr = []
    while l:
        if l.val is not None:
            arr.append(l.val)
        l = l.next
    return arr

def list_to_linkedlist(l: list):
    if len(l) == 0:
        return None
    first = LinkNode(l[0])
    curr = first
    for v in l[1:]:
        curr.next = LinkNode(v)
        curr = curr.next
    return first

def efficient(l1: LinkNode, l2: LinkNode) -> LinkNode:
    carry = 0
    # Dumb head node
    head = LinkNode()
    # Keep track of the current node
    current = head
    while l1 or l2:
        if l1 and l2:
            temp = l1.val + l2.val + carry
            l1 = l1.next
            l2 = l2.next
        elif not l2:
            temp = l1.val + carry
            l1 = l1.next
        else:
            temp = l2.val + carry
            l2 = l2.next
        
        carry = temp // 10
        current.next = LinkNode(temp % 10)
        current = current.next
    if carry > 0:
        current.next = LinkNode(carry)
    return head.next
    

if __name__ == "__main__":
    print('-' * 60)
    print('Add two numbers (linked list)')
    print('-' * 60)
    
    test_cases = [
        ([], [], []),
        ([], [0], [0]),
        ([1], [0], [1]),
        ([2,4,3], [5,6,4], [7, 0, 8]),
        ([9,9,9,9,9,9,9], [9,9,9,9], [8, 9, 9, 9, 0, 0, 0, 1])
    ]
    
    ll = list_to_linkedlist([0, -5])
    arr = linkedlist_to_list(ll)
    for a, b, solution in test_cases:
        
        string = f'add2num{a, b} = '
        
        # For convenience, convert from and to `list`
        a = list_to_linkedlist(a)
        b = list_to_linkedlist(b)
        result = efficient(a, b)
        result = linkedlist_to_list(result)
        
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')