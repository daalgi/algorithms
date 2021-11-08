"""
https://leetcode.com/problems/find-if-path-exists-in-graph/
There is a bi-directional graph with n vertices, where each vertex 
is labeled from 0 to n - 1 (inclusive). The edges in the graph are 
represented as a 2D integer array edges, where each edges[i] = [ui, vi] 
denotes a bi-directional edge between vertex ui and vertex vi. 
Every vertex pair is connected by at most one edge, and no vertex 
has an edge to itself.

You want to determine if there is a valid path that exists from 
vertex start to vertex end.

Given edges and the integers n, start, and end, return true if 
there is a valid path from start to end, or false otherwise.

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Example 2:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.

Constraints:
1 <= n <= 2 * 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= start, end <= n - 1
There are no duplicate edges.
There are no self edges.
"""
from collections import deque


def edges_to_adjacency_list(num_nodes: int, edges: list) -> list:
    # adj = [[1, 2], [0], [0, 3]]
    #   where the ith element contains the list of neighbours
    adj = [None] * num_nodes
    for edge in edges:
        nfrom, nto = edge[0], edge[1]
        # Add neighbours to the elements `nfrom` and `nto`
        if not adj[nfrom]:
            # If `nfrom` element is still empty, append a list
            adj[nfrom] = [nto]
        else:
            # If not empty, append `nto` to the existing list
            adj[nfrom].append(nto)

        if not adj[nto]:
            # If `nto` element is still empty, append a list
            adj[nto] = [nfrom]
        else:
            # If not empty, append `nfrom` to the existing list
            adj[nto].append(nfrom)

    return adj


def iterative(n: int, edges: list, start: int, end: int) -> bool:
    # Adjacency list
    adj = edges_to_adjacency_list(n, edges)
    # List of visited nodes
    visited = [False] * n
    # Stack to keep track of the nodes to be visited
    stack = deque([start])
    # Loop over while the stack is not empty
    while stack:
        # Pop the last node from the stack
        node = stack.pop()

        # Reached the end, there's a path between `start` and `end`
        if node == end:
            return True

        # If the node has already been visited, skip the code below
        if visited[node]:
            continue

        # Add current node to the list of visited nodes
        visited[node] = True

        # Loop over the neighbours of the current `node`
        for neighbour in adj[node]:
            if not visited[neighbour]:
                # If the current `neighbour` hasn't been visited yet,
                # add it to the stack for later
                stack.append(neighbour)

    # If the `end` node didn't come up in the while loop,
    # it doesn't belong to the same connected graph
    return False


def recursion(n: int, edges: list, start: int, end: int) -> bool:
    def path_exists(adj: list, visited: list, node: int, end: int) -> bool:
        # Recursive function
        # Base cases
        if node == end:
            return True
        if visited[node]:
            return False
        # Update the visited node list
        visited[node] = True
        # Loop over the current node's neighbours
        for neighbour in adj[node]:
            if path_exists(adj, visited, neighbour, end):
                # If recursive call returns True,
                # the path exists
                return True

        # If path not found yet, it doesn't exist
        return False

    # Adjacency list
    adj = edges_to_adjacency_list(n, edges)
    # List of visited nodes
    visited = [False] * n
    # Recursive call
    return path_exists(adj, visited, start, end) or False


if __name__ == "__main__":
    print("-" * 60)
    print("Find if path exists in graph")
    print("-" * 60)

    test_cases = [
        # (num_nodes, edges, start, end, path_exists)
        (3, [[0, 1], [1, 2], [2, 0]], 0, 2, True),
        (3, [[0, 1], [1, 2], [2, 0]], 1, 2, True),
        (3, [[0, 1], [1, 2], [2, 0]], 2, 0, True),
        (3, [[0, 1], [1, 2], [2, 0]], 2, 1, True),
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5, False),
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 1, 5, False),
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 2, 5, False),
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 3, 5, True),
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 4, 5, True),
    ]

    for num_nodes, edges, start, end, solution in test_cases:

        result = iterative(num_nodes, edges, start, end)
        string = f"iterative{start, end} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = recursion(num_nodes, edges, start, end)
        string = f"recursion{start, end} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
