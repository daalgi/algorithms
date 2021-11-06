"""
CRACKING THE CODING INTERVIEW
4.4 Check Balanced (ALTERNATIVE DEFINITION OF BALANCED):
Implement a function to check if a binary tree is balanced. 

For the purposes of this question, a balanced tree is defined to be
A TREE SUCH THAT THE HEIGHTS OF THE TWO SUBTREES OF ANY NODE
NEVER DIFFER BY MORE THAN ONE.
"""
from collections import deque

import sys

sys.path.insert(1, "./")

from tree_node import TreeNode, list_traversal_to_bt, print_tree


def recursion(root: TreeNode) -> bool:
    # INEFFICIENT SOLUTION
    # Compute the heights for each subtree and
    # check if it's balanced (see definition of balanced).
    # The height is calculated repeatedly on the same nodes,
    # so the time complexity is O(n2)

    def get_height(root: TreeNode) -> int:
        # Base case
        if not root:
            # If not a node, return `-1` to compensate the `+1`
            return 0
        return max(get_height(root.left), get_height(root.right)) + 1

    def is_balanced(root: TreeNode) -> bool:
        # Base case
        if not root:
            return True

        # Height difference for the left and right branches
        # of the current subtree
        height_diff = get_height(root.left) - get_height(root.right)

        if abs(height_diff) > 1:
            # If the height difference for the current subtree
            # is more than 1, it's not balanced
            return False
        else:
            # Recursively check the children subtrees
            return is_balanced(root.left) and is_balanced(root.right)

    return is_balanced(root)


def recursion2(root: TreeNode) -> bool:
    # EFFICIENT SOLUTION
    # Instead of calculating the height at each node,
    # we can return the height of the current node in the
    # recursion function.
    # We can set it up to return a negative value -1 when there's
    # a non-balanced subtree and avoid further checks in that subtree.
    # Time complexity: O(n), n = number of nodes
    # Space complexity: O(h), h = height of the tree

    def get_height(root: TreeNode) -> int:
        # Base case
        if not root:
            return 0

        # Left subtree height
        left_height = get_height(root.left)
        # Check if the left subtree is unbalanced
        if left_height == -1:
            return -1

        # Right subtree height
        right_height = get_height(root.right)
        # Check if the right subtree is unbalanced
        if right_height == -1:
            return -1

        # Check the current subtree height difference,
        # and if it's greater than 1, pass the value -1
        # to indicate that it's not balanced
        if abs(left_height - right_height) > 1:
            return -1

        # If it's balanced, return the height of the subtree
        return max(left_height, right_height) + 1

    # Check the height of the tree, and if it's
    # different to -1, it's balanced.
    return get_height(root) != -1


def iterative(root: TreeNode) -> bool:
    # TODO
    pass


if __name__ == "__main__":
    print("-" * 60)
    print("Check Balanced")
    print("-" * 60)

    test_cases = [
        ([], True),
        ([1], True),
        ([1, 2], True),
        ([1, None, 2, None, None, 3, 4], False),
        ([1, 2, 3], True),
        ([1, 2, 3, 4, 5], True),
        ([1, 2, 3, 4, None, 5], True),
        ([1, 2, 3, 4, None, None, 5], True),
        ([1, 2, 3, 4, 5, 6, 7, 8], True),
        ([3, 9, 20, None, None, 15, 7], True),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),
        ([1, 2, 3, 4, 5, 6, None, 8], True),  # False for strict-balanced definition
    ]

    for nums, solution in test_cases:

        root = list_traversal_to_bt(nums)

        result = recursion(root)
        string = f" recursion({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = recursion2(root)
        string = f"recursion2({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        # result = iterative(root)
        # string = f"iterative({nums}) = "
        # string += " " * (35 - len(string))
        # string += str(result)
        # string += " " * (60 - len(string))
        # print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()

    # case = -1
    # arr = test_cases[case][0]
    # root = list_traversal_to_bt(arr)
    # printTree(root)
    # print('Is Binary Tree balanced?', recursion(root))
