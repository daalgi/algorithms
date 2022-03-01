"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
Given the root of a binary tree, return the inorder traversal 
of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [1,2]

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


def recursion(root: TreeNode, res: list = None):
    # Time complexity: O(n)
    # Space complexity: O(n)
    if res is None:
        res = []

    if root:
        if root.left:
            recursion(root.left, res)
        res.append(root.data)
        if root.right:
            recursion(root.right, res)

    return res


def iterative(root: TreeNode, res: list = None):
    # Time complexity: O(n)
    # Space complexity: O(n)
    res = []
    stack = deque()
    cur = root
    # Loop over the nodes of the tree while
    # current pointer is a node or the stack
    # has nodes
    while cur or len(stack):

        # Loop over until the bottom-left node
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        res.append(cur.data)
        cur = cur.right

    return res


def iterative2(root: TreeNode) -> List[int]:
    # Time complexity: O(n)
    # Space complexity: O(n)
    res = []
    stack = deque([root])
    while stack:
        temp = stack.pop()
        if temp is not None:
            if isinstance(temp, TreeNode):
                stack.append(temp.right)
                stack.append(temp.data)
                stack.append(temp.left)
            else:
                res.append(temp)
    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Binary Tree inorder traversal")
    print("-" * 60)

    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, None, 2, 3], [1, 3, 2]),
        ([1, 2], [2, 1]),
        ([1, None, 2], [1, 2]),
        ([1, 2, 3, 4, 5], [4, 2, 5, 1, 3]),
        (
            [1, 2, 3, 4, 5, 6, None, 7, 8, 9, None, 10],
            [7, 4, 8, 2, 9, 5, 1, 10, 6, 3],
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

        result = iterative2(root)
        output = f"    iterative2 = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
