"""
CRACKING THE CODING INTERVIEW
4.10 Check Subtree:
T1 and T2 are two very large binary trees, with T1 much bigger than T2.
Create an algorithm to determine if T2 is a subtree of T1.

A tree T2 is a subtree of T1 if there exists a node in T1 such that
the subtree of n is identical to T2. That is, if you cut off the tree at
node n, the two trees would be identical.
"""
from collections import deque

import sys

sys.path.insert(1, "./")

from tree_node import (
    TreeNode,
    sorted_array_to_bst,
    create_binary_tree_from_list,
    printTree,
)


def recursion(root1: TreeNode, root2: TreeNode):
    def f(root1: TreeNode, root2: TreeNode, node2: TreeNode = None):

        # For convenience, if `node2` not passed and `root2` is a node,
        # force `node2 = root2`
        if root2 and not node2:
            node2 = root2

        # Base cases
        if not root1 and not node2:
            # If both trees have reached the leaves,
            # they are at least partially equal
            return True
        if not root1 or not node2:
            # If only one tree has reached a leaf, not equal
            return False

        # Recursive calls
        if root1.data == root2.data:
            # If booth `node.data` are equal, continue the
            # comparison with the children
            return f(root1.left, root2, node2.left) and f(
                root1.right, root2, node2.right
            )

        # If not equal, move on to the children of `root1` and go back
        # to the root of the second tree `root2`
        return f(root1.left, root2) or f(root1.right, root2)

    # Call the recursive function
    return f(root1, root2, node2=root2)


if __name__ == "__main__":
    print("-" * 60)
    print("Check Subtree")
    print("-" * 60)

    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8], [3, 4, 5], False),
    ]

    print("\n>>>>> Binary Tree:")
    case = 0
    arr = test_cases[case][0]
    root = sorted_array_to_bst(arr)
    printTree(root)

    for nums1, nums2, solution in test_cases[:3]:

        # TODO implement pre-order traversal for creation of tree from list
        root1 = create_binary_tree_from_list(nums1)
        root2 = create_binary_tree_from_list(nums2)
        result = recursion(root1, root2)

        string = f"recursion{nums1, nums2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
