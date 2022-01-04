"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) 
of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest 
common ancestor is defined between two nodes p and q as the 
lowest node in T that has both p and q as descendants (where 
we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can 
be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 105].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the tree.
"""
import sys

sys.path.insert(1, "./")

from tree_node import TreeNode, list_traversal_to_bt, print_tree, find_in_bt


def iterative(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    pass


def recursive(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Time complexity: O(n)
    # Space complexity: O(h), where `h` is the height of the tree

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
    return recursive(subtree, p, q)


def recursive2(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Time complexity: O(n)
    # Space complexity: O(h), where `h` is the height of the tree

    # Base cases
    if not root:
        return None
    if root is p or root is q:
        return root

    # Explore the left and right subtrees
    left = recursive2(root.left, p, q)
    right = recursive2(root.right, p, q)

    # If both the left and right subtrees returned a node,
    # the current `root` must be the LCA.
    if left and right:
        return root

    # If only one subtree returned a node, return it upwards
    return left or right


if __name__ == "__main__":
    print("-" * 60)
    print("Lowest common ancestor in a Binary Tree")
    print("-" * 60)

    arrays = [
        list(range(1, 4)),
        list(range(1, 10)),
    ]
    test_cases = [
        # (tree_as_sorted_list, num_node1, num_node2, FCA.data)
        (arrays[0], 1, 2, 1),
        (arrays[0], 1, 3, 1),
        (arrays[0], 2, 3, 1),
        (arrays[1], 1, 2, 1),
        (arrays[1], 1, 3, 1),
        (arrays[1], 1, 8, 1),
        (arrays[1], 8, 9, 4),
        (arrays[1], 5, 9, 2),
        (arrays[1], 6, 1, 1),
        (arrays[1], 6, 7, 3),
        (arrays[1], 3, 9, 1),
        (arrays[1], 4, 8, 4),
        (arrays[1], 6, 4, 1),
    ]

    for i, (nums, num1, num2, solution) in enumerate(test_cases):

        root = list_traversal_to_bt(nums)
        node1 = find_in_bt(root, num1)
        node2 = find_in_bt(root, num2)

        if i in [0, 3]:
            print(">>> Binary Tree:")
            print_tree(root)

        # result = iterative(root, )
        # output = f"\t  iterative{num1, num2} = "
        # output += " " * (10 - len(output))
        # test_ok = solution == result
        # output += str(result)
        # output += " " * (45 - len(output))
        # output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        # print(output)

        result = recursive(root, node1, node2)
        result = result.data
        output = f"\t  recursive{num1, num2} = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = recursive2(root, node1, node2)
        result = result.data
        output = f"\t recursive2{num1, num2} = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
