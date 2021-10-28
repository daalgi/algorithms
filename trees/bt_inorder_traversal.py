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

import sys

sys.path.insert(1, "./")

from tree_node import TreeNode


def recursion(root: TreeNode, res: list = None):
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
        res.append(cur.val)
        cur = cur.right

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
    ]

    # TODO implement array to TreeNode like LeetCode's

    # for nums, solution in test_cases:

    #     root = list_to_tree(nums)
    #     result = recursion(root)
    #     string = f" recursion({nums}) = "
    #     string += " " * (35 - len(string))
    #     string += str(result)
    #     string += " " * (60 - len(string))
    #     print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
