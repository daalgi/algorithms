"""
DIJKSTRA'S ALGORITHM: shortest path between two nodes.
Hypotheses:
- Connected graph.
- Edges with non-negative weights.
Notes:
- Works for both directed and undirected graphs.
- Works with cycles.

"""
import sys

sys.path.insert(1, "./")

from typing import List
from collections import defaultdict
import heapq


def min_distance(edges: List[List[int]], source: int, destination: int) -> int:
    # Time complexity: O(E VlogV)
    # Space complexity: O(V+E)

    # Given the passed `edges`, construct an adjacency list
    #   edge = [from, to, distance]
    #   adj = { from: [to1, to2] }
    #   distances = { (from, to): distance }
    adj = defaultdict(list)
    for x, y, d in edges:
        adj[x].append((y, d))

    # Set to keep track of the visited nodes
    # (we only care about the first time we visit a node,
    # which is going to give us the shortest distance)
    visited = set()

    # Hashtable to store how we got to each node
    # { to: from }
    prev = {}

    # Use a min-heap to keep track of the next
    # closest node.
    # The heap elements are tuples: (distance, node)
    heap = [(0, source)]

    while heap:
        # Next node to visit is the one with the minimum distance
        # in the heap
        dist, node = heapq.heappop(heap)

        if node == destination:
            # If the current `to` node is the `destination`,
            # return the distance
            # (the first time we visit a node is the
            # shortest distance from `source` to that node)
            return dist, prev

        # If the node's been visited, continue with next node
        if node in visited:
            continue
        # Add the current node to the visited set
        visited.add(node)

        # Loop over the nodes to which the current
        # node is connected to
        for to, d in adj[node]:
            # Add the `to` node to the heap (cummulated_distance, to)
            heapq.heappush(heap, (dist + d, to))
            # Add the item { `to`: `node` } to the `prev` hashtable
            prev[to] = node

    return float("inf"), prev


def shortest_path(edges: List[List[int]], source: int, destination: int) -> int:
    # Get the { node_from: node_to } hashtable: `prev`
    dist, prev = min_distance(edges, source, destination)
    # Store the path in a list
    path = []
    # If it was not posible to reach the `destination`, no path
    if dist == float("inf"):
        return path

    # Loop over the nodes in the `prev` hashtable, starting from
    # the `destination` node
    node_to = destination
    path.append(destination)
    while node_to != source:
        # Get the node from where the current node `node_to` was reached,
        # and store it in the same variable
        node_to = prev[node_to]
        # Add it to the path
        path.append(node_to)

    # Return the path reversed
    return path[::-1]


if __name__ == "__main__":
    print("-" * 60)
    print("Dijkstra")
    print("-" * 60)

    test_cases = [
        # (edges, source, destination, min_dist, path)
        ([[1, 2, 8]], 1, 2, 8, [1, 2]),
        ([["A", "B", 8]], "A", "B", 8, ["A", "B"]),
        ([[1, 2, 8], [1, 3, 10], [2, 3, 1]], 1, 3, 9, [1, 2, 3]),
        ([[1, 2, 8], [1, 3, 10], [2, 4, 4], [3, 4, 1]], 1, 4, 11, [1, 3, 4]),
        ([[1, 2, 8], [1, 3, 10], [2, 4, 4], [3, 4, 1]], 1, 5, float("inf"), []),
        # with cycles
        ([[1, 2, 8], [1, 3, 10], [2, 4, 4], [3, 1, 8]], 1, 4, 12, [1, 2, 4]),
        ([[1, 2, 8], [1, 4, 15], [2, 4, 4], [4, 1, 8]], 1, 4, 12, [1, 2, 4]),
        ([[1, 2, 1], [1, 4, 10], [2, 3, 3], [3, 1, 1]], 1, 4, 10, [1, 4]),
    ]

    for edges, source, destination, dist_solution, path_solution in test_cases:

        print(f"Graph:", edges)
        dist, prev = min_distance(edges, source, destination)
        result = dist
        output = f"\tmin_distance{source, destination} = "
        output += " " * (30 - len(output))
        test_ok = dist_solution == result
        output += f"{str(result)}"
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        path = shortest_path(edges, source, destination)
        result = path
        output = f"\t        path{source, destination} = "
        output += " " * (30 - len(output))
        test_ok = path_solution == result
        output += f"{str(result)}"
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
