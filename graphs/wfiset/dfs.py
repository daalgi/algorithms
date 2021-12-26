"""
DEPTH FIRST SEARCH (DFS)
Graph: adjacency list 
Time complexity O(V+E)
"""

def dfs(graph, start_vertex, verbose: bool = False):
    visited, traversal, stack = set(), [], [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            # add vertex in the same order as visited
            stack.extend(reversed(graph[vertex]))

            if verbose:
                string = f'--> Current vertex: {vertex}'
                string += f'\tConnected to: {str(graph[vertex])}'
                string += ' ' * (60 - len(string)) 
                string += f'Stack: {str(stack)}'
                print(string)

    return traversal


if __name__ == '__main__':
    print('-' * 60)
    print('Depth first search algorithm (DFS)')
    print('-' * 60)
    graphs = [
        {
            'A': ['B', 'S'],
            'B' : ['A'],
            'C' : ['D','E','F','S'],
            'D' : ['C'],
            'E' : ['C','H'],
            'F' : ['C','G'],
            'G' : ['F','S'],
            'H' : ['E','G'],
            'S' : ['A','C','G']
        },
        {
            1: [2, 3],
            2: [1, 4, 5],
            3: [1],
            4: [2],
            5: [2]
        }
    ]

    testcases = [
        (graphs[0], 'A', ['A', 'B', 'S', 'C', 'D', 'E', 'H', 'G', 'F']),
        (graphs[1], 1, [1, 2, 4, 5, 3]),
        (graphs[1], 4, [4, 2, 1, 3, 5]),
        (graphs[1], 2, [2, 1, 3, 4, 5]),
    ]

    for graph, start, solution in testcases:
        print(f'\nGraph: {graph}')
        print(f'Starting point: {start}')
        result = dfs(graph, start, verbose=True)
        print(f'Traversal: {result}')
        print(f'Test: {"OK" if solution == result else "NOT OK"}\n')