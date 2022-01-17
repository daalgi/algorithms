"""
CRACKING THE CODING INTERVIEW
2.7. Intersection.
Given two singly linked lists, determine if the two lists intersect.
Return the intersecting node. Note that the intersection is defined
based on reference, not value. That is, if the kth node of the
first linked list is the exact same node (by reference) as the
jth node of the second linked list, then they are intersecting.

https://leetcode.com/problems/intersection-of-two-linked-lists/

Follow up: Could you write a solution that runs in O(m + n) 
time and use only O(1) memory?
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


def brute_force(head1: Node, head2: Node) -> int:
    # NOTE: for testing simplicity, we assume that
    # the intersection is defined on value instead of
    # reference, so value acts like a reference.

    # Two pointers to current nodes of each
    # linked list
    cur1 = head1
    cur2 = head2

    # Compare all the values of one linked list
    # with the other one.
    # Time complexity: O(n * m)
    # Space complexity: O(1)
    while cur1:

        # Loop over the second linked list and compare
        # all its values with the current in the
        # first linked list
        while cur2:
            if cur2.val == cur1.val:
                return cur2.val
            cur2 = cur2.next

        # Start over with the second linked list
        cur2 = head2
        # Move to the next node in the first linked list
        cur1 = cur1.next

    return None


def get_tail_and_size(head: Node) -> tuple:
    cur = head
    size = 0
    while cur.next:
        cur = cur.next
        size += 1
    return cur, size


def efficient(head1: Node, head2: Node) -> int:
    # NOTE: for testing simplicity, we assume that
    # the intersection is defined on value instead of
    # reference, so value acts like a reference.
    # - If two linked lists intersect, they all end up in the same node.
    # - If they were the same length, we could just
    # compare one node at a time until we find it.
    # - If we know the length of the linked list, we can chop off (or ignore)
    # the excess nodes in the longer list.
    # Time complexity: O(m + n + max(m, n)) = O(max(m, n))

    # Edge case: one linked list is None
    if head1 is None or head2 is None:
        return None

    # Get tail and size of the lists
    tail1, size1 = get_tail_and_size(head1)
    tail2, size2 = get_tail_and_size(head2)

    # If the last nodes are not the same,
    # the lists don't intersect
    if tail1.val != tail2.val:
        return None

    # Pointers to the current nodes
    cur1 = head1
    cur2 = head2

    # Chop off the longest list
    while size1 != size2:
        if size1 > size2:
            cur1 = cur1.next
            size1 -= 1
        else:
            cur2 = cur2.next
            size2 -= 1

    # Move both pointers until there's a collision
    while cur1.val != cur2.val:
        cur1 = cur1.next
        cur2 = cur2.next

    # Return the collision node (node's value)
    return cur1.val


def efficient2(head1: Node, head2: Node) -> int:
    # NOTE: for testing simplicity, we assume that
    # the intersection is defined on value instead of
    # reference, so value acts like a reference.
    # - If two linked lists intersect, they all end up in the same node.
    # - If they were the same length, we could just
    # compare one node at a time until we find it.
    # - If we know the length of the linked list, we can chop off (or ignore)
    # the excess nodes in the longer list.
    # Time complexity: O(m + n + max(m, n)) = O(max(m, n))

    # Edge case: one linked list is None
    if head1 is None or head2 is None:
        return None

    # Get tail and size of the lists
    tail1, size1 = get_tail_and_size(head1)
    tail2, size2 = get_tail_and_size(head2)

    # If the last nodes are not the same,
    # the lists don't intersect
    if tail1.val != tail2.val:
        return None

    # Force the linked-list 1 to be the longest
    if size1 < size2:
        head1, head2 = head2, head1
        tail1, tail2 = tail2, tail1
        size1, size2 = size2, size2

    # Pointers to the current nodes
    cur1 = head1
    cur2 = head2

    # Chop off the longest list
    while size2 < size1:
        cur1 = cur1.next
        size1 -= 1

    # Move both pointers until there's a collision
    while cur1.val != cur2.val:
        cur1 = cur1.next
        cur2 = cur2.next

    # Return the collision node (node's value)
    return cur1.val


def two_pointers(head1: Node, head2: Node) -> int:
    # Time complexity: O(m+n)
    # Space complexity: O(1)
    # Strategy: use two pointers, one on each linked-list,
    # and advance them at the same time.
    # - If they have the same length (which we don't even care),
    # they'll intersect in O(n) time.
    # - If their length is different, when the shorter one
    # reaches the end, move the pointer to the start of the
    # other linked-list.
    #       - When the longer one reaches the end, move the pointer
    #       to the start of the shorter linked-list.
    #       - At this point, both pointers will be at the same
    #       distance from the intersection, if there exists one.
    #       - Continue moving the pointers forward until they match.
    # If there's no intersection, both linked-lists will reach
    # their respective tails, so we'll return None
    #
    # See solution without the simplifying assumptions
    # for testing made in this script.
    # https://leetcode.com/submissions/detail/622025320/
    # TODO: avoid the 'simplifyied' testing assumptions

    a, b = head1, head2

    while a != b:
        a = head2 if not a else a.next
        b = head1 if not b else b.next

    return a.val if a else None


if __name__ == "__main__":
    print("-" * 60)
    print("Intersection of two linked lists")
    print("-" * 60)

    test_cases = [
        ([1], [1], 1),
        ([1], [2], None),
        ([1, 2, 8, 3], [5, 3], 3),
        ([1, 2, 8, 3], [5, 19, 9, 99, 1, 2, 8, 3], 1),
        ([1, 2, 8, 3], [5, 19, 2, 8, 3], 2),
        ([1, 2, 8, 3], [5, 19, 99, 8, 3], 8),
        ([1, 2, 8, 3], [5, 19, 99, 18, 999], None),
    ]

    for nums1, nums2, solution in test_cases:

        head1 = list_to_linked_list(nums1)
        head2 = list_to_linked_list(nums2)

        print("Linked-list 1:", nums1)
        print("Linked-list 2:", nums2)
        
        res = brute_force(head1, head2)
        output = f"   brute_force = "
        output += str(res)
        output += " " * (70 - len(output))
        output += f'Test: {"OK" if solution == res else "NOT OK"}'
        print(output)

        res = efficient(head1, head2)
        output = f"     efficient = "
        output += str(res)
        output += " " * (70 - len(output))
        output += f'Test: {"OK" if solution == res else "NOT OK"}'
        print(output)

        # res = efficient2(head1, head2)
        # output = f'    efficient2 = '
        # output += str(res)
        # output += ' ' * (70 - len(output))
        # output += f'Test: {"OK" if solution == res else "NOT OK"}'
        # print(output)

        # res = two_pointers(head1, head2)
        # output = f"  two_pointers = "
        # output += str(res)
        # output += " " * (70 - len(output))
        # output += f'Test: {"OK" if solution == res else "NOT OK"}'
        # print(output)

        print()
