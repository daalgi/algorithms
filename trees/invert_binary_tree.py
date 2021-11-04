"""
https://leetcode.com/problems/invert-binary-tree/
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
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


def recursion(root: TreeNode) -> TreeNode:
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Strategy: invert the children of each node recursively

    def f(node: TreeNode):
        if not node:
            # If it's not a node, nothing to invert
            return
        # Invert left and right children of the current node
        node.left, node.right = node.right, node.left
        # Recursive call passing the children of the current node
        f(node.left)
        f(node.right)

    # Recursive function
    f(root)
    # Return the root
    return root


def iterative(root: TreeNode) -> TreeNode:
    if not root:
        return None

    # TODO implement


if __name__ == "__main__":
    print("-" * 60)
    print("Invert Binary Tree")
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
