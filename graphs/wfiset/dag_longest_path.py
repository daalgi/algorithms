"""
LONGEST PATH ON DAG
Graph: edge list
O(V+E) time

1. Multiply all edge values by -1.
2. Find the dag_shortest_path
3. Multiply the result by -1.
--> returns the longest path.
"""
from dag_shortest_path import dag_shortest_path


def dag_longest_path(edges: list, start: int, verbose: bool = False):
    new_edges = [[edge[0], edge[1], -edge[2]] for edge in edges]
    return [-d for d in dag_shortest_path(
        edges=new_edges, start=start, verbose=verbose)]


if __name__ == '__main__':
    print('-' * 60)
    print('Longest path on a DAG')
    print('-' * 60)
    
    edges = [
        [
            [0, 1, 3], [0, 2, 6], [1, 2, 4], [1, 3, 4], [2, 3, 8],
            [1, 4, 11], [2, 6, 11], [3, 4, -4], [3, 5, 5], [3, 6, 2],
            [4, 7, 9], [5, 7, 1], [6, 7, 2]
        ]        
    ]

    testcases = [
        (edges[0], 0, 23),
    ]

    for edges, start, solution in testcases:
        print(f'\nEdges: {edges}')
        print(f'Start: {start}')
        res = dag_longest_path(edges, start, verbose=True)
        print(f'Longest path: {res[-1]}')
        if solution:
            print(f'Test: {"OK" if res[-1] == solution else "NOT OK"}\n')
        print()