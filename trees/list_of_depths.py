"""
CRACKING THE CODING INTERVIEW
4.3 List of Depths:
Given a binary tree, design an algorithm which creates
a linked list of all the nodes at each depth.
(e.g., if you havea  tree with depth D,
you'll have D linked lists)
"""
from collections import deque

import sys

sys.path.insert(1, "./")

from tree_node import TreeNode, create_binary_tree_from_list, printTree


def iterative(root: TreeNode) -> list:
    # Base case
    if not root:
        return []

    # Store the result as a list of lists
    # instead of a LinkedList of LinkedList
    # for easy testing purposes
    res = []
    # Keep track of the nodes at the current level
    queue = deque([root])
    # Loop over the nodes until the queue is empty
    while queue:
        # Current length of the queue
        n = len(queue)
        # Add a list to the list result to store
        # the data of the nodes at the current level
        res.append([])
        # Loop over the nodes in the queue at the current level
        for i in range(n):
            # Pop the first node from the queue
            node = queue.popleft()
            # Append the node.data to the result list
            res[-1].append(node.data)

            # Check if the current node has children
            # for next iteration in the while loop
            # (current for loop only reaches the nodes of
            # the current level)
            if node.left:
                # If it has a left child, add it to the queue
                queue.append(node.left)
            if node.right:
                # If it has a right child, add it to the queue
                queue.append(node.right)

    # Return the list of lists with the data of the tree per level
    return res


def recursion(root: TreeNode) -> list:
    # Results list
    res = []
    # Recursive call that modifies `res`
    f(root, res, 0)
    # Return the resulting list
    return res


def f(node: TreeNode, res: list, level: int):
    # Recursive function

    # Base case
    if not node:
        return None

    current_list = []
    if len(res) == level:
        # Level not contained in the results list `res`,
        # append it
        res.append(current_list)
    else:
        # Level already in the results list `res`,
        # get it
        current_list = res[level]

    # Add the current node to the current list
    current_list.append(node.data)
    # Add the children nodes to the next level list
    # calling the recursive function
    f(node.left, res, level + 1)
    f(node.right, res, level + 1)


if __name__ == "__main__":
    print("-" * 60)
    print("List of Depths - Linked list of all nodes at each level")
    print("-" * 60)

    test_cases = [
        ([], []),
        ([1], [[1]]),
        ([1, 2], [[1], [2]]),
        ([1, None, 2], [[1], [2]]),
        ([1, 2, 3], [[1], [2, 3]]),
        ([1, 2, 3, 4, 5], [[1], [2, 3], [4, 5]]),
        ([1, 2, 3, 4, None, 5], [[1], [2, 3], [4, 5]]),
        ([1, 2, 3, 4, None, None, 5], [[1], [2, 3], [4, 5]]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [[1], [2, 3], [4, 5, 6, 7], [8]]),
    ]

    for nums, solution in test_cases:

        root = create_binary_tree_from_list(nums)
        result = iterative(root)
        string = f"iterative({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = recursion(root)
        string = f"recursion({nums}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()

    # case = -1
    # arr = test_cases[case][0]
    # root = create_binary_tree_from_list(arr)
    # printTree(root)
    # print(iterative(root))
