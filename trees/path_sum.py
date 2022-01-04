"""
https://leetcode.com/problems/path-sum/
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that 
adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false

Example 3:
Input: root = [1,2], targetSum = 0
Output: false

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""
import sys

sys.path.insert(1, "./")
from tree_node import TreeNode, list_traversal_to_bt, print_tree


def recursion(root: TreeNode, target_sum: int) -> bool:
    def f(node: TreeNode, target_sum: int) -> bool:
        # Recursive function

        # Base case
        if not node:
            if target_sum == 0:
                return True
            return False

        # Update `target_sum`
        target_sum -= node.data

        # If the node has no children is a leaf,
        # then check the path sum
        if not node.left and not node.right:
            if target_sum == 0:
                return True
            return False

        # If the node has one child, check the only possible path
        if not node.left:
            return f(node.right, target_sum)
        if not node.right:
            return f(node.left, target_sum)

        # If it has both children, check both paths
        return f(node.left, target_sum) or f(node.right, target_sum)

    # Base case before starting recursive calls
    if not root:
        return False

    # Recursive calls
    return f(root, target_sum)


def recursion2(root: TreeNode, target_sum: int) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Base cases
    if not root:
        # Not a node
        return False
    if not root.left and not root.right and root.data == target_sum:
        # Leaf node which value (data) equals the
        # current `target_sum`
        return True

    target_sum -= root.data
    return (
        # Explore left subtree
        recursion2(root.left, target_sum)
        # Explore right subtree
        or recursion2(root.right, target_sum)
    )


if __name__ == "__main__":
    print("-" * 60)
    print("Path sum")
    print("-" * 60)

    test_cases = [
        ([], 0, False),
        ([1], 1, True),
        ([1, 2], 1, False),
        ([1, 2, 3], 2, False),
        ([1, 2, 3], 3, True),
        ([1, 2, 3], 4, True),
        ([1, 2, 3], 5, False),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 10, False),
    ]

    for nums, target_sum, solution in test_cases:

        print("." * 36)
        root = list_traversal_to_bt(nums)
        print_tree(root)
        print()

        result = recursion(root, target_sum)
        string = f"\t  recursion({target_sum}) = "
        string += " " * (20 - len(string))
        string += str(result)
        string += " " * (30 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = recursion2(root, target_sum)
        string = f"\t recursion2({target_sum}) = "
        string += " " * (20 - len(string))
        string += str(result)
        string += " " * (30 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
