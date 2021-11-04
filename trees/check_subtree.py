"""
CRACKING THE CODING INTERVIEW
4.10 Check Subtree:
T1 and T2 are two very large binary trees, with T1 much bigger than T2.
Create an algorithm to determine if T2 is a subtree of T1.

A tree T2 is a subtree of T1 if there exists a node in T1 such that
the subtree of n is identical to T2. That is, if you cut off the tree at
node n, the two trees would be identical.

https://leetcode.com/problems/subtree-of-another-tree/
Given the roots of two binary trees root and subRoot, return true 
if there is a subtree of root with the same structure and node 
values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node 
in tree and all of this node's descendants. The tree tree could 
also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
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


def recursion(root1: TreeNode, root2: TreeNode) -> bool:
    def is_subtree(r1: TreeNode, r2: TreeNode) -> bool:
        if not r1:
            # Empty "big tree"
            return False

        if r1.data == r2.data and match_tree(r1, r2):
            return True

        return is_subtree(r1.left, r2) or is_subtree(r1.right, r2)

    def match_tree(r1: TreeNode, r2: TreeNode) -> bool:
        if not r1 and not r2:
            # Both trees reached the leaves
            return True
        if not r1 or not r2:
            # One tree reached the leaf while the other didn't
            return True
        if r1.data != r2.data:
            # Data doesn't match
            return False
        # Recursive call to check children
        return match_tree(r1.left, r2.left) and match_tree(r1.right, r2.right)

    # Before starting, check a base case
    if not root2:
        # An empty tree is always a subtree
        return True

    # Start recursive algorithm
    return is_subtree(root1, root2)


if __name__ == "__main__":
    print("-" * 60)
    print("Check Subtree")
    print("-" * 60)

    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8], [1], True),
        ([1, 2, 3, 4, 5, 6, 7, 8], [3], True),
        ([1, 2, 3, 4, 5, 6, 7, 8], [5], True),
        ([1, 2, 3, 4, 5, 6, 7, 8], [7, 8], True),
        ([1, 2, 3, 4, 5, 6, 7, 8], [6, 5, 7, 8], True),
        ([1, 2, 3, 4, 5, 6, 7, 8], [3, 4, 5], False),
        ([1, 2, 3, 4, 5, 6, 7, 8], [4, 6, 2], False),
        ([1, 2, 3, 4, 5, 6, 7, 8], [3, 2, 1], False),
        ([1, 2, 3, 4, 5, 6, 7, 8], [2, 3, 1], True),
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3], True),
    ]

    print("\n>>>>> Binary Tree:")
    case = 0
    arr = test_cases[case][0]
    root = sorted_array_to_bst(arr)
    printTree(root)

    for nums1, nums2, solution in test_cases:

        # TODO implement pre-order traversal for creation of tree from list
        root1 = create_binary_tree_from_list(nums1)
        root2 = create_binary_tree_from_list(nums2)
        result = recursion(root1, root2)

        string = f"recursion({nums2}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
