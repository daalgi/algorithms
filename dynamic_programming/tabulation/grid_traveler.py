"""
Say that you are a traeler on a 2D grid. You begin in the 
top-left corner and your goal is to travel to the bottom-right
corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with
dimensions m * n?

The function `grid_traveler(m, n)` takes two numbers as an argument.

--------------
Analysis:

time: O(m * n)
space: O(m * n)

"""
def grid_traveler(m: int, n: int):
    table = [[0] * (n+1) for i in range(m+1)]
    table[1][1] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            current = table[i][j]
            #print(i, j, table)
            if j < n:
                table[i][j+1] += current
            if i < m:
                table[i+1][j] += current
            #print(i, j, table, '\n')

    return table[m][n]


if __name__ == "__main__":
    from datetime import datetime
    m = 3
    n = 3
    print('\n' + '-' * 10, f'grid_traveler{m, n}', '-' * 10)    
    
    time = datetime.now()
    res = grid_traveler(m, n)
    
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'O(m * n) time:   {time:10.0f} ms, solution:', res)
    
    print('\n' + '-' * 10, 'tests', '-' * 10)
    test_cases = [
        (1, 1),  # 1
        (2, 3),  # 3
        (3, 2),  # 3
        (3, 3),  # 6
        (18, 18), # 2333606220
    ]
    for m, n in test_cases:
        print(f'grid_traveler{m, n} = {grid_traveler(m, n)}')