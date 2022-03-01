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
        helper(node.left)
        helper(node.right)
        res.append(node.data)

    res = []
    helper(root)
    return res


def iterative(root: TreeNode) -> List[int]:
    # Time complexity: O(n)
    # Space complexity: O(n)
    res = []
    stack = deque([(root, False)])
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                res.append(node.data)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

    return res


def iterative2(root: TreeNode) -> List[int]:
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Strategy: add to the stack both nodes
    # and the data of the nodes while traversing
    # the tree
    res = []
    stack = deque([root])
    while stack:
        temp = stack.pop()
        if temp is not None:
            if isinstance(temp, TreeNode):
                # If the current element of the stack is a node,
                # first, add the data
                stack.append(temp.data)
                # then, the children (right and left), so we
                # can continue exploring the tree in next iteration
                # starting from the left child
                stack.append(temp.right)
                stack.append(temp.left)
            else:
                # If the current element of the stack is not a node,
                # it's a number, add it to the traversal
                res.append(temp)

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Binary tree postorder traversal")
    print("-" * 60)

    test_cases = [
        ([1], [1]),
        ([1, 2, 3], [2, 3, 1]),
        ([1, 2, 3, 4, 5], [4, 5, 2, 3, 1]),
        (
            [1, 2, None, 3, 4, 5, None, 6, 7, 8, 9, None, 10],
            [8, 9, 5, 3, 10, 6, 7, 4, 2, 1],
        ),
        (
            [1, 2, 3, 4, 5, 6, None, 7, 8, 9, None, 10],
            [7, 8, 4, 9, 5, 2, 10, 6, 3, 1],
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
