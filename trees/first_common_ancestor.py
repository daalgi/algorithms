"""
CRACKING THE CODING INTERVIEW
4.8 First Common Ancestor:
Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in
a data structure.
NOTE: this is not necessrily a binary search tree.
Assume every node has a reference to its parent.
"""
from collections import deque

import sys

sys.path.insert(1, "./")

from tree_node import TreeNode, sorted_array_to_bst, find_in_bst, print_tree


def brute_force(node1: TreeNode, node2: TreeNode) -> TreeNode:
    # Note: can't use data structures to store nodes
    # Use two pointers to check when they point to the same node.
    # Loop over moving the pointers to the respective parent nodes
    # until the first common ancestor is found.
    # Time complexity: O(logm * logn), where
    # Space complexity: O(1)
    pointer1 = node1
    while pointer1:
        pointer2 = node2
        while pointer2:
            if pointer2 is pointer1:
                return pointer1
            pointer2 = pointer2.parent
        pointer1 = pointer1.parent


def sol1(node1: TreeNode, node2: TreeNode) -> TreeNode:
    # Trace `node1` and `node2` paths up until they intersect.
    # Determine the depth of each node to be able 
    # to efficiently find the First Common Ancestor. 
    # Time complexity: O(d), 
    # where `d` is the depth of the deeper node

    def depth(node: TreeNode) -> int:
        depth = 0
        while node:
            node = node.parent
            depth += 1
        return depth


    # Difference in depths of both nodes
    delta = depth(node1) - depth(node2)

    # Reference to the nodes depending on depth
    shallower = node2 if delta > 0 else node1
    deeper = node1 if delta > 0 else node2
    # After identifying the `shallower` and `deeper` nodes,
    # make `delta` positive for convenience
    delta = abs(delta)

    # Move the deeper node up to the same level of the shallower
    while delta > 0 and deeper:
        deeper = deeper.parent
        delta -= 1

    # Move up both nodes until their paths intersect
    while shallower and deeper and shallower is not deeper:
        shallower = shallower.parent
        deeper = deeper.parent

    # return shallower
    return None if not shallower or not deeper else shallower


if __name__ == "__main__":
    print("-" * 60)
    print("First common ancestor in a Binary Tree")
    print("-" * 60)

    test_cases = [
        # (tree_as_sorted_list, num_node1, num_node2, FCA.data)
        ([1, 2, 3], 1, 2, 2),
        ([1, 2, 3], 1, 3, 2),
        ([1, 2, 3], 2, 3, 2),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 2, 2),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 3, 2),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 4, 2),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 5, 5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 6, 5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 7, 5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 8, 5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 9, 5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 7, 7),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 8, 7),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 9, 7),
    ]

    print("\n>>>>> Binary Tree 1:")
    case = 0
    arr = test_cases[case][0]
    root = sorted_array_to_bst(arr)
    print_tree(root)

    for nums, num1, num2, solution in test_cases[:3]:

        root = sorted_array_to_bst(nums)
        node1 = find_in_bst(root, num1)
        node2 = find_in_bst(root, num2)
        res = brute_force(node1, node2)
        result = res.data if res else None

        string = f"brute_force{num1, num2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        res = sol1(node1, node2)
        result = res.data if res else None
        string = f"       sol1{num1, num2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()

    print("\n>>>>> Binary Tree 2:")
    case = -1
    arr = test_cases[case][0]
    root = sorted_array_to_bst(arr)
    print_tree(root)

    for nums, num1, num2, solution in test_cases[3:]:

        root = sorted_array_to_bst(nums)
        node1 = find_in_bst(root, num1)
        node2 = find_in_bst(root, num2)
        res = brute_force(node1, node2)
        result = res.data if res else None

        string = f"brute_force{num1, num2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        res = sol1(node1, node2)
        result = res.data if res else None
        string = f"       sol1{num1, num2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()