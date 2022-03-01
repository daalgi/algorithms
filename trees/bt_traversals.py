"""
BINARY TREE TRAVERSALS

See individual algorithms in their respective files:
- bt_preorder_traversal.py
- bt_inorder_traversal.py
- bt_postorder_traversal.py
"""
from collections import deque
from typing import List
import sys

sys.path.insert(1, "./")

from tree_node import (
    TreeNode,
    list_traversal_to_bt,
    print_tree,
)


def preorder_recursion(root: TreeNode) -> List[int]:
    def helper(node: TreeNode):
        if not node:
            return
        res.append(node.data)
        helper(node.left)
        helper(node.right)

    res = []
    helper(root)
    return res


def preorder(root: TreeNode) -> List[int]:
    res = []
    stack = deque([root])
    while stack:
        node = stack.pop()
        res.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res


def inorder_recursion(root: TreeNode) -> List[int]:
    def helper(node: TreeNode):
        if not node:
            return
        helper(node.left)
        res.append(node.data)
        helper(node.right)

    res = []
    helper(root)
    return res


def inorder(root: TreeNode) -> List[int]:
    res = []
    curr, stack = root, deque()
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.data)
        curr = curr.right
    return res


def postorder_recursion(root: TreeNode) -> List[int]:
    def helper(node: TreeNode):
        if not node:
            return
        helper(node.left)
        helper(node.right)
        res.append(node.data)

    res = []
    helper(root)
    return res


def postorder(root: TreeNode) -> List[int]:
    res = []
    # Stack (node, visited)
    stack = deque([(root, False)])
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                res.append(node.data)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

    return res


def bfs(root: TreeNode) -> List[int]:
    res, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        res.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Binary Tree traversals")
    print("-" * 60)

    test_cases = [
        ([1, 2, 3]),
        ([1, 2, 3, 4, 5, 6, 7]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
    ]

    for nums in test_cases:

        root = list_traversal_to_bt(nums)
        print("Binary Tree:")
        print_tree(root)

        result = preorder_recursion(root)
        output = f"\n preorder_recursion = "
        output += str(result)
        print(output)

        result = preorder(root)
        output = f"           preorder = "
        output += str(result)
        print(output)

        result = inorder_recursion(root)
        output = f"\n  inorder_recursion = "
        output += str(result)
        print(output)

        result = inorder(root)
        output = f"            inorder = "
        output += str(result)
        print(output)

        result = postorder_recursion(root)
        output = f"\npostorder_recursion = "
        output += str(result)
        print(output)

        result = postorder(root)
        output = f"          postorder = "
        output += str(result)
        print(output)

        result = bfs(root)
        output = f"\n                bfs = "
        output += str(result)
        print(output)

        print()
