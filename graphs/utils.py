from collections import defaultdict


def adjacency_matrix(edge_list = None):
    if edge_list:
        return edge_list_to_adjacency_matrix(edge_list)    


def edge_list_to_adjacency_matrix(edges: list):
    if not isinstance(edges, (list, dict)):
        raise ValueError("`array` must be a list or a dict.")

    n = len(edges)
    matrix = [[False for _ in range(n)] for _ in range(n)]
    for x in edges:
        matrix[x[0]][x[1]] = True
        matrix[x[1]][x[0]] = True
    
    return matrix


def edge_list_to_adjacency_list(edges: list, 
    bidirectional: bool = False):
    adj = defaultdict(list)
    for edge in edges:
        adj[edge[0]].append(edge[1])
        if bidirectional:
            adj[edge[1]].append(edge[0])
        elif not adj[edge[1]]:
            adj[edge[1]] = []

    return adj


def print_matrix(matrix: list, element_space: int = 8):
    for row in matrix:
        for col in row:
            print(f'{str(col):>{element_space}}', end='')
        print()


if __name__ == '__main__':
    edges = [[3, 0], [0, 4], [5, 0], [2, 1], [1, 4], [2, 3], [5, 2]]
    matrix = edge_list_to_adjacency_matrix(edges)
    # print_matrix(matrix)
    print(edge_list_to_adjacency_list(edges))