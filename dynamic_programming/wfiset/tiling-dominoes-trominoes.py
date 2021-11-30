"""
TILING DOMINOES + TROMINOES
https://leetcode.com/problems/domino-and-tromino-tiling/

In how many ways can you tile a 2xN rectangle grid with dominoes (2x1) and 
"L" shaped trominoes where N is an integer between 1 and 1000?
"""
def tiling_dominoes(n: int):
    """
    Parameters
    ----------
    n: int
        width of the rectangle 2xn to tile with 2x1 dominoes and "L" trominoes
    """
    # 4 states per column (n columns):
    # state 0: 0 0 (here the column is transposed for space reasons)
    # state 1: # 0
    # state 2: 0 #
    # state 3: # #
    
    # Table containing `n` rows that represent the columns,
    # and 4 columns that represent the possible states
    table = [[0 for _ in range(4)] for _ in range(n+1)]
    # Base case
    table[0][3] = 1
    # Loop through the columns to construct the current state
    # based on previous states
    for col in range(1, n+1):
        # TODO
        pass

    # print(table)
    return table[n][7]


def solve_recursion(n: int):
    """
    Parameters
    ----------
    n: int
        width of the rectangle 2xn to tile with 2x1 dominoes and "L" trominoes
    """
    dp = [[None for _ in range(4)] for _ in range(n+1)]
    return recursion(n, 0, True, True, dp)

def make_state(t1: bool, t2: bool):
    if not t1 and not t2: return 0
    if t1 and not t2: return 1
    if not t1 and t2: return 2
    return 3

def recursion(n: int, i: int, t1: bool, t2: bool, dp: list):
    """
    - - - - - -
    | t1 | t3 |
    - - - - - -
    | t2 | t4 |
    - - - - - -

    Parameters
    ----------
    n: int
        width of the rectangle 2xn
    i: int
        current index
    t1: bool
        is the cell t1 free?
    t2: bool
        is the cell t2 free?
    dp: 
    """
    # Base case, the end of the board is reached
    if i == n and t1 and t2:
        return 1

    # Evaluate the current state
    state = make_state(t1, t2)

    # Check if the solution has been already computed  
    if dp[i][state] is not None:
        return dp[i][state]

    # Frontier tiles t3 and t4
    t3, t4 = i+1 < n, i+1 < n

    # 4 states per column (n columns):
    # state 0: 0 0 (here the column is transposed for space reasons)
    # state 1: # 0
    # state 2: 0 #
    # state 3: # #
    count = 0
    if t1 and t2 and t3: 
        # Tromino in tiles t1, t2, t3
        count += recursion(n, i+1, False, True, dp)
    if t1 and t2 and t4: 
        # Tromino in tiles t1, t2, t4
        count += recursion(n, i+1, True, False, dp)
    if t1 and not t2 and t3 and t4:
        # Tromino in tiles t1, t3, t4
        count += recursion(n, i+1, False, False, dp)
    if not t1 and t2 and t3 and t4:
        # Tromino in tiles t2, t3, t4
        count += recursion(n, i+1, False, False, dp)
    if t1 and t2:
        # Vertical domino in tiles t1, t2
        count += recursion(n, i+1, True, True, dp)
    if t1 and t2 and t3 and t4:
        # Two horizontal dominoes in tiles t1-t3 and t2-t4
        count += recursion(n, i+1, False, False, dp)
    if t1 and not t2 and t3:
        # Horizontal domino in tiles t1, t3
        count += recursion(n, i+1, False, True, dp)
    if not t1 and t2 and t4:
        # Horizontal domino in tiles t2, t4
        count += recursion(n, i+1, True, False, dp)
    if not t1 and not t2:
        # Vertical domino in tiles t3, t4
        count += recursion(n, i+1, True, True, dp)
    
    dp[i][state] = count
    return dp[i][state]

    
if __name__ == "__main__":
    print('-' * 60)
    print('Tiling dominoes and trominoes')
    print('-' * 60)
    
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 5),
        (4, 11),
        (8, None),
        (12, None),
        (88, None)
    ]
    
    for n, solution in test_cases:        
        res = solve_recursion(n)
        string = f'Rectangle 2x{n}'
        string += ' ' * (25 - len(string)) + f'Possible tilings: {res}'
        if solution is not None:
            string += ' ' * (75 - len(string))
            string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string)
    print()