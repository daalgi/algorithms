"""
https://leetcode.com/problems/insert-into-a-binary-search-tree/

You are given the root node of a binary search tree (BST) 
and a value to insert into the tree. Return the root 
node of the BST after the insertion. It is guaranteed 
that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the 
insertion, as long as the tree remains a BST after insertion. 
You can return any of them.

Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Example 3:
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]

Constraints:
The number of nodes in the tree will be in the range [0, 104].
-10^8 <= Node.val <= 10^8
All the values Node.val are unique.
-10^8 <= val <= 10^8
It's guaranteed that val does not exist in the original BST.
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


def recursion(root: TreeNode, val: int) -> TreeNode:
    # Depth First Search - Recursion
    # Time complexity: O(h)
    # Space complexity: O(h)

    if not root:
        root = TreeNode(val)

    elif root.data < val:
        if not root.right:
            root.right = TreeNode(val)
        else:
            recursion(root.right, val)

    else:
        if not root.left:
            root.left = TreeNode(val)
        else:
            recursion(root.left, val)

    return root


def recursion2(root: TreeNode, val: int) -> TreeNode:
    # Depth First Search - Recursion
    # Time complexity: O(h)
    # Space complexity: O(h)

    if not root:
        root = TreeNode(val)
    elif root.data < val:
        root.right = recursion2(root.right, val)
    else:
        root.left = recursion2(root.left, val)
    return root


def iterative(root: TreeNode, val: int) -> TreeNode:
    # Depth First Search - Iterative
    # Time complexity: O(h)
    # Space complexity: O(1)

    if not root:
        root = TreeNode(val)
        return root

    prev, curr = None, root
    while curr:
        prev = curr
        curr = curr.left if val < curr.data else curr.right

    if val < prev.data:
        prev.left = TreeNode(val)
    else:
        prev.right = TreeNode(val)

    return root


if __name__ == "__main__":
    print("-" * 60)
    print("Insert into a binary search tree")
    print("-" * 60)

    test_cases = [
        ([0], 2, [0, 2]),  # [0, None, 2]),
        ([1], 0, [1, 0]),
        ([4, 2, 7, 1, 3], 5, [4, 2, 7, 1, 3, 5]),
        (
            [40, 20, 60, 10, 30, 50, 70],
            25,
            [40, 20, 60, 10, 30, 50, 70, 25],
            # [40, 20, 60, 10, 30, 50, 70, None, None, 25],
        ),
    ]

    for nums, val, solution in test_cases:

        root = list_traversal_to_bt(nums)
        print("." * 30 + "\nBinary Tree:")
        print_tree(root)
        print()

        new_root = recursion(clone_bt(root), val)
        result = binary_tree_to_list(new_root)
        output = f"   recursion({val}) = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (65 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)
        # print_tree(new_root)

        new_root = recursion2(clone_bt(root), val)
        result = binary_tree_to_list(new_root)
        output = f"  recursion2({val}) = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (65 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)
        # print_tree(new_root)

        new_root = iterative(clone_bt(root), val)
        result = binary_tree_to_list(new_root)
        output = f"   iterative({val}) = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (65 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)
        print_tree(new_root)

        print()
