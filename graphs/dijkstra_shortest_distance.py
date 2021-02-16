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
    n = len(graph)
    dist = [float('Inf')] * n
    dist[start] = 0
    pq = queue.PriorityQueue()
    pq.put((start, 0))
    out = ''
    while not pq.empty():
        node, min_val = pq.get()
        
        if verbose:
            out = f'Current node {node} distance: {min_val}'
        
        if dist[node] < min_val: continue

        for edge in graph[node]:
            
            new_dist = dist[node] + edge.cost

            if verbose:
                out += f'\n\tEdge to: {edge.to} --> new distance: {new_dist}'
            
            if new_dist < dist[edge.to]:

                if verbose:
                    out += f'\t--> Node {edge.to} distance updated!'
                
                dist[edge.to] = new_dist
                pq.put((edge.to, new_dist))

        if verbose:
            print(out) 

    if verbose:
        print(f'>> Distance array: {str(dist)}\n')
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
        }, 
    ]

    testcases = [
        (graphs[0], 0, [0, 3, 1, 4, 7]),
    ]

    for graph, start, solution in testcases:
        print(f'\nGraph: {graph}')
        dist = dijkstra_shortest_distance(graph, start, True)
        print(f'Distances: {dist}')
        if solution:
            print(f'Test: {"OK" if dist == solution else "NOT OK"}\n')
        print()