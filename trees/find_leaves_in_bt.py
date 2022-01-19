"""
https://leetcode.com/problems/find-leaves-of-binary-tree/

Given the root of a binary tree, collect a tree's nodes 
as if you were doing this:
- Collect all the leaf nodes.
- Remove all the leaf nodes.
- Repeat until the tree is empty.

Example 1:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered 
correct answers since per each level it does not matter 
the order on which elements are returned.

Example 2:
Input: root = [1]
Output: [[1]]

Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""
from typing import List
from collections import defaultdict
import sys

sys.path.insert(1, "./")

from tree_node import (
    TreeNode,
    list_traversal_to_bt,
    clone_bt,
    print_tree,
)


def dfs_with_sorting(root: TreeNode) -> List[List[int]]:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)

    def get_height(node: TreeNode) -> bool:
        # Depth First Search - Recursion

        # Base case
        if not node:
            return -1

        # Height of the left subtree
        left_height = get_height(node.left)
        # Height of the right subtree
        right_height = get_height(node.right)
        # Height of the current node
        curr_height = 1 + max(left_height, right_height)

        # Add the height and value of the current node
        pairs.append((curr_height, node.data))

        return curr_height

    # List of tuples to store (height, node_value)
    pairs = []
    get_height(root)

    # Sort the pairs by `height`, so we can build the
    # result list
    pairs.sort()
    res = []

    # Loop over the pairs
    n, i, height = len(pairs), 0, 0
    while i < n:
        # For the current `height`, add a list to `res`,
        # where we'll store the values of the nodes
        res.append([])

        # Loop over the nodes with the current `height`
        while i < n and pairs[i][0] == height:
            res[-1].append(pairs[i][1])
            i += 1

        height += 1

    return res


def dfs_without_sorting(root: TreeNode) -> List[List[int]]:
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Strategy: instead of sorting an auxiliary list
    # with tuples (height, node_value), directly
    # fill the resulting array as we visit the nodes

    def get_height(node: TreeNode) -> int:
        if not node:
            return -1

        left_height = get_height(node.left)
        right_height = get_height(node.right)
        curr_height = 1 + max(left_height, right_height)

        # If the `res` list has not a sublist at the
        # index `curr_height`, add it
        if len(res) == curr_height:
            res.append([])
        res[curr_height].append(node.data)

        return curr_height

    res = []
    get_height(root)
    return res


def dfs_without_sorting2(root: TreeNode) -> List[List[int]]:
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Strategy: instead of sorting an auxiliary list
    # with tuples (height, node_value), directly
    # fill the resulting array as we visit the nodes.
    # In this case, use a defaultdict

    def get_height(node: TreeNode) -> int:
        if not node:
            return -1

        left_height = get_height(node.left)
        right_height = get_height(node.right)
        curr_height = 1 + max(left_height, right_height)

        res[curr_height].append(node.data)

        return curr_height

    res = defaultdict(list)
    get_height(root)
    # Since the dictionary is not necessarily sorted by keys,
    # we have to sort it
    return [res[key] for key in sorted(res.keys())]


if __name__ == "__main__":
    print("-" * 60)
    print("Find leaves of binary tree")
    print("-" * 60)

    test_cases = [
        ([1], [[1]]),
        ([1, 2, 3, 4, 5], [[3, 4, 5], [2], [1]]),
        (
            [1, 23, 52, 12, 3, 45, 2, 3, 4, 3, 5, 5, 7, 8, 53, 45, 4, 54, 8],
            [[3, 4, 5, 5, 7, 8, 8, 45, 53, 54], [2, 3, 3, 4, 45], [12, 52], [23], [1]],
        ),
    ]

    for nums, solution in test_cases:

        sol = sorted((sorted(s) for s in solution))
        root = list_traversal_to_bt(nums)
        print("." * 30 + "\nBinary Tree:")
        print_tree(root)
        print()

        result = dfs_with_sorting(clone_bt(root))
        output = f"      dfs_with_sorting = "
        output += " " * (10 - len(output))
        test_ok = sol == sorted((sorted(r) for r in result))
        res_str = str(result)
        if len(res_str) > 35:
            res_str = res_str[:30] + " ...]"
        output += res_str
        output += " " * (65 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dfs_without_sorting(clone_bt(root))
        output = f"   dfs_without_sorting = "
        output += " " * (10 - len(output))
        test_ok = sol == sorted((sorted(r) for r in result))
        res_str = str(result)
        if len(res_str) > 35:
            res_str = res_str[:30] + " ...]"
        output += res_str
        output += " " * (65 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dfs_without_sorting2(clone_bt(root))
        output = f"  dfs_without_sorting2 = "
        output += " " * (10 - len(output))
        test_ok = sol == sorted((sorted(r) for r in result))
        res_str = str(result)
        if len(res_str) > 35:
            res_str = res_str[:30] + " ...]"
        output += res_str
        output += " " * (65 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
