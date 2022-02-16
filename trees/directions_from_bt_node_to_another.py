"""
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

You are given the root of a binary tree with n nodes. 
Each node is uniquely assigned a value from 1 to n. 
You are also given an integer startValue representing 
the value of the start node s, and a different integer 
destValue representing the value of the destination 
node t.

Find the shortest path starting from node s and ending 
at node t. Generate step-by-step directions of such 
path as a string consisting of only the uppercase 
letters 'L', 'R', and 'U'. Each letter indicates a 
specific direction:
- 'L' means to go from a node to its left child node.
- 'R' means to go from a node to its right child node.
- 'U' means to go from a node to its parent node.

Return the step-by-step directions of the shortest 
path from node s to node t.

Example 1:
Input: root = [5,1,2,3,null,6,4], 
startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

Example 2:
Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.

Constraints:
The number of nodes in the tree is n.
2 <= n <= 10^5
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue
"""
from typing import List
import sys

sys.path.insert(1, "./")
from tree_node import (
    TreeNode,
    list_traversal_to_bt,
    print_tree,
)


def dfs_common_prefix(root: TreeNode, start: int, dest: int) -> str:
    # Time complexity: O(n)
    # Space complexity: O(n)

    def dfs(node: TreeNode, target: int, path: List[str]):
        # Base case: target node found
        if node.data == target:
            return True

        if node.left and dfs(node.left, target, path):
            # If the target node is in the left subtree,
            # add "L" to the path
            path.append("L")
        elif node.right and dfs(node.right, target, path):
            # If the target node is in the right subtree,
            # add "R" to the path
            path.append("R")

        # Return the path
        return path

    # Keep track of the directions to the
    # `start` and `dest` nodes:
    # - `going_up` for the path to `start`
    # - `going_down` for the path to `dest`
    going_up, going_down = [], []
    dfs(root, start, going_up)
    dfs(root, dest, going_down)

    # Remove the common ancestors until reaching the
    # lowest common ancestor LCA
    # (only when the paths start to diverge we have
    # reached the LCA)
    while going_up and going_down and going_up[-1] == going_down[-1]:
        going_up.pop()
        going_down.pop()

    # The path to `start` is not important, only its length,
    # since we have to always go up until the LCA.
    # The path from LCA to `dest` is in reverse order
    # to the stored in `going_down`
    return "".join(["U"] * len(going_up) + going_down[::-1])


if __name__ == "__main__":
    print("-" * 60)
    print("Path sum")
    print("-" * 60)

    array = [1, 2, 3, 4, 5, 6, 7, 8]

    test_cases = [
        # ( list_traversal_to_bt, start, dest, solution )
        ([1, 2], 1, 2, "L"),
        ([1, 2], 2, 1, "U"),
        ([1, 2, 3], 2, 3, "UR"),
        ([1, 2, 3], 3, 2, "UL"),
        ([1, 2, 3], 1, 2, "L"),
        ([1, 2, 3], 1, 3, "R"),
        ([1, 2, 3], 3, 1, "U"),
        ([1, 5, 3, 2, None, 8, 7], 8, 7, "UR"),
        ([1, 5, 3, 2, None, 8, 7], 8, 2, "UULL"),
        ([5, 1, 2, 3, None, 6, 4], 3, 6, "UURL"),
        (array, 7, 1, "UU"),
        (array, 7, 6, "UL"),
        (array, 7, 3, "U"),
        (array, 7, 2, "UUL"),
        (array, 7, 8, "UULLL"),
        (array, 5, 6, "UURL"),
    ]

    for i, (nums, start, dest, solution) in enumerate(test_cases):

        root = list_traversal_to_bt(nums)
        if i == 0 or nums != test_cases[i - 1][0]:
            print("." * 50)
            print_tree(root)
        print("      Start:", start)
        print("Destination:", dest)

        result = dfs_common_prefix(root, start, dest)
        output = f"      dfs_common_prefix = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
