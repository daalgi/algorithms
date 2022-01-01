"""
https://leetcode.com/problems/network-delay-time/submissions/

You are given a network of n nodes, labeled from 1 to n. 
You are also given times, a list of travel times as directed 
edges times[i] = (ui, vi, wi), where ui is the source node, 
vi is the target node, and wi is the time it takes for a signal 
to travel from source to target.

We will send a signal from a given node k. Return the time it 
takes for all the n nodes to receive the signal. If it is 
impossible for all the n nodes to receive the signal, 
return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""
from collections import defaultdict
from typing import List
import heapq


def dijkstra(times: List[List[int]], n: int, k: int) -> int:
    # Dijkstra algorithm with heap
    # Time complexity: O(ElogE)
    # Space complexity: O(V+E)

    # Given the passed `edges`, construct an adjacency list
    #   edge = [from, to, distance]
    #   adj = [[(to, time), (to, time)], [(to, time]]
    #   where the index of the list represents the `from` node
    adj = [[] for _ in range(n + 1)]
    for x, y, t in times:
        adj[x].append((y, t))

    # List with the times from `k` to each node.
    # Make it size n + 1 in order to have cleaner code
    # later on, but have to omit the node `0`,
    # which doesn't actually exist.
    time_to = [float("inf")] * (n + 1)
    time_to[0] = 0

    # List to keep track of the visited nodes
    visited = [False] * (n + 1)

    # Use a min-heap to select in O(1) time the
    # next closest node
    heap = [(0, k)]

    # Loop over while the heap is non-empty
    while heap:
        # Current node
        node_time, node = heapq.heappop(heap)

        # If it's been visited, continue with the next node
        if visited[node]:
            continue
        # Set current node as visited
        visited[node] = True

        # Update the time to get to the current node
        # (the minimum time is reached the first time the
        # node is visited)
        time_to[node] = node_time

        # Loop over the current node neighbors
        for to, to_time in adj[node]:
            # Add the cummulated time to the `to` node,
            # and the node itself
            heapq.heappush(heap, (node_time + to_time, to))

    # Get the maximum time to any node
    max_time = max(time_to)
    if max_time < float("inf"):
        return max_time
    # If there's any node not visited, the time
    # in the `time_to` list equals infinity,
    # so can't be reached given the current graph
    return -1


def dijkstra2(times: List[List[int]], n: int, k: int) -> int:
    # Dijkstra algorithm with heap
    # Time complexity: O(ElogE)
    # Space complexity: O(V+E)

    adj = defaultdict(list)
    for x, y, t in times:
        adj[x].append((y, t))

    times_to = {}

    heap = [(0, k)]
    while heap:
        node_time, node = heapq.heappop(heap)

        if node not in times_to:
            times_to[node] = node_time
            
            for to, t in adj[node]:
                heapq.heappush(heap, (node_time + t, to))

    return max(times_to.values()) if len(times_to) == n else -1


if __name__ == "__main__":
    print("-" * 60)
    print("Network delay time")
    print("-" * 60)

    test_cases = [
        # (times, n, k, solution)
        # where edge = [from, to, time]
        ([[1, 2, 1]], 2, 1, 1),
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
        ([[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]], 3, 1, 4),
    ]

    for times, n, k, solution in test_cases:

        print(f"Graph:", times)

        result = dijkstra(times, n, k)
        output = f"\t dijkstra{n, k} = "
        output += " " * (28 - len(output))
        test_ok = solution == result
        output += f"{str(result):>3}"
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dijkstra2(times, n, k)
        output = f"\tdijkstra2{n, k} = "
        output += " " * (28 - len(output))
        test_ok = solution == result
        output += f"{str(result):>3}"
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
