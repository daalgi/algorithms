"""
CRACKING THE CODING INTERVIEW
4.11 Random node:
You are implementing a binary tree class from scratch which,
in addition to `insert`, `find`, and `delete`, has a method
`get_random_node()` which returns a random node from the tree.
All nodes should be equally likely to be chosen. Design and
implement an algorithm to`get_random_node`, and explain how you
would implement the rest of the methods.
"""
from collections import deque
from dataclasses import dataclass
from random import randint
import sys

sys.path.insert(1, "./")

from tree_node import print_tree


@dataclass
class TreeNode:
    data: int
    left = None
    right = None
    children: int = 0

    def get_ith_node(self, i: int):
        left_size = 0 if not self.left else self.left.children

        if i < left_size:
            return self.left.get_ith_node(i)
        elif i == left_size:
            return self
        return self.right.get_ith_node(i - (left_size + 1))


class BinaryTreeV1:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data: int) -> TreeNode:
        if not self.root:
            self.root = TreeNode(data)
            self.size += 1
            return self.root

        queue = deque([self.root])
        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            else:
                node.left = TreeNode(data)
                self.size += 1
                return node.left

            if node.right:
                queue.append(node.right)
            else:
                node.right = TreeNode(data)
                self.size += 1
                return node.right

    def get_random_node(self) -> TreeNode:
        # Time complexity: O(n)
        # Space complexity: O(1)

        index = randint(0, self.size - 1)

        queue = deque([self.root])

        while queue and index > -1:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            index -= 1

        return node


if __name__ == "__main__":
    print("-" * 60)
    print("Random node")
    print("-" * 60)

    b = BinaryTreeV1()
    for i in range(10):
        node = b.insert(i)
    print_tree(b.root)
    print()
    for i in range(20):
        print(f"Iter: {i:>2} - Random node: {b.get_random_node().data}")
