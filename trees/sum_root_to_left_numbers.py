"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/

You are given the root of a binary tree containing 
digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 
represents the number 123.
Return the total sum of all root-to-leaf numbers. 
Test cases are generated so that the answer will 
fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

Constraints:
The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
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
    # Time complexity: O(n)
    # Space complexity: O(n)

    def dfs(node: TreeNode, curr_sum: int) -> int:
        nonlocal res

        if not node:
            return
        if not node.left and not node.right:
            res += curr_sum

        if node.left:
            dfs(node.left, curr_sum * 10 + node.left.data)
        if node.right:
            dfs(node.right, curr_sum * 10 + node.right.data)

    res = 0
    dfs(root, root.data)
    return res


def bfs_iterative(root: TreeNode) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    res = 0
    q = deque([([root.data], root)])
    while q:
        nums, node = q.popleft()

        if not node.left and not node.right:
            # Leaf node
            res += int("".join(str(i) for i in nums))

        if node.left:
            q.append((nums + [node.left.data], node.left))

        if node.right:
            q.append((nums + [node.right.data], node.right))

    return res


def bfs_iterative2(root: TreeNode) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    res = 0
    q = deque([(root.data, root)])
    while q:
        curr_num, node = q.popleft()

        if not node.left and not node.right:
            # Leaf node
            res += curr_num

        if node.left:
            q.append((curr_num * 10 + node.left.data, node.left))

        if node.right:
            q.append((curr_num * 10 + node.right.data, node.right))

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Sum root to leaf numbers")
    print("-" * 60)

    array = [1, 2, 3, 4, 5, 6, 7, 8]

    test_cases = [
        # ( list_traversal_to_bt, solution )
        ([1], 1),
        ([1, 2], 12),
        ([1, 2, 3], 12 + 13),
        ([4, 9, 0, 5, 1], 495 + 491 + 40),
        ([1, 2, 3, 2, None, 1], 122 + 131),
    ]

    for i, (nums, solution) in enumerate(test_cases):

        root = list_traversal_to_bt(nums)
        if i == 0 or nums != test_cases[i - 1][0]:
            print("." * 50)
            print_tree(root)

        result = dfs_recursion(root)
        output = f"      dfs_recursion = "
        output += " " * (35 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = bfs_iterative(root)
        output = f"      bfs_iterative = "
        output += " " * (35 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = bfs_iterative2(root)
        output = f"     bfs_iterative2 = "
        output += " " * (35 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
