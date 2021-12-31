"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

A path in a binary tree is a sequence of nodes where each 
pair of adjacent nodes in the sequence has an edge connecting 
them. A node can only appear in the sequence at most once. 
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum 
of any non-empty path.

Example 1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 
with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 
with a path sum of 15 + 20 + 7 = 42.
 
Constraints:
The number of nodes in the tree is in the range [1, 3 * 10^4].
-1000 <= Node.val <= 1000
"""
from functools import lru_cache
from collections import deque
import sys

sys.path.insert(1, "./")

from tree_node import (
    TreeNode,
    list_traversal_to_bt,
    print_tree,
)


def dfs(root: TreeNode) -> int:
    # Depth First Search
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Note: see `dfs_opt` for a cleaner and more efficient solution

    @lru_cache(maxsize=None)
    def _dfs(node: TreeNode, parent_added: bool) -> int:
        # Base case
        if not node:
            return float("-inf")

        if parent_added:
            # If the parent node was added to the path,
            # we have to choose only one path downwards,
            # otherwise we'd repeat the current node in the path
            return max(
                # Option 1: path edge finishes at the current node
                node.data,
                # Option 2: path continues through the left child
                node.data + _dfs(node.left, True),
                # Option 3: path continues through the right child
                node.data + _dfs(node.right, True),
            )
        # If the parent node was not added to the path
        return max(
            # Option 1: path composed only of the current node
            node.data,
            # Option 2: path starts at the current node and continues
            # through the left child
            node.data + _dfs(node.left, True),
            # Option 3: path starts at the current node and continues
            # through the right child
            node.data + _dfs(node.right, True),
            # Option 3: current node added to the path, and continues
            # to expand through both the left and right children
            node.data + _dfs(node.left, True) + _dfs(node.right, True),
            # Option 4: current node NOT added to the path, and continues
            # to explore the left child
            _dfs(node.left, False),
            # Option 5: current node NOT added to the path, and continues
            # to explore the right child
            _dfs(node.right, False),
        )

    return _dfs(root, False)


def dfs_opt(root: TreeNode) -> int:
    # Depth First Search
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Strategy: compute the

    def _dfs(node: TreeNode) -> int:
        # Variable defined outside the scope of the `_dfs` function
        nonlocal max_sum

        # Base case
        if not node:
            return 0

        # Maximum contribution of the left branch
        left = max(0, _dfs(node.left))
        # Maximum contribution of the right branch
        right = max(0, _dfs(node.right))
        # Current path, including the current node and
        # the max contributions of both the left and right branches
        current = node.data + left + right
        # Check if a new maximum has been achieved
        max_sum = max(max_sum, current)
        # Return the current node plus the maximum path of
        # one of the two branches.
        # When further exploring the children, we have to choose only
        # one path; if we chose both paths, we'd visit the current node
        # twice, which is invalid according to the problem statement.
        return node.data + max(left, right)

    max_sum = float("-inf")
    _dfs(root)
    return max_sum


if __name__ == "__main__":
    print("-" * 60)
    print("Binary tree maximum path sum")
    print("-" * 60)

    test_cases = [
        ([1], 1),
        ([-10], -10),
        ([-10, 1], 1),
        ([1, 1], 2),
        ([1, 2, 10], 13),
        ([-1, -2, 10], 10),
        ([-1, 2, 10], 11),
        ([-10, 9, 20, None, None, 15, 7], 42),
        ([-10, 9, 20, 2, None, 15, -7], 36),
        ([-10, -9, 20, 20, None, 15, -7], 36),
    ]

    for nums, solution in test_cases:

        root = list_traversal_to_bt(nums)
        print("Binary Tree:")
        print_tree(root)

        result = dfs(root)
        output = f"\t     dfs = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dfs_opt(root)
        output = f"\t dfs_opt = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
