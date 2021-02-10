"""
SHORTEST PATH ON DAG
Graph: edge list
O(V+E) time
"""
from topsort import topsort
from utils import edge_list_to_adjacency_list


def dag_shortest_path(edges: list, start: int, verbose: bool = False):
    # Graph is stored as a list of edges
    adjacency_list = edge_list_to_adjacency_list(edges)
    weights = {(edge[0], edge[1]): edge[2] for edge in edges}
    ordering = topsort(graph=adjacency_list)
    n = len(adjacency_list)
    dist = [None] * n
    dist[start] = 0

    if verbose:
        print(f'\nAdjacency list:\n{adjacency_list}\n')
        print(f'Topsort:\n{ordering}\n')
    
    # Iterate through all the nodes of the graph
    for i in range(n):
        node_index = ordering[i]

        if verbose:
            print(f'Node {node_index}', end='\t')

        if dist[node_index] is None:
            continue

        # Grab the edges of the node
        adjacent_edges = adjacency_list[node_index]

        if verbose:
            print(f'Adjacent nodes:\t {adjacent_edges}')

        if not edges:
            continue

        # Iterate through the edges
        for edge in adjacent_edges:

            # Compute new distance from `node_index` to `edge`
            new_dist = dist[node_index] + weights[(node_index, edge)]

            if verbose:
                print(f'\t-->Edge {edge}, distance: {new_dist}')

            # Update the minimum distance to `edge`
            if dist[edge]:
                dist[edge] = min(dist[edge], new_dist)
            else:
                dist[edge] = new_dist

    if verbose:
        print(f'\nDistances:\t{dist}')

    return dist


if __name__ == '__main__':
    print('-' * 60)
    print('Shortest path on a DAG')
    print('-' * 60)
    
    edges = [
        [
            [0, 1, 3], [0, 2, 6], [1, 2, 4], [1, 3, 4], [2, 3, 8],
            [1, 4, 11], [2, 6, 11], [3, 4, -4], [3, 5, 5], [3, 6, 2],
            [4, 7, 9], [5, 7, 1], [6, 7, 2]
        ]        
    ]

    testcases = [
        (edges[0], 0, 11),
    ]

    for edges, start, solution in testcases:
        print(f'\nEdges: {edges}')
        print(f'Start: {start}')
        res = dag_shortest_path(edges, start, verbose=True)
        print(f'Shortest path: {res[-1]}')
        if solution:
            print(f'Test: {"OK" if res[-1] == solution else "NOT OK"}\n')
        print()