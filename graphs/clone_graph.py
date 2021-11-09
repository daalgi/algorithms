"""
https://leetcode.com/problems/clone-graph/
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a 
list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
} 

Test case format:

For simplicity, each node's value is the same as the node's 
index (1-indexed). For example, the first node with val == 1, 
the second node with val == 2, and so on. The graph is represented 
in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to 
represent a finite graph. Each list describes the set of 
neighbors of a node in the graph.

The given node will always be the first node with val = 1. 
You must return the copy of the given node as a reference to 
the cloned graph.
 

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Example 4:
Input: adjList = [[2],[1]]
Output: [[2],[1]]

Constraints:
The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""
from dataclasses import dataclass
from collections import deque


@dataclass
class Node:
    val: int
    neighbors: list = None

    def __post_init__(self):
        if self.neighbors is None:
            self.neighbors = []


def recursion_dfs(node: Node) -> list:
    # Hashtable to keep track of the cloned
    # node references { old_node: new_node }
    old_to_new = dict()

    def dfs(node: Node) -> Node:
        # Base case
        if node in old_to_new:
            # If the node has been already cloned,
            # it'll be in the hashtable,
            # return the reference to that node
            return old_to_new[node]

        # If it's a new node, clone it
        copy = Node(node.val)
        # Add the new node to the hashtable for future use
        old_to_new[node] = copy

        # Loop over the current `node` neighbors
        for neighbor in node.neighbors:
            # Copy each `neighbor` into the node `copy`.
            # Use recursion, since each node can have
            # an arbitrary number of neighbors
            copy.neighbors.append(dfs(neighbor))

        # Once the current node is completely cloned, return it
        return copy

    # Edge case: null Node
    if not Node:
        return None

    # Call recursive function
    return dfs(node)


def iter_dfs(node: Node) -> list:
    # Edge case
    if not node:
        return None

    # Hashtable to keep track of the cloned node references
    # like { old_node: new_node }, and add the first node
    cloned = {node: Node(node.val)}

    # Stack to keep track of the nodes
    stack = deque([node])

    # Loop over the nodes until the stack is empty
    while stack:
        # Pop last node of the stack
        current = stack.pop()

        # Loop over the current node neighbors
        for neighbor in current.neighbors:

            if neighbor not in cloned:
                # If the neighbor is not in the hashmap yet,
                # add it both to the stack for later iterations
                # and to the hashmap
                stack.append(neighbor)
                cloned[neighbor] = Node(neighbor.val)

            # Add neighbor to the copy
            cloned[current].neighbors.append(cloned[neighbor])

    return cloned[node]


def iter_bfs(node: Node) -> list:
    # Edge case
    if not node:
        return None

    # Hashtable to keep track of the cloned node references
    # like { old_node: new_node }, and add the first node
    cloned = {node: Node(node.val)}

    # Queue to keep track of the nodes
    queue = deque([node])

    # Loop over until the queue is empty.
    # The code is very similar to the previous algorithm `iter_dfs`,
    # but with a queue instead of a stack
    while queue:
        current = queue.popleft()

        for neighbor in current.neighbors:

            if neighbor not in cloned:
                queue.append(neighbor)
                cloned[neighbor] = Node(neighbor.val)

            cloned[current].neighbors.append(cloned[neighbor])

    return cloned[node]


def adj_list_to_node(adj: list) -> Node:
    # Returns a node in a connected undirected graph (adjacency list)
    pass


def node_to_adj_list(node: Node) -> list:
    # Returns the adjacency list of a connected undirected graph
    # from a Node
    pass


if __name__ == "__main__":
    print("-" * 60)
    print("Clone graph")
    print("-" * 60)

    test_cases = [
        # (adj_list, cloned_adj_list)
        ([[2, 4], [1, 3], [2, 4], [1, 3]], [[2, 4], [1, 3], [2, 4], [1, 3]]),
    ]

    for adj_list, solution in test_cases:

        node = adj_list_to_node(adj_list)
        res = recursion_dfs(node)
        result = node_to_adj_list(res)

        string = f"recursion{adj_list} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
