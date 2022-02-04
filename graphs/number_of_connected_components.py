"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

You have a graph of n nodes. You are given an 
integer n and an array edges where 
edges[i] = [ai, bi] indicates that there is 
an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Constraints:
1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
"""
from typing import List
from collections import deque


def dfs_recursion(n: int, edges: List[List[int]]) -> int:
    # Time complexity: O(E + V)
    # Space complexity: O(E + V)

    def dfs(node: int) -> None:
        visited[node] = 1
        for nei in adj[node]:
            if not visited[nei]:
                dfs(nei)

    # Adjacency list
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    visited = [0] * n

    count = 0
    for node in range(n):
        if not visited[node]:
            dfs(node)
            count += 1

    return count


def bfs_iterative(n: int, edges: List[List[int]]) -> int:
    # Time complexity: O(E + V)
    # Space complexity: O(E + V)

    # Adjacency list
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    visited = [0] * n

    count = 0
    # Loop over all the nodes
    for node in range(n):

        if visited[node]:
            continue

        # For the current univisted node,
        # explore all its neighbours
        count += 1
        q = deque([node])
        while q:
            current = q.popleft()
            visited[current] = 1
            for nei in adj[current]:
                if not visited[nei]:
                    q.append(nei)

    return count


def union_find(n: int, edges: List[List[int]]) -> int:
    # Time complexity: O(E α(n))
    #   Traverse the edges: O(E)
    #   Union and find: α(n)
    #   Union and find worst case: O(n)
    #   Union and find on average: O(1)
    #   (α(n) is O(1) on average)
    # Space complexity: O(n)

    def find(x: int) -> int:
        # Disjoint set find operation
        if x == root[x]:
            return x
        root[x] = find(root[x])
        return root[x]

    root = [i for i in range(n)]
    rank = [1] * n
    for a, b in edges:
        # Disjoint set union operation
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            if rank[root_a] < rank[root_b]:
                root[root_a] = root_b
            elif rank[root_a] > rank[root_b]:
                root[root_b] = root_a
            else:
                root[root_b] = root_a
                rank[root_a] += 1
            # Two previously disjoint components
            # have become one, so subtract 1
            n -= 1
    return n


if __name__ == "__main__":
    print("-" * 60)
    print("Number of connected components")
    print("-" * 60)

    test_cases = [
        # ( n, edges, solution )
        (2, [[0, 1]], 1),
        (3, [[0, 1], [1, 2]], 1),
        (5, [[0, 1], [1, 2], [3, 4]], 2),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1),
        (6, [[0, 1], [1, 2], [3, 4], [3, 5], [5, 4]], 2),
        (7, [[0, 1], [1, 2], [3, 4], [3, 5], [5, 6]], 2),
        (6, [[0, 1], [1, 2], [3, 4], [3, 5], [5, 0]], 1),
        (8, [[0, 1], [2, 3], [3, 4], [5, 6], [5, 7]], 3),
    ]

    for n, edges, solution in test_cases:

        print("Edges:", edges)

        result = dfs_recursion(n, edges)
        output = f"   dfs_recursion = "
        output += f"{result:>4}"
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = bfs_iterative(n, edges)
        output = f"   bfs_iterative = "
        output += f"{result:>4}"
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = union_find(n, edges)
        output = f"      union_find = "
        output += f"{result:>4}"
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
