"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an integer array nums where the elements are sorted in 
ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of 
the two subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""
from collections import deque
import sys

sys.path.insert(1, "./")

from tree_node import TreeNode, print_tree, binary_tree_to_list


def recursive(nums: list) -> TreeNode:
    return f(nums, 0, len(nums) - 1)


def f(nums: list, left: int, right: int) -> TreeNode:
    if left == right:
        return TreeNode(nums[left])
    elif left < right:
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = f(nums, left, mid - 1)
        node.right = f(nums, mid + 1, right)
        return node
    # Python functions implicitly return None


def iterative(nums: list) -> TreeNode:
    n = len(nums)
    
    # The root of the tree will be
    # the middle point of the array
    mid = (n - 1) // 2
    root = TreeNode(nums[mid])
    
    # Base case
    if n == 1:
        return root

    # Use a stack to emulate the recursive call stack.
    # The stack contains a tuple of values (TreeNode, left, right),
    stack = deque([(root, 0, n - 1)])
    
    # Loop over until the stack is empty
    while stack:

        # Pop the last tuple in the stack
        node, left, right = stack.pop()
        # print('\n-->', left, mid, right, '>>', node.data)
        
        # Update the `node.data` for the popped node and 
        # its boundaries `left` and `right`
        mid = (left + right) // 2
        node.data = nums[mid]

        # Check if there're still elements of the array to be added
        if mid < right:
            # If the `mid` index is less than the `right` index,
            # there're still nodes to be added to the tree in this side.
            # Create child node to the right with a default data (0),
            # which will be updated when popped from the stack
            node.right = TreeNode(0)
            # Add the child to the stack, along with the new array
            # boundaries for which the node is in the middle
            stack.append((node.right, mid + 1, right))
        
        if left < mid:
            # If the `left` index is less than the `mid` index,
            # there're still nodes to be added to the tree in this side.
            # Create child node to the left with a default data (0),
            # which will be updated when popped from the stack
            node.left = TreeNode(0)
            # Add the child to the stack, along with the new array
            # boundaries for which the node is in the middle
            node.left = TreeNode(0)
            stack.append((node.left, left, mid - 1))

    # Return the root node
    return root


if __name__ == "__main__":
    print("-" * 60)
    print("Convert sorted aray to Binary Search Tree")
    print("-" * 60)

    # TODO implement binary_tree_to_list to get
    # an equivalent resulting list as in LeetCode,
    # including None for the children not having nodes in the last depth
    test_cases = [
        ([1], [1]),
        ([1, 2], [1, 2]), # [1,None,2]
        ([1, 2, 3], [2, 1, 3]), 
        ([1, 2, 3, 4], [2, 1, 3, 4]), # [2,1,3,None,None,None,4]
        ([1, 2, 3, 4, 5], [3, 1, 4, 2, 5]), # [3,1,4,None,2,None,5]
        ([1, 2, 3, 4, 5, 6], [3, 1, 5, 2, 4, 6]), # [3,1,5,None,2,4,6]
        ([-10, -3, 0, 5, 9], [0, -10, 5, -3, 9]), # [0,-10,5,None,-3,None,9]
        ([0, 1, 2, 3, 4, 5], [2, 0, 4, 1, 3, 5]), # [2,0,4,None,1,3,5]
        ([0, 1, 2, 3, 4, 5, 6, 7, 8], [4, 1, 6, 0, 2, 5, 7, 3, 8]), # [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    ]

    for nums, solution in test_cases:

        root = recursive(nums)
        result = binary_tree_to_list(root)
        string = f"recursive({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
        
        root = iterative(nums)
        result = binary_tree_to_list(root)
        string = f"iterative({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
        
        print()