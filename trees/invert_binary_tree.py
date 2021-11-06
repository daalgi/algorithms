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
    list_traversal_to_bt,
    binary_tree_to_list,
    print_tree,
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
        ([1, 2, 3], [1, 3, 2]),
        ([1, 3, 2], [1, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 3, 2, 5, 4]),
        ([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 7, 6, 5, 4]),
    ]

    for nums, solution in test_cases:

        print("." * 36)
        root = list_traversal_to_bt(nums)
        print_tree(root)
        print()

        res = recursion(root)
        print_tree(res)
        print()

        result = binary_tree_to_list(res)

        string = f"recursion({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
