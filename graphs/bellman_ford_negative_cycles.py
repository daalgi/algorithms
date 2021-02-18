from dataclasses import dataclass
import queue


@dataclass
class Edge:
    to: int
    cost: int


def bellman_ford(graph: dict, start: int):
    n = len(graph)
    dist = [float("Inf")] * n
    dist[start] = 0
    
    # For each vertex, apply relaxation for all the edges
    # for _ in range(n):
    for node in range(n):
        for edge in graph[node]:
            new_dist = dist[node] + edge.cost            
            if new_dist < dist[edge.to]:
                dist[edge.to] = new_dist

    # Run algo a second time to detect which nodes are part of
    # a negative cycle.
    for _ in range(n):
        for node in range(n):
            for edge in graph[node]:
                new_dist = dist[node] + edge.cost
                if new_dist < dist[edge.to]:
                    dist[edge.to] = float("-Inf")

    return dist


def bellman_ford_verbose(graph: dict, start: int):
    out = ''
    n = len(graph)
    dist = [float("Inf")] * n
    dist[start] = 0
    
    # For each vertex, apply relaxation for all the edges
    print('\n# Apply relaxation for all the edges:')
    # for _ in range(n):
    for node in range(n):

        out = f'Node {node}'

        for edge in graph[node]:
            new_dist = dist[node] + edge.cost
            
            out += f'\n\tEdge to: {edge.to} --> new distance: {new_dist:>4}'

            if new_dist < dist[edge.to]:
                dist[edge.to] = new_dist

                out += f'  --> Node {edge.to} distance updated!'

        print(out)
    print(f'>> Iteration 1 distance array: {str(dist)}')

    # Run algo a second time to detect which nodes are part of
    # a negative cycle.
    print('\n# Run the algorithm a second time to detect negative cycles:')
    for iter in range(n-1):
        print(f'>> Iteration {iter}:')
        for node in range(n):

            out = f'Node {node}'

            for edge in graph[node]:
                new_dist = dist[node] + edge.cost

                out += f'\n\tEdge to: {edge.to} --> new distance: {new_dist:>4}'

                if new_dist < dist[edge.to]:
                    dist[edge.to] = float("-Inf")

                    out += f'  --> Node {edge.to} updated to -Inf!'
                
            print(out)
        print(f'>> Current distance array: {str(dist)}')

    print(f'>> Final distance array: {str(dist)}')
    return dist


if __name__ == '__main__':
    print('-' * 60)
    print("Bellman-Ford algorithm - Negative cycles")
    print('-' * 60, '\n')
    
    graphs = [
        {
            0: [Edge(1, 5)],
            1: [Edge(2, 20), Edge(5, 30), Edge(6, 60)],
            2: [Edge(3, 10), Edge(4, 75)],
            3: [Edge(2, -15)],
            4: [Edge(9, 100)],
            5: [Edge(4, 25), Edge(6, 5), Edge(8, 50)],
            6: [Edge(7, -50)],
            7: [Edge(8, -10)],
            8: [],
            9: []
        }, {
            0: [Edge(1, 10), Edge(5, 8)],
            1: [Edge(3, 2)],
            2: [Edge(1, 1)],
            3: [Edge(2, -2)],
            4: [Edge(1, -4), Edge(3, -1)],
            5: [Edge(4, 1)]
        }
    ]

    testcases = [
        (
            graphs[0], 0, 
            [0, 5, float("-Inf"), float("-Inf"), float("-Inf"), 35, 40, -10, -20, float("-Inf")]
        ), (
            graphs[1], 0, None
        )            
    ]

    for graph, start, solution in testcases:
        print(f'Graph: {graph}')
        dist = bellman_ford(graph, start)
        print(f'Distances: {dist}')
        if solution is not None:
            print(f'Test: {"OK" if dist == solution else "NOT OK"}')
        print()

    
    print('-' * 60)
    print(f'>>> Verbose example:\nGraph: {graphs[1]}')
    # bellman_ford_verbose(graphs[1], 0)
    bellman_ford_verbose(graphs[0], 0)