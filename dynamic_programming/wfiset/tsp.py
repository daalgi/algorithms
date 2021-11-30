"""
TRAVELLING SALESMAN PROBLEM (TSP)

TODO finish algorithm...

Given a list of cities and the distances between each pair of cities,
what is the shortest possible route that visits each city exactly
once and returns to the origin city?

In other words: 
Given a complete graph with weighted edges (as an adjacency matrix),
what is the Hamiltonian cycle (path that visits every node once)
of minimum cost?

TSP is very hard: NP-Complete
- Brute force solution: O(n!)
- Dinamic programing algorithms: O(n^2 2^n)

TSP with DP:
The main idea will be to compute the optimal solution for all the
subpaths of length N, while using information from the already
known optimal partial tours of length N-1.

Initial setup:
1. Pick a starting node S
2. Store the optimal value from S to each node X
"""
def tsp(m: list, s: int):
    """
    Parameters
    ----------
    m: list
        2D adjacency matrix representing the graph
    s: int
        index of the starting node
    """
    n = len(m)

    # Initialize memo table with None values
    memo =[[None for _ in range(2**n)] for _ in range(n)]

    setup(m, memo, s, n)
    solve(m, memo, s, n)
    min_cost = find_min_cost(m, memo, s, n)
    tour = find_optimal_tour(m, memo, s, n)
    return(min_cost, tour)

def setup(m: list, memo: list, s: int, n: int):
    """
    Initializes the memo table by caching the optimal solution
    from the starting node to every other node
    """
    for i in range(n):
        if i == s: continue
        memo[i][i << s | 1 << i] = m[s][i]

def solve(m: list, memo: list, s: int, n: int):
    for

def find_min_cost(m: list, memo: list, s: int, n: int):
    pass

def find_optimal_tour(m: list, memo: list, s: int, n: int):
    pass

if __name__ == "__main__":
    print('-' * 60)
    print('Travelling salesman problem (TSP)')
    print('-' * 60)

    test_cases = [

    ]
    
    for (m, s), solution in test_cases:        
        res = tsp(m, s)
        string = f'Cities: {len(m)}\n'
        string += f'Min cost: {res[0]}\n'
        string += f'Optimal tour: {res[1]}\n'
        if solution is not None:
            string += f'Test: {"OK" if res == solution else "NOT OK"}\n'
        print(string)