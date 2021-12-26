"""
TOPOLOGICAL SORT (TOPSORT)
Graph: adjacency list
O(V+E) time
"""
def topsort(graph):
    # Graph is stored as adjacency list
    n = len(graph)
    visited = [False] * n
    ordering = [0] * n
    index = n - 1 # index for ordering array

    # Iterate through all the nodes of the graph
    for node in graph.keys():
        if not visited[node]:
            # if the node hasn't been visited yet

            # List passed to `dfs()` to add nodes as we find them
            visited_nodes = []
            
            # add the visited nodes for this iteration
            dfs(node, visited, visited_nodes, graph)
            
            # 
            for node_id in visited_nodes:
                ordering[index] = node_id
                index -= 1
    
    return ordering

def dfs(node, visited, visited_nodes, graph):
    visited[node] = True

    for next in graph[node]:
        if not visited[next]:
            dfs(next, visited, visited_nodes, graph)
    
    visited_nodes.append(node)


if __name__ == '__main__':
    print('-' * 60)
    print('Topological sort (Topsort)')
    print('>> Directed Acyclic Graphs (DAG)')
    print('-' * 60)
    
    graphs = [
        {
            0: [2],
            1: [2, 3],
            2: [3, 4],
            3: [],
            4: []
        }, {
            0: [1],
            1: [2, 3, 4],
            2: [4],
            3: [4],
            4: [],
            5: [0]
        }
    ]

    testcases = [
        (graphs[0], None),
        (graphs[1], None),
    ]

    for graph, solution in testcases:
        print(f'\nGraph: {graph}')
        ordering = topsort(graph)
        print(f'Ordering: {ordering}')
        if solution:
            print(f'Test: {"OK" if ordering == solution else "NOT OK"}\n')
        print()
