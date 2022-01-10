"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given the root of a binary tree, flatten the 
tree into a "linked list":

The "linked list" should use the same TreeNode class 
where the right child pointer points to the next node 
in the list and the left child pointer is always null.
The "linked list" should be in the same order as a 
pre-order traversal of the binary tree.

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""
from collections import deque
import sys

sys.path.insert(1, "./")
from tree_node import (
    TreeNode,
    list_traversal_to_bt,
    binary_tree_to_list,
    clone_bt,
    print_tree,
)


def dfs_recursion(root: TreeNode) -> TreeNode:
    # Time complexity: O(n)
    # Space complexity: O(h)

    def dfs(node: TreeNode) -> TreeNode:
        if not node:
            return None
        
        left_tail = dfs(node.left)
        right_tail = dfs(node.right)

        if left_tail:
            # right child of the flatten left tail points 
            # to the current `node` right
            left_tail.right = node.right
            # the current `node` right child pointes to left child
            node.right = node.left
            # remove the current `node` left child pointer
            node.left = None

        last = right_tail or left_tail or node
        return last


    dfs(root)
    return root


def dfs_iterative(root: TreeNode) -> TreeNode:
    # Time complexity: O(n)
    # Space complexity: O(h)
    if not root:
        return None

    # Pre-order traversal - Iterative (using a stack)
    stack = deque([root])
    # Pointer to the head of the new tree or linked list
    head = TreeNode()
    curr = head
    while stack:
        node = stack.pop()

        curr.right = TreeNode(node.data)
        curr = curr.right

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return head.right


def dfs_iterative_opt(root: TreeNode) -> TreeNode:
    # Time complexity: O(n)
    # Space complexity: O(1)
    if not root:
        return None

    # Pre-order traversal - Iterative (using a stack)
    stack = deque([root])
    # Pointer to the head of the new tree or linked list
    head = TreeNode()
    curr = head
    while stack:
        node = stack.pop()

        curr.right = node
        curr = curr.right

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            node.left = None

    return head.right


def dfs_iterative_opt2(root: TreeNode) -> TreeNode:
    # Time complexity: O(n)
    # Space complexity: O(1)
    if not root:
        return None

    # Pre-order traversal - Iterative
    curr = root
    while curr:

        if curr.left:
            # The right side of the tree is already in place,
            # we only have to modify the `left`

            # Flatten the left subtree
            p = curr.left
            while p.right:
                p = p.right

            p.right = curr.right

            # Insert the flattened left subtree in
            # the right child, and remove the left subtree
            curr.right = curr.left
            curr.left = None

        curr = curr.right

    return root


if __name__ == "__main__":
    print("-" * 60)
    print("Path sum")
    print("-" * 60)

    array = [1, 2, 3, 4, 5, 6, 7, 8]

    test_cases = [
        # ( list_traversal_to_bt, sum, count, paths )
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 5, 3, 4, None, 6], [1, 2, 3, 4, 5, 6]),
    ]

    for i, (nums, solution) in enumerate(test_cases):

        root = list_traversal_to_bt(nums)
        if i == 0 or nums != test_cases[i - 1][0]:
            print("." * 50)
            print_tree(root)

        new_root = dfs_recursion(clone_bt(root))
        result = binary_tree_to_list(new_root) if new_root else []
        output = f"      dfs_recursion = "
        output += " " * (20 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        new_root = dfs_iterative(clone_bt(root))
        result = binary_tree_to_list(new_root) if new_root else []
        output = f"      dfs_iterative = "
        output += " " * (20 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)
        # print_tree(new_root)

        new_root = dfs_iterative_opt(clone_bt(root))
        result = binary_tree_to_list(new_root) if new_root else []
        output = f"  dfs_iterative_opt = "
        output += " " * (20 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)
        # print_tree(new_root)

        new_root = dfs_iterative_opt2(clone_bt(root))
        result = binary_tree_to_list(new_root) if new_root else []
        output = f" dfs_iterative_opt2 = "
        output += " " * (20 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)
        # print_tree(new_root)

        print()
