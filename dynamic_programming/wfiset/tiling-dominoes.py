"""
TILING DOMINOES
https://open.kattis.com/problems/tritiling

In how many ways can you tile a 3×n rectangle with 2×1 dominoes?
"""
def tiling_dominoes(n: int):
    """
    Parameters
    ----------
    n: int
        width of the rectangle 3xn to tile with 2x1 dominoes
    """
    # If the width is even, there's no solution
    if n & 1 != 0: return 0

    # 8 states per column (n columns):
    # state 0: 0 0 0 (here the column is transposed for space reasons)
    # state 1: # 0 0
    # state 2: 0 # 0
    # state 3: # # 0
    # state 4: 0 0 #
    # state 5: # 0 #
    # state 6: 0 # #
    # state 7: # # #
    
    # Table containing `n` rows that represent the columns,
    # and 8 columns that represent the possible states
    table = [[0 for _ in range(8)] for _ in range(n+1)]
    # Base case
    table[0][7] = 1
    # Loop through the columns to construct the current state
    # based on previous states
    for col in range(1, n+1):
        table[col][0] = table[col-1][7]
        table[col][1] += table[col-1][6]
        # table[col][2] += table[col-1][5] # state can't be tiled, so no need for this computation
        table[col][3] += table[col-1][7] + table[col-1][4]
        table[col][4] += table[col-1][3]
        # table[col][5] += table[col-1][2] # state can't be tiled, so no need for this computation
        table[col][6] += table[col-1][7] + table[col-1][1]
        table[col][7] += table[col-1][6] + table[col-1][3] + table[col-1][0]

    # print(table)
    return table[n][7]

    
if __name__ == "__main__":
    print('-' * 60)
    print('Tiling dominoes')
    print('-' * 60)
    
    test_cases = [
        (1, 0),
        (2, 3),
        (3, 0),
        (4, 11),
        (8, 153),
        (12, 2131)
    ]
    
    for n, solution in test_cases:        
        res = tiling_dominoes(n)
        string = f'Rectangle 2x{n}'
        string += ' ' * (25 - len(string)) + f'Possible tilings: {res}'
        if solution is not None:
            string += ' ' * (75 - len(string))
            string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string)
    print()