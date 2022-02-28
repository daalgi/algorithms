"""
https://leetcode.com/problems/binary-tree-preorder-traversal/

Given the root of a binary tree, return the preorder 
traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from collections import deque
from typing import List
import sys

sys.path.insert(1, "./")

from tree_node import (
    TreeNode,
    list_traversal_to_bt,
    print_tree,
)


def recursion(root: TreeNode) -> List[int]:
    # Time complexity: O(n)
    # Space complexity: O(n)

    def helper(node: TreeNode):
        if not node:
            return
        res.append(node.data)
        helper(node.left)
        helper(node.right)

    res = []
    helper(root)
    return res


def iterative(root: TreeNode) -> List[int]:
    # Time complexity: O(n)
    # Space complexity: O(n)
    if not root:
        return []
    res = []
    stack = deque([root])
    while stack:
        node = stack.pop()
        res.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Binary tree preorder traversal")
    print("-" * 60)

    test_cases = [
        ([1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 2, 4, 5, 3]),
        (
            [1, 2, None, 3, 4, 5, None, 6, 7, 8, 9, None, 10],
            [1, 2, 3, 5, 8, 9, 4, 6, 10, 7],
        ),
        (
            [1, 2, 3, 4, 5, 6, None, 7, 8, 9, None, 10],
            [1, 2, 4, 7, 8, 5, 9, 3, 6, 10],
        ),
    ]

    for nums, solution in test_cases:

        root = list_traversal_to_bt(nums)
        print("Binary Tree:")
        print_tree(root)

        result = recursion(root)
        output = f"     recursion = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = iterative(root)
        output = f"     iterative = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
