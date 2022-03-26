"""
Search for an element in a binary tree (unsorted)
"""
import sys

sys.path.insert(1, "./")
from tree_node import (
    TreeNode,
    list_traversal_to_bt,
    print_tree,
)


def dfs(root: TreeNode, target: int) -> TreeNode:
    # Time complexity: O(n)
    # Space complexity: O(h)

    # Base case, not a node (reached a leaf)
    if not root:
        return None

    # Node found
    if root.data == target:
        return root

    # Explore the left subtree
    x = dfs(root.left, target)
    if x is not None:
        return x

    # Explore the right subtree
    x = dfs(root.right, target)
    if x is not None:
        return x

    # Not found
    return None


if __name__ == "__main__":
    print("-" * 60)
    print("Search elemement in binary tree")
    print("-" * 60)

    bt_list = [1, 2, 3, 4, 5, 6, 7, 8, 13, 73]

    test_cases = [
        # ( list_traversal_to_bt, sum, count, paths )
        (bt_list, 1, 1),
        (bt_list, 5, 5),
        (bt_list, 73, 73),
        (bt_list, 86, None),
    ]

    for i, (nums, target, solution) in enumerate(test_cases):

        root = list_traversal_to_bt(nums)
        if i == 0 or nums != test_cases[i - 1][0]:
            print_tree(root)

        print("Target:", target)
        res = dfs(root, target)
        output = f"    dfs_recursion = "
        output += str(res.data) if res else "None"
        output += " " * (50 - len(output))
        test_ok = res.data == solution if res else res == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
