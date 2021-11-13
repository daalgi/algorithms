"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
(premium)

Given `n` nodes labeled from `0` to `n - 1` and a list of undirected
edges (each edge is a pair of nodes), write a function to find the 
number of connected components in an undirected graph.

Example 1:
Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
Output: 2

Example 2:
Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
Output: 1
"""


def recursion(n: int, edges: list) -> int:
    # Edge case
    if n == 0:
        return 0

    # Build an adjacency list
    adj = [[] for _ in range(n)]
    for n1, n2 in edges:
        # Undirected edges
        adj[n1].append(n2)
        adj[n2].append(n1)

    # Set to keep track of the visited nodes
    visited = set()

    def dfs(current: int, prev: int = None):
        # DFS recursive function

        if current in visited:
            # If the current node is already visited,
            # there's a cycle, so stop the recursion
            # to avoid an infinite loop
            # (recursion maximum depth exceeded)
            return

        # Set the current node as visited
        visited.add(current)

        # Loop over the neighbors of the current node
        for neighbor in adj[current]:
            if neighbor == prev:
                # Avoid revisiting the previous node
                # due to the undirected nature of the edges
                continue

            # Explore the neighbor
            dfs(neighbor, current)

    # Keep track of the number of components
    count = 0
    # Loop over all the nodes
    for node in range(n):
        if node in visited:
            # If the node has been visited,
            # continue with next iteration
            continue

        # Recursive call to visit all the nodes
        # in the component of the current node
        dfs(node)
        count += 1

    return count


if __name__ == "__main__":
    print("-" * 60)
    print("Number of connected components in an undirected graph")
    print("-" * 60)

    test_cases = [
        # (n, edges, solution)
        (5, [[0, 1], [1, 2], [3, 4]], 2),
        (5, [[0, 1], [1, 2], [3, 4], [2, 3]], 1),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1),
        (7, [[0, 1], [2, 3], [4, 5], [5, 6]], 3),
        (7, [[0, 1], [2, 3], [4, 5], [5, 6], [5, 1]], 2),
        (7, [[0, 1], [2, 3], [4, 5], [5, 6], [5, 1], [4, 2]], 1),
        # test with cycles
        (5, [[0, 1], [1, 2], [2, 0], [3, 4]], 2),
        (7, [[0, 1], [2, 3], [4, 5], [5, 6], [5, 1], [4, 2], [4, 3]], 1),
        # repeated edges (different directions)
        (5, [[0, 1], [1, 2], [4, 3], [3, 4], [2, 3]], 1),
    ]

    for i, (n, edges, solution) in enumerate(test_cases):

        result = recursion(n, edges)
        string = f"Test {i} - recursion({n}) = "
        string += " " * (15 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
