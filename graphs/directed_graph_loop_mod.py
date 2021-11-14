"""
https://www.lintcode.com/problem/1366/

Please judge whether there is a cycle in the directed graph 
with n vertices and m edges. The parameter is two int arrays. 
There is a directed edge from start[i] to end[i].

2 <= n <= 10^5
1 <= m <= 4*10^5
1 <= start[i], end[i] <= n


Example1
Input: start = [1],end = [2]
Output: "False"
Explanation:
There is only one edge 1->2, and do not form a cycle.

Example2
Input: start = [1,2,3],end = [2,3,1]
Output: "True"
Explanation:
There is a cycle 1->2->3->1.

PROBLEM STATEMENT MODIFICATION: 
Input: n = number of nodes, edges = [[0, 1], [1, 2], ...]
"""
from collections import deque


def recursion(n: int, edges: list) -> bool:
    # DFS
    # Time complexity: O(V + E)

    # Build the adjacency list
    adj = [[] for _ in range(n)]
    for n1, n2 in edges:
        # Directed graph: from -> to
        adj[n1].append(n2)

    # Set to keep track of the visited vertices in
    # each DFS path
    visited = set()

    def dfs(vertex: int) -> bool:
        # DFS recursive function
        if vertex in visited:
            # If the vertex has been visited in the current
            # DFS path, there's a cycle
            return True

        # Add the vertex to the current DFS path
        visited.add(vertex)

        # Loop over the neighbors of the current vertex
        for neighbor in adj[vertex]:
            # Explore the neighbor vertex
            if dfs(neighbor):
                # If there's a cycle
                return True

        # Remove the current vertex from the current DFS
        # path visited set
        visited.remove(vertex)

        # If no cycle detected for the current DFS path,
        # return False
        return False

    # Loop over all the vertices of the graph
    for vertex in range(n):
        if dfs(vertex):
            # If there's a cycle
            return True
    # No cycle detected
    return False


def iter_bfs(n: int, edges: list) -> bool:
    # BFS

    # Build the adjacency list
    adj = [[] for _ in range(n)]
    for n1, n2 in edges:
        adj[n1].append(n2)

    # Build the indegree list to keep track of the
    # incoming edges in each vertex
    indegree = [0] * n
    for _, n2 in edges:
        indegree[n2] += 1

    # Keep track of the count of vertices visited
    count = 0
    # Build a queue with the nodes without incoming edges
    # (indegree = 0)
    queue = deque([v for v in range(n) if indegree[v] == 0])
    # Loop over the vertices until the queue is empty
    while queue:
        # Pop the next vertex to be "removed" from the graph
        vertex = queue.popleft()
        # Update the visited node's count
        count += 1
        # Loop over the current vertex neighbors
        for neighbor in adj[vertex]:
            # Remove the edge from the current vertex
            # to the current neighbor
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                # If the current neighbor has no incoming edges
                # append it to the queue
                queue.append(neighbor)

    # Once the loop has finished, if the visited nodes
    # is less than the given total number of nodes `n`,
    # there was a loop that emptied the queue before
    # reaching all the nodes in the graph
    if n != count:
        # There's a cycle
        return True
    # No cycles
    return False


if __name__ == "__main__":
    print("-" * 60)
    print("Directed graph loop (modified)")
    print("-" * 60)

    test_cases = [
        # ( num_projects, dependencies, solution )
        (2, [[1, 0]], False),
        (2, [[1, 0], [0, 1]], True),
        (3, [[0, 1], [2, 1], [2, 0]], False),
        (5, [[0, 1], [2, 1], [2, 0], [0, 3], [3, 4], [4, 2]], True),
        (5, [[0, 1], [2, 1], [2, 0], [0, 3], [3, 4], [4, 1]], False),
        (4, [[0, 1], [2, 1], [2, 0], [3, 0], [3, 1], [3, 2]], False),
    ]

    for i, (n, edges, solution) in enumerate(test_cases):

        result = recursion(n, edges)
        string = f" recursion{edges} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\n\tTest: {"OK" if solution == result else "NOT OK"}')

        result = iter_bfs(n, edges)
        string = f"  iter_bfs{n, edges} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\n\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
