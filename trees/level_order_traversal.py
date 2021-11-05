"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal 
of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
from collections import deque

import sys

sys.path.insert(1, "./")

from tree_node import TreeNode, list_traversal_to_bt, print_tree


def recursion(root: TreeNode, array: list = None) -> list:
    pass


def iterative(root: TreeNode) -> list:
    if not root:
        return []

    # Results list
    res = list()

    # Queue to keep track of the nodes
    queue = deque([root])

    # Loop over the nodes: BSF
    while queue:

        # Current length of the queue to limit the inner loop
        n = len(queue)
        # Level results
        level = list()

        for _ in range(n):
            node = queue.popleft()
            level.append(node.data)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        # Add level to the result
        res.append(level)

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Binary Tree level order traversal")
    print("-" * 60)

    test_cases = [
        ([], []),
        ([1], [[1]]),
        ([1, 2], [[1], [2]]),
        ([1, None, 2], [[1], [2]]),
        ([1, 2, 3], [[1], [2, 3]]),
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
    ]

    for nums, solution in test_cases:

        root = list_traversal_to_bt(nums)

        # result = recursion(root)
        # string = f" recursion({nums}) = "
        # string += " " * (35 - len(string))
        # string += str(result)
        # string += " " * (60 - len(string))
        # print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = iterative(root)
        string = f"iterative({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

    # print("\n>>>>> Binary Tree 1:")
    # case = -2
    # arr = test_cases[case][0]
    # root = list_traversal_to_bt(arr)
    # print_tree(root)
