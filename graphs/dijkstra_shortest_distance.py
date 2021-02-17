"""
DIJKSTRA'S ALGORITHM (LAZY IMPLEMENTATION) -- SHORTEST DISTANCE
Graph: adjacency list
O(E*log(V)) time
"""
from dataclasses import dataclass
import queue


@dataclass
class Edge:
    to: int
    cost: int


def dijkstra_shortest_distance(graph: dict, start: int, verbose: bool = False):
    out = ''
    n = len(graph)
    # Visited nodes array to avoid re-visiting nodes
    visited = [False] * n
    # Keep track of the minimum distance to each node
    dist = [float('Inf')] * n
    dist[start] = 0
    # PriorityQueue of the next most promising node to visit (shortest distance)
    pq = queue.PriorityQueue()
    pq.put((0, start))   

    while not pq.empty():
        min_val, node = pq.get()
        
        if verbose:
            out = f'Current node {node} distance: {min_val}'
        
        visited[node] = True

        if dist[node] < min_val: continue

        for edge in graph[node]:
            
            if visited[edge.to]: continue

            new_dist = dist[node] + edge.cost

            if verbose:
                out += f'\n\tEdge to: {edge.to} --> new distance: {new_dist}'
            
            if new_dist < dist[edge.to]:

                if verbose:
                    out += f'\t--> Node {edge.to} distance updated!'
                
                dist[edge.to] = new_dist
                # Insert tuple (dist, node) so they're sorted by dist
                pq.put((new_dist, edge.to))

        if verbose:
            print(out)

    if verbose:
        print(f'>> Distance array: {str(dist)}')
    return dist


if __name__ == '__main__':
    print('-' * 60)
    print("Dijkstra's algorithm -- Shortest distance")
    print('-' * 60)
    
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
        (graphs[0], 0, [0, 3, 1, 4, 7]),
        (graphs[1], 0, [0, 4, 1, 7, 9, 10])
    ]

    for graph, start, solution in testcases:
        print(f'\nGraph: {graph}')
        dist = dijkstra_shortest_distance(graph, start, True)
        # print(f'Distances: {dist}')
        if solution:
            print(f'Test: {"OK" if dist == solution else "NOT OK"}\n')
        print()