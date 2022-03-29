"""
https://leetcode.com/problems/find-duplicate-subtrees/

Given the root of a binary tree, return all 
duplicate subtrees.

For each kind of duplicate subtrees, you only need to 
return the root node of any one of them.

Two trees are duplicate if they have the same structure 
with the same node values.

Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

Constraints:
The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
"""
from typing import List
from collections import defaultdict
import sys

sys.path.insert(1, "./")
from tree_node import (
    TreeNode,
    binary_tree_to_list,
    list_traversal_to_bt,
    print_tree,
)


def dfs_preorder(root: TreeNode) -> List[TreeNode]:
    # Time complexity: O(n²)
    # Space complexity: O(n),
    # where `n` is the number of nodes

    # Strategy: serialize each subtree as a tuple,
    # and add the tuple to a hashmap mapping
    # { tuple: [TreeNode1, TreeNode2, ...] }
    # When a tuple contains more than one element,
    # the subtree has at least a duplicate.
    # Each element in a tuple has a hash value,
    # so every time we do a tuple hash lookup,
    # it traverses the entire tree --> O(n²)

    def serialize(node: TreeNode):
        # DFS pre-order to serialize each subtree as a tuple
        if node:
            tup = node.data, serialize(node.left), serialize(node.right)
            # Add the serialization to the hashmap
            trees[tup].append(node)
            return tup

    # Store the serialized subtrees mapping them to the root
    # nodes in a hasmap
    # { serialized_subtree1: [TreeNode1, TreeNode2, ...]}
    trees = defaultdict(list)
    serialize(root)

    return [t[0] for t in trees.values() if len(t) > 1]


def dfs_preorder2(root: TreeNode) -> List[TreeNode]:
    # Time complexity: O(n)
    # Space complexity: O(n),
    # where `n` is the number of nodes

    def serialize(node: TreeNode):
        if not node:
            return "null"
        s = "%s,%s,%s" % (str(node.data), serialize(node.left), serialize(node.right))
        trees[s].append(node)

    trees = defaultdict(list)
    serialize(root)

    return [t[0] for t in trees.values() if len(t) > 1]


def dfs_preorder3(root: TreeNode) -> List[TreeNode]:
    # Time complexity: O(n)
    # Space complexity: O(n),
    # where `n` is the number of nodes

    # Improvement: add caching wrapping each tuple in
    # a `frozenset`, which does cache its hash value

    def serialize(node: TreeNode):
        # DFS pre-order to serialize each subtree as a tuple
        if node:
            tup = frozenset([node.data, serialize(node.left), serialize(node.right)])
            # Add the serialization to the hashmap
            trees[tup].append(node)
            return tup

    # Store the serialized subtrees mapping them to the root
    # nodes in a hasmap
    # { serialized_subtree1: [TreeNode1, TreeNode2, ...]}
    trees = defaultdict(list)
    serialize(root)

    return [t[0] for t in trees.values() if len(t) > 1]


if __name__ == "__main__":
    print("-" * 60)
    print("Find duplicate subtrees")
    print("-" * 60)

    bt_list = [1, 2, 3, 4, 5, 6, 7, 8, 13, 73]

    test_cases = [
        # ( list_traversal_to_bt, solution )
        ([2, 1, 1], [[1]]),
        ([2, 2, 2, 3, None, 3, None], [[2, 3], [3]]),
        ([1, 2, 3, 4, None, 2, 4, None, None, 4], [[2, 4], [4]]),
        # Test not passing for the `dfs_preorder3`
        ([0, 0, 0, 0, None, None, 0, None, None, None, 0], [[0]]),
    ]

    for nums, solution in test_cases:

        root = list_traversal_to_bt(nums)
        print_tree(root)

        res = dfs_preorder(root)
        result = []
        for r in res:
            result.append(binary_tree_to_list(r))
        output = f"    dfs_preorder = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = sorted(result) == sorted(solution)
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        res = dfs_preorder2(root)
        result = []
        for r in res:
            result.append(binary_tree_to_list(r))
        output = f"   dfs_preorder2 = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = sorted(result) == sorted(solution)
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        res = dfs_preorder3(root)
        result = []
        for r in res:
            result.append(binary_tree_to_list(r))
        output = f"   dfs_preorder3 = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = sorted(result) == sorted(solution)
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
