"""
https://leetcode.com/problems/same-tree/
Given the roots of two binary trees p and q, write a function 
to check if they are the same or not.

Two binary trees are considered the same if 
they are structurally identical, and the nodes 
have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""
from collections import deque

import sys

sys.path.insert(1, "./")

from tree_node import TreeNode


def recursion(p: TreeNode, q: TreeNode):
    # Base cases
    if not p and not q:
        # If both are None, same leaf, ok
        return True
    if not p or not q:
        # If only one is None, not the same leaf, not ok
        return False
    if p.data != q.data:
        # If the data is not the same, not ok
        return False

    # Recursive call to check children nodes
    return recursion(p.left, q.left) and recursion(p.right, q.right)


def iterative(p: TreeNode, q: TreeNode):
    # Stacks to keep track of the nodes
    p_stack = deque([p])
    q_stack = deque([q])

    # Loop over the nodes of both trees at the same time
    while len(p_stack) and len(q_stack):
        # Pointer to the current nodes
        cur_p = p_stack.pop()
        cur_q = q_stack.pop()

        if not cur_p and not cur_q:
            # Both trees have the same leaf,
            # continue with next iteration
            continue
        elif not cur_p or not cur_q:
            # Trees with different structure
            return False
        elif cur_p.data != cur_q.data:
            # Trees with same structure but different values
            return False

        # If both point to actual nodes,
        # add both right children
        p_stack.append(cur_p.right)
        q_stack.append(cur_q.right)

        # Add both left children last
        # (to check them immediately in next iteration)
        p_stack.append(cur_p.left)
        q_stack.append(cur_q.left)

    # If both stacks have the same length means that
    # both are empty, so both trees have the same structure
    # and their nodes have equal data
    return len(p_stack) == len(q_stack)


if __name__ == "__main__":
    print("-" * 60)
    print("Are both Binary Trees the same?")
    print("-" * 60)

    test_cases = [
        ([], [], True),
        ([1], [1], True),
        ([1, 2], [1, 2], True),
        ([1, 2], [1, 3], False),
        ([1, 2, None], [1, 2, 3], False),
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2, 1], [1, 1, 2], False),
        ([1, 2], [1, None, 2], False),
    ]

    # TODO implement array to TreeNode like LeetCode's

    # for nums, solution in test_cases:

    #     root = list_to_tree(nums)
    #     result = recursion(root)
    #     string = f" recursion({nums}) = "
    #     string += " " * (35 - len(string))
    #     string += str(result)
    #     string += " " * (60 - len(string))
    #     print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
