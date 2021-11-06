"""
CRACKING THE CODING INTERVIEW
4.9 BST Sequences:
A binary search tree was created by traersing through an array from 
left to right and inserting each element. Given a binary search tree
with distinct elements, print all possible arrays that could
have led to this tree.

Example:
Input:       2
           /   \
          1     3
Outpu: [[2, 1, 3], [2, 3, 1]]
"""
from collections import deque

import sys

sys.path.insert(1, "./")

from tree_node import TreeNode, sorted_array_to_bst, find_in_bst, print_tree



if __name__ == "__main__":
    print("-" * 60)
    print("BST sequences")
    print("-" * 60)

    test_cases = [
       
    ]

    # print("\n>>>>> Binary Tree 1:")
    # case = 0
    # arr = test_cases[case][0]
    # root = sorted_array_to_bst(arr)
    # printTree(root)

    # for nums, num1, num2, solution in test_cases[:3]:

    #     root = sorted_array_to_bst(nums)
    #     node1 = find_in_bst(root, num1)
    #     node2 = find_in_bst(root, num2)
    #     res = brute_force(node1, node2)
    #     result = res.data if res else None

    #     string = f"brute_force{num1, num2} = "
    #     string += " " * (35 - len(string))
    #     string += str(result)
    #     string += " " * (60 - len(string))
    #     print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

    #     res = sol1(node1, node2)
    #     result = res.data if res else None
    #     string = f"       sol1{num1, num2} = "
    #     string += " " * (35 - len(string))
    #     string += str(result)
    #     string += " " * (60 - len(string))
    #     print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

    #     print()

    # print("\n>>>>> Binary Tree 2:")
    # case = -1
    # arr = test_cases[case][0]
    # root = sorted_array_to_bst(arr)
    # printTree(root)

    # for nums, num1, num2, solution in test_cases[3:]:

    #     root = sorted_array_to_bst(nums)
    #     node1 = find_in_bst(root, num1)
    #     node2 = find_in_bst(root, num2)
    #     res = brute_force(node1, node2)
    #     result = res.data if res else None

    #     string = f"brute_force{num1, num2} = "
    #     string += " " * (35 - len(string))
    #     string += str(result)
    #     string += " " * (60 - len(string))
    #     print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

    #     res = sol1(node1, node2)
    #     result = res.data if res else None
    #     string = f"       sol1{num1, num2} = "
    #     string += " " * (35 - len(string))
    #     string += str(result)
    #     string += " " * (60 - len(string))
    #     print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

    #     print()