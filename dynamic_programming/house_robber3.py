"""
https://leetcode.com/problems/house-robber-iii/

The thief has found himself a new place for his thievery again. 
There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that all houses in 
this place form a binary tree. It will automatically 
contact the police if two directly-linked houses were broken 
into on the same night.

Given the root of the binary tree, return the maximum amount 
of money the thief can rob without alerting the police.

Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can 
rob = 3 + 3 + 1 = 7.

Example 2:
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can 
rob = 4 + 5 = 9.

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
0 <= Node.val <= 10^4
"""
from collections import defaultdict

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "trees"))
from tree_node import list_traversal_to_bt, print_tree, TreeNode


def dfs_recursion(node: TreeNode) -> int:
    # Depth First Search - Recursion
    # Time complexity: O(2^n)
    # Space complexity: O(n)

    if node is None:
        return 0

    left_max = 0
    right_max = 0
    if node.left:
        left_max = dfs_recursion(node.left.left) + dfs_recursion(node.left.right)

    if node.right:
        right_max = dfs_recursion(node.right.left) + dfs_recursion(node.right.right)

    return max(
        node.data + left_max + right_max,
        dfs_recursion(node.left) + dfs_recursion(node.right),
    )


def dp_recursion(root: TreeNode) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Use memoization to avoid repeated work:
    # dictionary { node: value }
    memo = defaultdict(int)

    def recursion(node: TreeNode) -> int:
        # Recursive function

        # Base case
        if node is None:
            return 0
        # Check if computation already done
        if node in memo:
            return memo[node]

        # Recurrence relation
        val = 0
        if node.left:
            val = recursion(node.left.left) + recursion(node.left.right)

        if node.right:
            val += recursion(node.right.left) + recursion(node.right.right)

        memo[node] = max(
            # Rob only houses in the next level
            recursion(node.left) + recursion(node.right),
            # Rob houses in the current and after-next levels
            node.data + val,
        )
        return memo[node]

    # Call the recursive function
    return recursion(root)


if __name__ == "__main__":
    print("-" * 60)
    print("House robber III")
    print("-" * 60)

    test_cases = [
        ([3, 4, 5, 1, 3, None, 1], 9),
        ([3, 2, 3, None, 3, None, 1], 7),
        ([1, 20, 3, 2, 3, 30], 50),
    ]

    for nums, solution in test_cases:

        # print(nums)
        root = list_traversal_to_bt(nums)
        print_tree(root)

        result = dfs_recursion(root)
        string = f" dfs_recursion = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = dp_recursion(root)
        string = f"  dp_recursion = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
