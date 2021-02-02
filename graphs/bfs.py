"""
BREADTH FIRST SEARCH (BFS)
Graph: adjacency list 
Time complexity O(V+E)
"""
import queue

def bfs(graph, start, verbose: bool = False):
    n = len(graph)
    visited = set()
    q = queue.Queue(maxsize=n)

    visited.add(start)
    q.put(start)
    nodes = []
    string = ''
    
    while not q.empty():
        node = q.get()
        nodes.append(node)
        
        for next in graph[node]:
            if next not in visited:
                q.put(next)
                visited.add(next)
    
        if verbose:
            string = f'Node {node}'
            string += f'\t\tQueue {[e for e in list(q.queue)]}'
            print(string)

    return nodes


if __name__ == '__main__':
    print('-' * 60)
    print('Breadth first search algorithm (BFS)')
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
        }, {
            1: [2, 3],
            2: [1, 4, 5],
            3: [1],
            4: [2],
            5: [2]
        }
    ]

    testcases = [
        (graphs[0], 'A', None),
        (graphs[1], 1, [1, 2, 3, 4, 5]),
        (graphs[1], 4, [4, 2, 1, 5, 3]),
        (graphs[1], 2, [2, 1, 4, 5, 3]),
    ]

    for graph, start, solution in testcases:
        print(f'\nGraph: {graph}')
        print(f'Starting point: {start}')
        result = bfs(graph, start, verbose=True)
        print(f'Nodes visiting order: {result}')
        if solution:
            print(f'Test: {"OK" if solution == result else "NOT OK"}')
        print()