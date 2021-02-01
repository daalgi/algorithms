"""
FIND COMPONENTS 
DEPTH FIRST SEARCH (DFS)
Graph: adjacency list 
Time complexity O(V+E)
"""
class FindComponents:

    def __init__(self, graph: dict):
        self.graph = graph
        self.n = len(graph)
        self.count = 0
        self.components = {}
        self.find_components()
        
    def find_components(self):
        for node in self.graph.keys():
            if node not in self.components:
                self.count += 1
                self.dfs(node)            
        return (self.count, self.components)

    def dfs(self, node):
        self.components[node] = self.count
        for next in self.graph[node]:
            if next not in self.components:
                self.dfs(next)


if __name__ == '__main__':
    print('-' * 60)
    print('Find components in a unidirected graph')
    print('-' * 60)
    
    graphs = [
        {
            1: [2, 3],
            2: [1, 4, 5],
            3: [1],
            4: [2],
            5: [2]
        }, {
            1: [2],
            2: [3],
            3: [1],
            4: [5],
            5: []
        }, {
            1: [2],
            2: [1],
            3: [],
            4: []
        }
    ]

    testcases = [
        (graphs[0], 1, {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}),
        (graphs[1], 2, {1: 1, 2: 1, 3: 1, 4: 2, 5: 2}),
        (graphs[2], 3, {1: 1, 2: 1, 3: 2, 4: 3}),
    ]

    for graph, num, components in testcases:
        print(f'\nGraph: {graph}')
        fc = FindComponents(graph)
        print(f'Number of components: {fc.count}')
        print(f'Components: {fc.components}')
        print(f'Test: {"OK" if fc.count == num and fc.components == components else "NOT OK"}\n')