def adjacency_matrix(edge_list = None):
    if edge_list:
        return edge_list_to_adjacency_matrix(edge_list)    


def edge_list_to_adjacency_matrix(edge_list):
    if not isinstance(edge_list, (list, dict)):
        raise ValueError("`array` must be a list or a dict.")

    n = len(edge_list)
    matrix = [[False for _ in range(n)] for _ in range(n)]
    for x in edge_list:
        matrix[x[0]][x[1]] = True
        matrix[x[1]][x[0]] = True
    
    return matrix


def print_matrix(matrix: list, element_space: int = 8):
    for row in matrix:
        for col in row:
            print(f'{str(col):>{element_space}}', end='')
        print()


if __name__ == '__main__':
    edge_list = [[3, 0], [0, 4], [5, 0], [2, 1], [1, 4], [2, 3], [5, 2]]
    matrix = edge_list_to_adjacency_matrix(edge_list)
    print_matrix(matrix)