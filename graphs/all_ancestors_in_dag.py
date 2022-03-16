"""
https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

You are given a positive integer n representing the 
number of nodes of a Directed Acyclic Graph (DAG). 
The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where 
edges[i] = [fromi, toi] denotes that there is a 
unidirectional edge from fromi to toi in the graph.

Return a list answer, where answer[i] is the list 
of ancestors of the ith node, sorted in ascending 
order.

A node u is an ancestor of another node v if u can 
reach v via a set of edges.

Example 1:
Input: n = 8, edgeList = [
    [0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
Explanation:
The above diagram represents the input graph.
- Nodes 0, 1, and 2 do not have any ancestors.
- Node 3 has two ancestors 0 and 1.
- Node 4 has two ancestors 0 and 2.
- Node 5 has three ancestors 0, 1, and 3.
- Node 6 has five ancestors 0, 1, 2, 3, and 4.
- Node 7 has four ancestors 0, 1, 2, and 3.
Example 2:


Input: n = 5, edgeList = [
    [0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Output: [[],[0],[0,1],[0,1,2],[0,1,2,3]]
Explanation:
The above diagram represents the input graph.
- Node 0 does not have any ancestor.
- Node 1 has one ancestor 0.
- Node 2 has two ancestors 0 and 1.
- Node 3 has three ancestors 0, 1, and 2.
- Node 4 has four ancestors 0, 1, 2, and 3.
 
Constraints:
1 <= n <= 1000
0 <= edges.length <= min(2000, n * (n - 1) / 2)
edges[i].length == 2
0 <= fromi, toi <= n - 1
fromi != toi
There are no duplicate edges.
The graph is directed and acyclic.
"""
from typing import List
from collections import defaultdict


def dfs(n: int, edges: List[List[int]]) -> List[List[int]]:
    # Time complexity: O(n² + E)
    # Space complexity: O(n² + E)
    # where `E` is the number of edges

    def _dfs(ancestor: int, child: int) -> None:
        # Recursive function
        # Adds `ancestor` into the corresponding ancestors
        # list for each child
        if not ans[child] or ans[child][-1] != ancestor:
            if child != ancestor:
                ans[child].append(ancestor)
            for grand_child in adj[child]:
                _dfs(ancestor, grand_child)

    # Adjacency list mapping { parent: [kid1, kid2, ...] }
    adj = defaultdict(list)
    for parent, child in edges:
        adj[parent].append(child)

    # Resulting ancestors list
    ans = [[] for _ in range(n)]

    # Traverse all the nodes
    for node in range(n):
        # Recurse to the lowest offspring
        _dfs(node, node)

    return ans


if __name__ == "__main__":
    print("-" * 60)
    print("All ancestors of a node in a DAG (directed acyclic graph)")
    print("-" * 60)

    test_cases = [
        # (n, edges, solution)
        (
            8,
            [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]],
            [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]],
        ),
        (
            5,
            [
                [0, 1],
                [0, 2],
                [0, 3],
                [0, 4],
                [1, 2],
                [1, 3],
                [1, 4],
                [2, 3],
                [2, 4],
                [3, 4],
            ],
            [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]],
        ),
    ]

    for n, edges, solution in test_cases:

        edges_str = str(edges)
        if len(edges_str) > 60:
            edges_str = edges_str[:55] + " ...]"
        print(f"Edges:", edges_str)

        result = dfs(n, edges)
        output = f"    dfs = "
        test_ok = solution == result
        res_str = str(edges)
        if len(res_str) > 35:
            res_str = res_str[:30] + " ...]"
        output += res_str
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
