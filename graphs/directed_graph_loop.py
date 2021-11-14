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

"""
from collections import defaultdict, deque


def recursion(start: list, end: list) -> bool:
    # DFS
    # Time complexity: O(V + E)

    # Build the adjacency list
    adj = defaultdict(list)
    for i in range(len(start)):
        # Directed graph: from -> to
        adj[start[i]].append(end[i])

    # Set to keep track of the visited vertices in
    # each DFS path
    visited = set()

    def dfs(vertex: int) -> bool:
        # DFS recursive function
        if vertex in visited:
            # If the vertex has been visited in the current
            # DFS path, there's a cycle
            return True

        # Check if the current vertex has neighbors
        # (no entry in the adjacency list)
        if vertex not in adj:
            # If no neighbors, finish the current DFS path
            return False

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

        # print(vertex)
        # print('adj', adj)
        # If no cycle detected for the current DFS path,
        # return False
        return False

    # print(adj)
    # Loop over all the vertices of the graph
    for vertex in adj.keys():
        if dfs(vertex):
            # If there's a cycle
            return True
    # No cycle detected
    return False


def iter_bfs(start: list, end: list) -> bool:
    # BFS

    # Set of vertices in the graph
    vertices = set()

    # Build the adjacency list
    adj = defaultdict(list)
    for i in range(len(start)):
        # Directed graph: from -> to
        adj[start[i]].append(end[i])
        vertices.add(start[i])

    # Build the indegree list to keep track of the
    # incoming edges in each vertex
    indegree = defaultdict(int)
    for v in end:
        indegree[v] += 1
        vertices.add(v)

    # Keep track of the count of vertices visited
    count = 0
    # Build a queue with the nodes without incoming edges
    # (indegree = 0)
    queue = deque([v for v in vertices if v not in indegree])
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
    if len(vertices) != count:
        # There's a cycle
        return True
    # No cycles
    return False


if __name__ == "__main__":
    print("-" * 60)
    print("Directed graph loop")
    print("-" * 60)

    test_cases = [
        # ( start, end, solution )
        ([3], [4], False),
        ([11, 10], [10, 11], True),
        ([0, 0, 2], [1, 2, 1], False),
        ([2, 2, 0, 0, 3, 4], [1, 0, 1, 3, 4, 1], False),
        ([2, 2, 0, 0, 3, 4], [1, 0, 1, 3, 4, 2], True),
        ([2, 2, 0, 0, 3, 4, 4], [1, 0, 1, 3, 4, 1, 2], True),
        ([3, 3, 3, 0, 2], [0, 1, 2, 1, 1], False),
        ([1, 3, 4, 6, 1], [3, 4, 6, 2, 5], False),
    ]

    for i, (start, end, solution) in enumerate(test_cases):

        result = recursion(start, end)
        string = f" recursion{start, end} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\n\tTest: {"OK" if solution == result else "NOT OK"}')

        result = iter_bfs(start, end)
        string = f"  iter_bfs{start, end} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\n\tTest: {"OK" if solution == result else "NOT OK"}')

        print()

    # case = -1
    # start = test_cases[case][0]
    # end = test_cases[case][1]
    # print(start, end)
    # print(iter_bfs(start, end), test_cases[case][2])
