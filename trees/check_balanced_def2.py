"""
CRACKING THE CODING INTERVIEW
4.4 Check Balanced (ALTERNATIVE DEFINITION OF BALANCED):
Implement a function to check if a binary tree is balanced. 

For the purposes of this question, a balanced tree is defined to be
A TREE WHERE THE MAXIMUM HEIGHT OF ANY BRANCH IS NO MORE THAN ONE MORE
THAN THE MINIMUM HEIGHT OF ANY BRANCH.
"""
from collections import deque

import sys

sys.path.insert(1, "./")

from tree_node import TreeNode, list_traversal_to_bt, print_tree


def recursion(root: TreeNode) -> bool:
    def f(node: TreeNode) -> tuple:
        # Recursive function returns a tuple (max, min),
        # which represents the maximum and minimum depths
        # below a given node

        # Base case
        if not node:
            return 0, 0

        # Recursive call
        left = tuple([1 + x for x in f(node.left)])
        right = tuple([1 + x for x in f(node.right)])

        # Maximum and minimum depths from the current node downwards
        maximum = max(left[0], right[0])
        minimum = min(left[1], right[1])
        # print(node.data, "-->", maximum, minimum)

        return maximum, minimum

    # Call the recursive function, which returns
    # a tuple (max, min) representing the maximum
    # and minimum heights
    maximum, minimum = f(root)

    # If the heights differ no more than 1,
    # it's considered a balanced tree
    # print('-->', maximum, minimum)
    return maximum - minimum <= 1


def iterative(root: TreeNode) -> bool:
    # Base case
    if not root:
        return True

    # Queue to keep track of the nodes of the tree to be visited
    queue = deque([root])
    # Keep track of the current level and the minimum depth
    # if a shorter branch is found
    level, minimum_height = 0, 0
    shorter_branch_found = False

    # Loop over until the queue is empty
    while queue:

        # Update the level
        level += 1
        # Check if a shorted branch has ben found
        if not shorter_branch_found:
            # Update it only if a shorter branch hasn't
            # been found yet
            minimum_height = level

        # Current length of the queue to bound the following loop
        n = len(queue)
        # Loop over the nodes of the current level
        for i in range(n):

            node = queue.popleft()

            if node.left:
                # If there's a left child, add it to the queue
                # for inspection in the following iteration (while loop)
                queue.append(node.left)
            if node.right:
                # If there's a right child, add it to the queue
                # for inspection in the following iteration (while loop)
                queue.append(node.right)

            if not shorter_branch_found and not node.left or not node.right:
                # If any node at the current level has not both
                # left and right children, there's a shorter branch
                shorter_branch_found = True

    # If the heights differ no more than 1,
    # it's considered a balanced tree
    # print('-->', level, minimum_height)
    return level - minimum_height <= 1


def iterative2(root: TreeNode) -> bool:
    # Base case
    if not root:
        return True

    # Queue to keep track of the nodes of the tree to be visited
    queue = deque([root])
    # Keep track of the current level and the minimum depth
    # if a shorter branch is found
    level, minimum_height = 0, 0
    shorter_branch_found = False

    # Loop over until the queue is empty
    while queue:

        # Current length of the queue to bound the following loop
        n = len(queue)

        # Update the level
        level += 1

        # Check the number of nodes in the queue,
        # and determine if there're enough to consider the
        # level "completely balanced"
        level_max_nodes = 2 ** (level - 1)
        if not shorter_branch_found and n == level_max_nodes:
            # If no shorter branch found and the level
            # is "full" of nodes, update the minimum depth equals the
            # current level
            minimum_height = level
        elif n < level_max_nodes:
            # If there are less nodes than the maximum for the level,
            # don't update the minimum_height, and change the
            # `shorter_branch_found` flag to True
            shorter_branch_found = True

        if level - minimum_height > 1:
            # Early stop if th current level is 2 steps greater than
            # the minimum height
            return False

        # Loop over the nodes of the current level
        for i in range(n):

            node = queue.popleft()

            if node.left:
                # If there's a left child, add it to the queue
                # for inspection in the following iteration (while loop)
                queue.append(node.left)
            if node.right:
                # If there's a right child, add it to the queue
                # for inspection in the following iteration (while loop)
                queue.append(node.right)

    # If the heights differ no more than 1,
    # it's considered a balanced tree
    # print('-->', level, minimum_height)
    return level - minimum_height <= 1


if __name__ == "__main__":
    print("-" * 60)
    print("Check Balanced - Strict definition")
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
        ([1, 2, 3, 4, 5, 6, None, 8], False),  # True for not-strict balanced definition
    ]

    for nums, solution in test_cases:

        root = list_traversal_to_bt(nums)

        result = recursion(root)
        string = f"recursion({nums}) = "
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

        result = iterative2(root)
        string = f"iterative2({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()

    # case = -1
    # arr = test_cases[case][0]
    # root = list_traversal_to_bt(arr)
    # print_tree(root)
    # print(recursion(root))
