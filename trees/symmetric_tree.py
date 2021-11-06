"""
https://leetcode.com/problems/symmetric-tree/
Given the root of a binary tree, check whether it is a mirror 
of itself (i.e., symmetric around its center).
 
Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
"""
from collections import deque

import sys

sys.path.insert(1, "./")

from tree_node import TreeNode, list_traversal_to_bt


def recursion(root: TreeNode):
    def f(left: TreeNode, right: TreeNode) -> bool:
        # Recursive function

        # Base cases
        if not left and not right:
            # Symmetric structure
            return True
        if not left or not right:
            # Not symmetric structure
            return False
        if left.data != right.data:
            # Not symmetric data
            return False

        # Recursive call
        return f(left.left, right.right) and f(left.right, right.left)

    if not root:
        # If there's no tree, consider it symmetric
        return True

    # Recursive call to check children nodes
    return f(root.left, root.right)


def iterative(root: TreeNode):
    if not root:
        # If there's no tree, consider it symmetric
        return True

    # Stacks to keep track of the nodes
    left_stack = deque([root.left])
    right_stack = deque([root.right])

    # Loop over the nodes of both trees at the same time
    while len(left_stack) and len(right_stack):
        # Pointer to the current nodes
        left = left_stack.pop()
        right = right_stack.pop()

        if not left and not right:
            # Symmetric structure, leaf reached,
            # so continue with next iteration
            continue
        elif not left or not right:
            # Not symmetric structure
            return False
        elif left.data != right.data:
            # Not symmetric data
            return False

        # Add children to the stack in the proper order to compare:
        #   left.left  and right.right
        #   left.right and right.left
        left_stack.append(left.right)
        left_stack.append(left.left)
        right_stack.append(right.left)
        right_stack.append(right.right)

    # If both stacks are empty, the tree is symmetric
    return len(left_stack) == len(right_stack)


if __name__ == "__main__":
    print("-" * 60)
    print("Is Binary Tree symmetric?")
    print("-" * 60)

    test_cases = [
        ([], True),
        ([1], True),
        ([1, 2], False),
        ([1, 2, 2], True),
        ([1, 2, 3], False),
        ([1, 2, 1], False),
    ]

    for nums, solution in test_cases:

        root = list_traversal_to_bt(nums)
        result = recursion(root)
        string = f" recursion({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = iterative(root)
        string = f"iterative({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
