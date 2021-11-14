"""
https://leetcode.com/problems/graph-valid-tree/
(premium)
https://www.lintcode.com/problem/178/

Given n nodes labeled from 0 to n - 1 and a list of undirected 
edges (each edge is a pair of nodes), write a function to check 
whether these edges make up a valid tree.

You can assume that no duplicate edges will appear in edges. 
Since all edges are undirected, [0, 1] is the same as [1, 0] 
and thus will not appear together in edges.

Example 1:
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.

Example 2:
Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
"""
from collections import deque


def recursion_dfs(n: int, edges: list) -> bool:
    # DFS
    # Conditions:
    # - Trees can't have cycles.
    # - Trees have to be connected (all the nodes must be connected)

    # Edge case
    if n == 0:
        return True

    # Build adjacency list from edges
    adj = [[] for _ in range(n)]
    for n1, n2 in edges:
        # Not directed edges (both ways)
        adj[n1].append(n2)
        adj[n2].append(n1)

    # Set to keep track of the visited nodes
    visited = set()

    def dfs(curr: int, prev: int) -> bool:
        # DFS recursive function

        # Base case
        if curr in visited:
            # If the current node has been visited
            # and it's not the pevious node,
            # there's a cycle in the graph
            return False

        # Add the current node to the visited set
        visited.add(curr)

        # Loop over the neighbors of the current node
        for neighbor in adj[curr]:
            if neighbor == prev:
                # If the neighbor is the previous node
                # no need to check it, skip the code below
                # for the current iteration
                continue

            if not dfs(neighbor, curr):
                # If there's a cycle, return False
                return False

        # No cycle detected
        return True

    # Start the recursive DFS from node 0 and setting prev = None
    # to go through the nodes of the graph.
    # If dfs() returns True, there're no cycles (trees are acyclic)
    # Additionally, we have to check that the number of visited
    # nodes equals the number of nodes given initially
    # (trees have all the nodes connected)
    return dfs(0, None) and len(visited) == n


def iter_bfs(n: int, edges: list) -> bool:
    # BFS
    # Time complexity: O(E+V)
    # Space complexity: O(E+V)

    # Edge case
    if len(edges) != n - 1:
        # Trees have exactly n-1 edges, so if this is not
        # satified, it can't be a tree
        return False

    # Build an adjacency list
    adj = [[] for _ in range(n)]
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    # List of the visited nodes,
    # initialized to False for the `n` nodes
    visited = [False] * n
    # Initialize the queue with the nodes with only one
    # incoming edge (for undirected graphs)
    queue = deque([0])
    # Loop over the nodes in the queue until the queue is empty
    while queue:
        # Pop next node from the queue
        curr = queue.popleft()
        # Add the current node to the visited set
        visited[curr] = True
        # Loop over the current node neighbors
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                # If the neighbor hasn't been visited,
                # add it to the queue
                queue.append(neighbor)

    # If the length of visited nodes equals the total number of nodes,
    # all the nodes are connected, so it can be a tree.
    return n == sum(visited)


if __name__ == "__main__":
    print("-" * 60)
    print("Graph valid tree")
    print("-" * 60)

    test_cases = [
        # (n, edges, solution)
        (2, [[0, 1]], True),
        (3, [[0, 1], [0, 2]], True),
        (3, [[0, 1], [0, 2], [1, 2]], False),
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
    ]

    for i, (n, edges, solution) in enumerate(test_cases):

        result = recursion_dfs(n, edges)
        string = f"recursion_dfs({i}) = "
        string += " " * (15 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = iter_bfs(n, edges)
        string = f"     iter_bfs({i}) = "
        string += " " * (15 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()

    # case = 0
    # n = test_cases[case][0]
    # edges = test_cases[case][1]
    # print(n, edges)
    # print(iter_bfs(n, edges))
