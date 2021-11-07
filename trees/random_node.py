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


class TreeNode:
    pass


@dataclass
class TreeNodeV1(TreeNode):
    data: int
    left = None
    right = None
    left_size: int = 0


@dataclass
class BinaryTreeV1:
    root: TreeNodeV1 = None
    size: int = 0

    def insert(self, data: int) -> TreeNodeV1:
        if not self.root:
            self.root = TreeNodeV1(data)
            self.size += 1
            return self.root

        queue = deque([self.root])
        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            else:
                node.left = TreeNodeV1(data)
                self.size += 1
                return node.left

            if node.right:
                queue.append(node.right)
            else:
                node.right = TreeNodeV1(data)
                self.size += 1
                return node.right

    def get_random_node(self) -> TreeNodeV1:
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


@dataclass
class TreeNodeV2(TreeNode):
    data: int
    left = None
    right = None
    size: int = 1

    def insert_in_order(self, data: int):
        if data <= self.data:
            if not self.left:
                self.left = TreeNodeV2(data)
            else:
                self.left.insert_in_order(data)
        else:
            if not self.right:
                self.right = TreeNodeV2(data)
            else:
                self.right.insert_in_order(data)

        self.size += 1

    def get_ith_node(self, i: int):
        left_size = 0 if not self.left else self.left.size

        if i < left_size:
            return self.left.get_ith_node(i)
        elif i == left_size:
            return self
        return self.right.get_ith_node(i - (left_size + 1))


@dataclass
class BinaryTreeV2:
    root: TreeNodeV2 = None

    def size(self) -> int:
        return 0 if not self.root else self.root.size

    def insert_in_order(self, data: int):
        if not self.root:
            self.root = TreeNodeV2(data)
        else:
            self.root.insert_in_order(data)

    def get_random_node(self) -> TreeNodeV2:
        if not self.root:
            return None

        index = randint(0, self.size() - 1)
        return self.root.get_ith_node(index)


if __name__ == "__main__":
    print("-" * 60)
    print("Random node")
    print("-" * 60)

    print("\n>>> BinaryTreeV1 - get_random_node >> O(n)\n")
    b = BinaryTreeV1()
    for i in range(10):
        node = b.insert(i)
    print_tree(b.root)
    print()
    for i in range(20):
        print(f"Iter: {i:>2} - Random node: {b.get_random_node().data}")

    print("\n>>> BinaryTreeV2 - get_random_node >> O(logn)\n")
    b = BinaryTreeV2()
    for i in range(10):
        val = 5 if i == 0 else randint(0, 9)
        node = b.insert_in_order(val)

    print_tree(b.root)
    print()
    for i in range(20):
        print(f"Iter: {i:>2} - Random node: {b.get_random_node().data}")
