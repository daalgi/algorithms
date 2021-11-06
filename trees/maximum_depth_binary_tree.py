"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along 
the longest path from the root node down to the farthest 
leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
from collections import deque

import sys

sys.path.insert(1, "./")

from tree_node import TreeNode, list_traversal_to_bt


def recursion(node: TreeNode) -> int:
    # Base cases
    if not node:
        return 0

    # If it's a node, count it and add the children's depth: 1 + d
    # Recursive call returning the maximum depth
    return 1 + max(recursion(node.left), recursion(node.right))


def dfs_iterative(root: TreeNode) -> int:
    # Depth First Search
    # Keep track of the resulting maximum depth
    res = 0

    # Use a stack (to emulate the recursive call stack)
    # The stack will contain tuples like: (node, depth)
    stack = deque([(root, 1)])

    # Loop over unitl the stack is empty
    while stack:
        node, depth = stack.pop()

        if node:
            # If it's a node, update the depth
            res = max(res, depth)

            # Add the children to the stack
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))

    return res


def bfs_iterative(root: TreeNode) -> int:
    # Base case
    if not root:
        return 0

    # Breadth First Search:
    # Traverse each level from top to bottom
    # Keep track of the current level
    level = 0

    # Use a queue
    queue = deque([root])

    # Loop over until the queue is empty
    while queue:

        # Loop over every node in the queue
        for i in range(len(queue)):
            # Pop a node and add its children
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Once the current level has been checked,
        # increase the number of levels
        level += 1

    return level


if __name__ == "__main__":
    print("-" * 60)
    print("Maximum depth of Binary Tree")
    print("-" * 60)

    test_cases = [
        ([], 0),
        ([1], 1),
        ([1, 2], 2),
        ([1, None, 2], 2),
        ([3, 9, 20, None, None, 15, 7], 3),
    ]

    for nums, solution in test_cases:

        root = list_traversal_to_bt(nums)
        result = recursion(root)
        string = f"     recursion({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = dfs_iterative(root)
        string = f" dfs_iterative({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = bfs_iterative(root)
        string = f" bfs_iterative({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
