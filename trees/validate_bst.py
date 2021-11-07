"""
CRACKING THE CODING INTERVIEW
4.5 Validate BST:
Implement a function to check if a binary tree
is a binary search tree.

https://leetcode.com/problems/validate-binary-search-tree/
Given the root of a binary tree, determine if it is a valid 
binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees. 

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
from collections import deque

import sys

sys.path.insert(1, "./")

from tree_node import TreeNode, list_traversal_to_bt, print_tree


def recursion(root: TreeNode) -> bool:
    def f(node: TreeNode, min_val: int = None, max_val: int = None) -> bool:
        # Base cases
        if not node:
            return True
        if min_val is not None and min_val >= node.data:
            return False
        if max_val is not None and max_val <= node.data:
            return False

        # Check children with recursive calls
        left = f(node.left, min_val=min_val, max_val=node.data)
        right = f(node.right, min_val=node.data, max_val=max_val)
        return left and right

    # Call the recursive function passing the root
    return f(root)


def recursion2(root: TreeNode) -> bool:
    # Assumption: the tree has no duplicate values
    # strategy: IN-ORDER TRAVERSAL

    def bst_in_order_traversal(node: TreeNode, array: list) -> list:
        if not node:
            return None
        bst_in_order_traversal(node.left, array)
        array.append(node.data)
        bst_in_order_traversal(node.right, array)

    array = []
    bst_in_order_traversal(root, array)
    n = len(array)
    for i in range(1, n):
        if array[i] <= array[i - 1]:
            return False
    return True


def iterative(root: TreeNode) -> bool:
    # Assumption: the tree has no duplicate values
    # strategy: IN-ORDER TRAVERSAL
    array = []
    stack = deque()
    curr = root
    while curr or stack:

        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        array.append(curr.data)
        curr = curr.right

    n = len(array)
    for i in range(1, n):
        if array[i] <= array[i - 1]:
            return False
    return True


def iterative2(root: TreeNode) -> bool:
    # Assumption: the tree has no duplicate values
    # strategy: IN-ORDER TRAVERSAL
    # Avoid using an array; during traversal, compare
    # the last value with the current node's
    last_value = None
    stack = deque()
    curr = root
    while curr or stack:

        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        if last_value is not None:
            if last_value >= curr.data:
                # Early stop if found a value
                # not in the proper place
                return False
        last_value = curr.data
        curr = curr.right

    return True


if __name__ == "__main__":
    print("-" * 60)
    print("Validate BST")
    print("-" * 60)

    test_cases = [
        ([], True),
        ([1], True),
        ([0, None, -1], False),
        ([1, 1], False),
        ([0, None, -1], False),
        ([1, 2], False),
        ([2, 1], True),
        ([1, 2, 3], False),
        ([2, 1, 3], True),
        ([2, 2, 3], False),
        ([2, 1, 2], False),
        ([1, 2, 3, 4, 5], False),
        ([4, 2, 6, 1, 3, 5, 7], True),
        ([4, 1, 6, 2, 3, 5, 7], False),
        ([4, 2, 6, 1, 3, 7, 5], False),
        ([1, None, 2, 3, 4], False),
        ([5, 1, 4, None, None, 3, 6], False),
        ([5, 4, 6, None, None, 3, 7], False),
    ]

    for nums, solution in test_cases:

        root = list_traversal_to_bt(nums)

        result = recursion(root)
        string = f" recursion({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        if len(nums) == len(set(nums)):
            # If the tree has no duplicate values
            result = recursion2(root)
            string = f"recursion2({nums}) = "
            string += " " * (35 - len(string))
            string += str(result)
            string += " " * (60 - len(string))
            print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

            result = iterative(root)
            string = f" iterative({nums}) = "
            string += " " * (35 - len(string))
            string += str(result)
            string += " " * (60 - len(string))
            print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

            result = iterative2(root)
            string = f"iterative2({nums}) = "
            string += " " * (35 - len(string))
            string += str(result)
            string += " " * (60 - len(string))
            print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()

    # case = -2
    # arr = test_cases[case][0]
    # root = list_traversal_to_bt(arr)
    # print_tree(root)
    # print('Validate BST:', recursion(root))
