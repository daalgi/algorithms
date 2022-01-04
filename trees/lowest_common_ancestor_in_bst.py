"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) 
of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common 
ancestor is defined between two nodes p and q as the lowest node 
in T that has both p and q as descendants (where we allow a node 
to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""
import sys

sys.path.insert(1, "./")

from tree_node import TreeNode, sorted_array_to_bst, find_in_bst, print_tree


def iterative_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Time complexity: O(h)
    # Space complexity: O(h), where `h` is the height of the tree
    # Strategy: given the definition of Binary Search Tree,
    # and the fact that there're no repeated values,
    # we can compare the values of the nodes to know
    # if they belong to the same subtree.
    while root:
        if root.data > p.data and root.data > q.data:
            # Both nodes have values smaller than the current `root`,
            # so both are in the leftsubtree
            root = root.left

        elif root.data < p.data and root.data < q.data:
            # Both nodes have values greater than the current `root`,
            # so both are in the right subtree
            root = root.right

        else:
            # In other case, if any of the nodes is the current `root`,
            # or both nodes belong to different subtrees,
            # the LCA must be `root`
            return root


def iterative2_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Time complexity: O(h)
    # Space complexity: O(h), where `h` is the height of the tree
    while (root.data - p.data) * (root.data - q.data) > 0:
        root = (root.left, root.right)[p.data > root.data]
    return root


def recursion_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Time complexity: O(h)
    # Space complexity: O(h), where `h` is the height of the tree
    if root.data > p.data and root.data > q.data:
        return recursion_bst(root.left, p, q)
    if root.data < p.data and root.data < q.data:
        return recursion_bst(root.right, p, q)
    else:
        return root


def recursion_bt(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Time complexity: O(h)
    # Space complexity: O(h), where `h` is the height of the tree
    # Note: general case, valid for any Binary Tree (not only BST)
    # Assumption: there's no reference to parent nodes

    def covers(root: TreeNode, p: TreeNode) -> bool:
        # Recursive function to determine if a node is on
        # a the tree defined by the `root` node.
        if not root:
            return False
        if root is p:
            return True
        return covers(root.left, p) or covers(root.right, p)

    # Base case
    if root is p or root is q:
        return root

    # Determine if both nodes belong to the same subtree
    # (left child of the current `root`)
    p_is_on_left = covers(root.left, p)
    q_is_on_left = covers(root.left, q)
    if p_is_on_left != q_is_on_left:
        # If both nodes are not in the same subtree from the root,
        # the LCA is the current `root`
        return root

    # Recursively check the corresponding subtree both nodes
    # belong to
    subtree = root.left if p_is_on_left else root.right
    return recursion_bt(subtree, p, q)


if __name__ == "__main__":
    print("-" * 60)
    print("Lowest common ancestor in a a Binary Search Tree")
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

        res = iterative_bst(root, node1, node2)
        result = res.data if res else None
        string = f"  iterative_bst{num1, num2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        res = iterative2_bst(root, node1, node2)
        result = res.data if res else None
        string = f" iterative2_bst{num1, num2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        res = recursion_bt(root, node1, node2)
        result = res.data if res else None
        string = f"   recursion_bt{num1, num2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        res = recursion_bst(root, node1, node2)
        result = res.data if res else None
        string = f"  recursion_bst{num1, num2} = "
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

        res = iterative_bst(root, node1, node2)
        result = res.data if res else None
        string = f"  iterative_bst{num1, num2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        res = iterative2_bst(root, node1, node2)
        result = res.data if res else None
        string = f" iterative2_bst{num1, num2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        res = recursion_bst(root, node1, node2)
        result = res.data if res else None
        string = f"   recursion_bt{num1, num2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        res = recursion_bst(root, node1, node2)
        result = res.data if res else None
        string = f"  recursion_bst{num1, num2} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
