"""
https://leetcode.com/problems/path-sum-ii/

Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where the sum of the node 
values in the path equals targetSum. Each path should be 
returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and 
ending at any leaf node. A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
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


def dfs_recursion(root: TreeNode, target_sum: int) -> List[List[int]]:
    # Time complexity: O(n)
    # Space complexity: O(n)

    def dfs(node: TreeNode, target: int, path: List[int]):
        # Base case
        if not node:
            return

        new_target = target - node.data
        path.append(node.data)

        if not node.left and not node.right:
            # If the current node is a leaf node
            if new_target == 0:
                # If the current target is 0,
                # add the current path
                paths.append(path)
            return

        # `[:]` less efficient?
        dfs(node.left, new_target, path[:])
        dfs(node.right, new_target, path[:])
        return

    paths = []
    dfs(root, target_sum, [])
    return paths


def dfs_recursion2(root: TreeNode, target_sum: int) -> List[List[int]]:
    # Time complexity: O(n)
    # Space complexity: O(n)

    def dfs(node: TreeNode, target: int, path: List[int]):
        if node:
            if not node.left and not node.right and target == node.data:
                path.append(node.data)
                paths.append(path)
                return
            new_target = target - node.data
            dfs(node.left, new_target, path + [node.data])
            dfs(node.right, new_target, path + [node.data])

    paths = []
    dfs(root, target_sum, [])
    return paths


def bfs_iterative(root: TreeNode, target_sum: int) -> List[List[int]]:
    # Time complexity: O(n)
    # Space complexity: O(n)

    if not root:
        return []

    paths = []

    # Queue of tuples (target_sum, path, node)
    q = deque([(target_sum, [], root)])
    while q:
        target, path, node = q.popleft()

        if not node.left and not node.right and target == node.data:
            paths.append(path + [node.data])
            continue

        target -= node.data

        if node.left:
            q.append((target, path + [node.data], node.left))

        if node.right:
            q.append((target, path + [node.data], node.right))

    return paths


if __name__ == "__main__":
    print("-" * 60)
    print("Path sum")
    print("-" * 60)

    array = [1, 2, 3, 4, 5, 6, 7, 8]

    test_cases = [
        # ( list_traversal_to_bt, sum, count, paths )
        ([], 0, []),
        ([1], 1, [[1]]),
        ([1, 2], 1, []),
        ([1, 2], 3, [[1, 2]]),
        ([1, 2, 3], 2, []),
        ([1, 2, 3], 3, [[1, 2]]),
        ([1, 2, 3], 4, [[1, 3]]),
        ([1, 2, 3, 2, None, 1], 5, [[1, 2, 2], [1, 3, 1]]),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, [[5, 4, 11, 2]]),
        (array, 7, []),
        (array, 8, [[1, 2, 5]]),
        (array, 15, [[1, 2, 4, 8]]),
    ]

    for i, (nums, target_sum, paths_solution) in enumerate(test_cases):

        root = list_traversal_to_bt(nums)
        if i == 0 or nums != test_cases[i - 1][0]:
            print("." * 50)
            print_tree(root)

        result = dfs_recursion(root, target_sum)
        output = f"      dfs_recursion({target_sum}) = "
        output += " " * (35 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == paths_solution
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dfs_recursion2(root, target_sum)
        output = f"     dfs_recursion2({target_sum}) = "
        output += " " * (35 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == paths_solution
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = bfs_iterative(root, target_sum)
        output = f"      bfs_iterative({target_sum}) = "
        output += " " * (35 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == paths_solution
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
