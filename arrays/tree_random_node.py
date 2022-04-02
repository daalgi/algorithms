from random import randint
from typing import List
from collections import Counter


class TreeNode:
    def __init__(self, index: int = None) -> None:
        self.index = index
        self.parent = None

    def __repr__(self) -> str:
        return str(self.index)


class Tree:
    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("`capacity` must be greater than 0")
        self.capacity = capacity
        # Prepopulated list of nodes
        self.nodes = [None] * capacity
        # Keep track of the current number of nodes
        self.size = 0
        # hashtable to keep track of the indices of the leaf nodes
        # { node: index }
        self.leaf_indices = {}

    def initialize(self) -> TreeNode:
        # Creates a root node and returns it
        self.nodes[0] = TreeNode(index=0)
        self.leaf_indices[self.nodes[0]] = 0
        self.size = 1
        return self.nodes[0]

    def add_node(self, parent: TreeNode) -> TreeNode:
        # Given a `parent` node, creates a child node
        # and returns it

        # Check if the tree is already full
        if self.size == self.capacity:
            raise ValueError("The tree is full, can't add more nodes")

        # Add the new node to the list of nodes
        new_node = TreeNode(index=self.size)
        new_node.parent = parent
        self.nodes[new_node.index] = new_node
        self.size += 1

        # Check if the parent node was a leaf node,
        # and if so, remove it
        if parent in self.leaf_indices:
            del self.leaf_indices[parent]

        # A new node will always be a leaf node
        self.leaf_indices[new_node] = new_node.index

        return new_node

    def get_random_node(self) -> TreeNode:
        index = randint(0, self.size - 1)
        return self.nodes[index]

    def get_random_leaf(self) -> TreeNode:
        leaf_index = randint(0, len(self.leaf_indices) - 1)
        nodes_index = list(self.leaf_indices.values())[leaf_index]
        return self.nodes[nodes_index]

    """Methods for testing"""

    def get_random_nodes(self, n: int) -> List[TreeNode]:
        ans = []
        for _ in range(n):
            ans.append(self.get_random_node())
        return ans

    def get_random_nodes_counter(self, n: int) -> dict:
        count = Counter()
        for _ in range(n):
            count[self.get_random_node()] += 1
        return count

    def get_random_leaf_nodes(self, n: int) -> List[TreeNode]:
        ans = []
        for _ in range(n):
            ans.append(self.get_random_leaf())
        return ans

    def get_random_leafs_counter(self, n: int) -> dict:
        count = Counter()
        for _ in range(n):
            count[self.get_random_leaf()] += 1
        return count


if __name__ == "__main__":
    print("-" * 60)
    print("Tree random nodes")
    print("-" * 60)

    capacity = 8
    tree = Tree(capacity=capacity)
    root = tree.initialize()
    print("Root node:", root.index)

    nodes = tree.get_random_nodes_counter(n=100)
    assert len(nodes) == 1
    print("Random nodes:", nodes)
    nodes = tree.get_random_leafs_counter(n=100)
    assert len(nodes) == 1
    print("Random leaf nodes:", nodes)

    print("\nParent node:", root)
    for _ in range(2):
        node = tree.add_node(parent=root)
        print(">>New node added:", node)

    nodes = tree.get_random_nodes_counter(n=10000)
    assert len(nodes) == 3
    print("\nRandom nodes:", nodes)
    nodes = tree.get_random_leafs_counter(n=10000)
    assert len(nodes) == 2
    print("Random leaf nodes:", nodes)

    for parent in tree.nodes[1:3]:
        print("\nParent node:", parent)
        for _ in range(2):
            node = tree.add_node(parent=parent)
            print(">>New node added:", node)

    nodes = tree.get_random_nodes_counter(n=10000)
    assert len(nodes) == 7
    print("\nRandom nodes:", nodes)
    nodes = tree.get_random_leafs_counter(n=10000)
    assert len(nodes) == 4
    print("Random leaf nodes:", nodes)

    parent = tree.nodes[-1]
    print("\nParent node:", parent)
    try:
        for _ in range(capacity):
            node = tree.add_node(parent=parent)
            print(">>New node added:", node)

    except:
        print("ERROR: tree capacity exceeded, can't add more nodes")
