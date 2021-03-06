"""
DIJKSTRA'S ALGORITHM (LAZY IMPLEMENTATION) -- SHORTEST PATH
Graph: adjacency list
O(E*log(V)) time
"""
from dataclasses import dataclass
import queue


@dataclass
class Edge:
    to: int
    cost: int


def dijkstra(graph: dict, start: int, verbose: bool = False):
    n = len(graph)
    # Visited nodes array to avoid re-visiting nodes
    visited = [False] * n
    # Keep track of the minimum distance to each node
    dist = [float('Inf')] * n
    dist[start] = 0    
    # PriorityQueue of the next most promising node to visit (shortest distance)
    pq = queue.PriorityQueue()
    pq.put((0, start))
    # array to track the node you took to get to the i-th node
    prev = [None] * n

    while not pq.empty():
        min_val, node = pq.get()
        
        visited[node] = True

        if dist[node] < min_val: continue

        for edge in graph[node]:
            
            if visited[edge.to]: continue

            new_dist = dist[node] + edge.cost
    
            if new_dist < dist[edge.to]:
                prev[edge.to] = node
                dist[edge.to] = new_dist
                pq.put((new_dist, edge.to))

    return (dist, prev)


def dijkstra_shortest_path(graph, start: int, end: int):
    dist, prev = dijkstra(graph, start)

    if dist[end] == float("Inf"):
        return []

    index = len(prev) - 1
    start_recording = False
    path = [end]
    while index > 0:
        if index == end:
            start_recording = True
        
        if start_recording:
            # Record the path
            current = prev[index]
            path.append(current)
            if current == start:
                break
            index = current
            
        else:
            # Keep looking for `end`
            index -= 1

    return path[::-1]



if __name__ == '__main__':
    print('-' * 60)
    print("Dijkstra's algorithm -- Shortest path")
    print('-' * 60, '\n')
    
    graphs = [
        {
            0: [Edge(1, 4), Edge(2, 1)],
            1: [Edge(3, 1)],
            2: [Edge(1, 2), Edge(3, 5)],
            3: [Edge(4, 3)],
            4: []
        }, { 
            0: [Edge(1, 5), Edge(2, 1)],
            1: [Edge(2, 2), Edge(3, 3), Edge(4, 20)],
            2: [Edge(1, 3), Edge(4, 12)],
            3: [Edge(4, 2), Edge(5, 6)],
            4: [Edge(5, 1)],
            5: []
        }
    ]

    testcases = [
        (graphs[0], 0, 4, [0, 2, 1, 3, 4]),
        (graphs[0], 0, 3, [0, 2, 1, 3]),
        (graphs[0], 4, 3, []),
        (graphs[1], 1, 5, [1, 3, 4, 5]),
        (graphs[1], 0, 3, [0, 2, 1, 3]),
    ]

    for graph, start, end, solution in testcases:
        print(f'Graph: {graph}')
        path = dijkstra_shortest_path(graph, start, end)
        print(f'Shortest path: {" -> ".join(str(p) for p in path)}')
        if solution is not None:
            print(f'Test: {"OK" if path == solution else "NOT OK"}')
        print()