"""
NARROW ART GALLERY
https://www.youtube.com/watch?v=oQQO_n57SB0&list=PLDV1Zeh2NRsAsbafOroUBnNV8fhZa7P4u&index=6&ab_channel=WilliamFiset
https://open.kattis.com/problems/narrowartgallery

A long art gallery has `2N` rooms. The gallery is laid out as 
`N` (3 <= N <= 200) rows of 2 rooms side by side.

Doors connect all adjacent rooms (but not diagonally).

The gallery manager must close off `K` (0 <= K <= N) of the
rooms because of staffing cuts.

Visitors of the gallery must be able to enter using at least one of 
the two rooms at one end of the gallery, proceed through the gallery,
and exit from at least one of the two rooms at the other end.

Furthermore, the manager has determined how much value each room
has to the general public, and now she wants to close off those `K`
rooms that leave the most value available to the public, without
blocking passage through the gallery.
"""
LEFT = 0 # constant for the left gallery column
RIGHT = 1 # constant for the right gallery column
INF = 1E9 # a large enough inifinity for this problem

gallery = [] #

def solve(gallery: list, k: int):
    n = len(gallery)
    dp = [[[None for _ in range(2)] for _ in range(n)] for _ in range(k+1)]
    suma = 0
    for i in range(n):
        suma += gallery[i][LEFT] + gallery[i][RIGHT]
    return suma - f(k, n-1, gallery, dp)

def f(k: int, r: int, g: list, dp: list):
    return min(state(k, r, LEFT, g, dp), state(k, r, RIGHT, g, dp))

def state(k: int, r: int, c: int, g: list, dp: list):
    """
    Parameters
    ----------
    k: int
        number of rooms the manager has to close.
    r: int
        represents the row index.
    c: int
        column index, either 0 or 1.
    g: list
        2D integer matrix of size N x 2
    dp: list
        3D integer matrix of size K+1 x N x 2, 
        initially filled with None values. The value of dp[k][r][c]
        represents the partial state with `k` rooms closed, `r` rows
        processed, and column `c` selected in the current row.
    
    Returns
    -------
    int
        value of the closed rooms for the given state
    """
    if k == 0:
        return 0
    if r < 0:
        return INF
    if dp[k][r][c] is not None:
        return dp[k][r][c]
    # Get the value of the current room at row `r` column `c`
    room_value = g[r][c]
    dp[k][r][c] = min(
        # Close the current room, and take the best value from the partial
        # state directly below the current room
        state(k-1, r-1, c, g, dp) + room_value,
        # Don't include the current room. Instead, take the value of the
        # best previously calculated state which includes `k` closed rooms
        state(k, r-1, c, g, dp),
        state(k, r-1, c ^ 1, g, dp) # operator XOR: 1 ^ 1 = 0, 0 ^ 1 = 1
    )
    return dp[k][r][c]
        

if __name__ == "__main__":
    print('-' * 60)
    print('Narrow art gallery')
    print('-' * 60)
    
    gallery = [
        [[3, 1], [2, 1], [1, 2], [1, 3], [3, 3], [0, 0]],
        [[1, 2], [4, 1], [1, 2]],
        [[7, 8], [4, 9], [3, 7], [5, 9], [7, 2], [10, 3], [0, 10], [3, 2], [6, 3], [7, 9]]
    ]
    test_cases = [
        ((gallery[0], 4), 17),
        ((gallery[1], 0), 11),
        ((gallery[1], 1), 10),
        ((gallery[1], 2), 9),
        ((gallery[1], 3), 6),
        ((gallery[2], 5), 102),
        ((gallery[2], 8), None),
        ((gallery[2], 10), None),
        ((gallery[2], 2), None)
    ]
    
    for (gallery, k), solution in test_cases:        
        res = solve(gallery, k)
        string = f'Gallery: {gallery}\nRooms to be closed = {k}\n'
        string += f'Gallery open rooms value: {res}'
        if solution is not None:
            string += ' ' * (55 - len(string))
            string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string)
        print()
    print()