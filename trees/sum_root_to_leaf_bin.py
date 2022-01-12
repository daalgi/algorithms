"""
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

You are given the root of a binary tree where each 
node has a value 0 or 1. Each root-to-leaf path 
represents a binary number starting with the most 
significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, 
then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers 
represented by the path from the root to that leaf. 
Return the sum of these numbers.

The test cases are generated so that the answer fits 
in a 32-bits integer.

Example 1:
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Example 2:
Input: root = [0]
Output: 0

Constraints:
The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.
"""
from collections import deque
import sys

sys.path.insert(1, "./")

from tree_node import (
    TreeNode,
    list_traversal_to_bt,
    print_tree,
)


def dfs_recursion(root: TreeNode) -> int:
    # Depth First Search - Recursion
    # Time complexity: O(n)
    # Space complexity: O(h)

    def dfs(node: TreeNode, curr_val: int) -> int:
        # Base case: not a node, and the previous
        # node was not a leaf (only one child),
        # so don't take it into account for the total sum
        if not node:
            return 0

        # Update the passed current value
        # curr_val = curr_val << 1 | node.val
        curr_val = curr_val * 2 + node.data

        # If the current `node` is a leaf,
        # return `curr_value`
        # (which includes the update with the current `node`)
        if not node.left and not node.right:
            return curr_val

        # Continue exploring both branches
        return dfs(node.left, curr_val) + dfs(node.right, curr_val)

    return dfs(root, 0)


def dfs_iterative(root: TreeNode) -> int:
    # Depth First Search - Iterative
    # Time complexity: O(n)
    # Space complexity: O(h)

    res = 0
    # Explore the nodes of the tree using a stack
    # of tuples: (current_value, node)
    stack = deque([(root.data, root)])
    while stack:
        curr_val, node = stack.pop()

        if not node.left and not node.right:
            # If leaf node, add the number to the total sum
            res += curr_val

        # Update the current value
        curr_val <<= 1

        if node.left:
            stack.append((curr_val | node.left.data, node.left))

        if node.right:
            stack.append((curr_val | node.right.data, node.right))

    return res


def dfs_iterative2(root: TreeNode) -> int:
    # Depth First Search - Iterative
    # Time complexity: O(n)
    # Space complexity: O(h)

    res = 0
    # Explore the nodes of the tree using a stack
    # of tuples: (current_value, node)
    stack = deque([(0, root)])
    while stack:
        curr_val, node = stack.pop()

        # Update the current sum with the current node
        # curr_val = curr_val << 1 | node.data
        curr_val = curr_val * 2 + node.data

        if not node.left and not node.right:
            # If leaf node, add the number to the total sum
            res += curr_val

        if node.left:
            stack.append((curr_val, node.left))

        if node.right:
            stack.append((curr_val, node.right))

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Sum of root to leaf binary numbers")
    print("-" * 60)

    test_cases = [
        ([0], 0),
        ([1], 1),
        ([1, 0], 2),
        ([1, 0, 0], 4),
        ([1, 0, 1], 5),
        ([1, 0, 1, 0, 1, 0, 1], 22),
    ]

    for nums, solution in test_cases:

        root = list_traversal_to_bt(nums)
        print("Binary Tree:")
        print_tree(root)

        result = dfs_recursion(root)
        output = f"   dfs_recursion = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dfs_iterative(root)
        output = f"   dfs_iterative = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dfs_iterative2(root)
        output = f"  dfs_iterative2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
