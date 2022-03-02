"""
https://leetcode.com/problems/minimum-distance-between-bst-nodes/

Given the root of a Binary Search Tree (BST), return the 
minimum difference between the values of any two different 
nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 10^5
"""
from collections import deque
import sys

sys.path.insert(1, "./")

from tree_node import (
    TreeNode,
    list_traversal_to_bt,
    print_tree,
)


def iterative(root: TreeNode) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Strategy: inorder traversal
    min_diff = curr_diff = float("inf")
    last_num = -float("inf")
    stack = deque([root])
    while stack:
        temp = stack.pop()
        if temp is not None:
            if isinstance(temp, TreeNode):
                stack.append(temp.right)
                stack.append(temp.data)
                stack.append(temp.left)
            else:
                curr_diff = temp - last_num
                if curr_diff < min_diff:
                    min_diff = curr_diff
                last_num = temp

    return min_diff


if __name__ == "__main__":
    print("-" * 60)
    print("Minimum distance between BST nodes")
    print("-" * 60)

    test_cases = [
        ([2, 1], 1),
        ([4, 2, 6, 1, 3], 1),
        ([1, 0, 48, None, None, 12, 49], 1),
    ]

    for nums, solution in test_cases:

        root = list_traversal_to_bt(nums)
        print("Binary Search Tree:")
        print_tree(root)

        result = iterative(root)
        output = f"     iterative = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
