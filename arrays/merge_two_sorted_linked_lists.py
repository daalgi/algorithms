# Definition for singly-linked list.
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

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    first = ListNode(None)
    last = first
    is_first_iter = True
    while True:
        if not l1 and not l2:
            return first
        elif l1 and l2:
            if l1.val <= l2.val:
                curr = ListNode(l1.val)
                l1 = l1.next
            else:
                curr = ListNode(l2.val)
                l2 = l2.next
        elif l2:
            curr = ListNode(l2.val)
            l2 = l2.next
        elif l1:
            curr = ListNode(l1.val)
            l1 = l1.next
            
        # Update for next iteration
        if is_first_iter:
            first = curr
            last = first
            is_first_iter = False
        else:
            last.next = curr
            last = last.next


if __name__ == "__main__":
    print('-' * 60)
    print('Merge two sorted linked lists and return a sorted linked list')
    print('-' * 60)
    
    test_cases = [
        ([], [], []),
        ([], [0], [0]),
        ([], [8, 86], [8, 86]),
        ([1, 2], [2], [1, 2, 2]),
        ([1, 6, 9], [-2, 2, 10], [-2, 1, 2, 6, 9, 10]),        
    ]
    
    ll = list_to_linkedlist([0, -5])
    arr = linkedlist_to_list(ll)
    for a, b, solution in test_cases:
        
        string = f'merge{a, b} = '
        
        # For convenience, convert from and to `list`
        a = list_to_linkedlist(a)
        b = list_to_linkedlist(b)
        result = mergeTwoLists(a, b)
        result = linkedlist_to_list(result)
        
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

