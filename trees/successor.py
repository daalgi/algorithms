"""
CRACKING THE CODING INTERVIEW
4.6 Successor:
Write an algorithm to find the "next" node (i.e., in-order successor)
of a given node in a binary search tree. You may assume that each node
has a link to its parent
"""
from collections import deque

import sys

sys.path.insert(1, "./")

from tree_node import TreeNode, sorted_array_to_bst, find_in_bst, printTree


def iterative(node: TreeNode) -> bool:
    # Base case
    if not node:
        return None

    if node.right:
        # If the node has a right child,
        # the in-order successor will always be
        # the leftmost child of the right subtree
        cur = node.right
        while cur.left:
            cur = cur.left
        return cur

    if not node.parent:
        # If the node hasn't right child and no parent,
        # there's no in-order successor
        return None

    # If the node hasn't a right child and has a parent,
    # the in-order successor will always be an ancestor, but which one?
    # The first ancestor whose left child comes from the original node.

    # Loop over until parent = root or parent.left = node
    parent = node.parent
    while parent and parent.left is not node:
        node = parent
        parent = parent.parent

    return parent


if __name__ == "__main__":
    print("-" * 60)
    print("Successor in a BST")
    print("-" * 60)

    test_cases = [
        # (tree_as_sorted_list, ref_num, node.data)
        ([1], 1, None),
        ([1, 2], 2, None),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 2),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 3),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 4),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 6),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 7),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 8),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 8, 9),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, None),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 1, 2),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 2, 3),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 3, 4),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 4, 5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 5, 6),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 6, 7),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 7, 8),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 8, 9),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 9, 10),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 10, 11),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 11, 12),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 12, 13),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 13, 14),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 14, 15),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15, None),
    ]

    for nums, ref_num, solution in test_cases:

        root = sorted_array_to_bst(nums)
        ref_node = find_in_bst(root, ref_num)

        res = iterative(ref_node)
        result = res.data if res else None

        string = f" iterative{nums, ref_num} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

    # case = -1
    # arr = test_cases[case][0]
    # root = sorted_array_to_bst(arr)
    # printTree(root)
    # # print('Validate BST:', recursion(root))
