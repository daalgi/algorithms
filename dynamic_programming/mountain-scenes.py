"""
MOUNTAIN SCENES
https://open.kattis.com/problems/scenes

An artist begins with a roll of ribbon. She clips it into pieces of 
various integral lengths, then aligns them with the bottom of a frame,
rising vertically in columns, to form a mountain scene. A mountain
scene must be uneven; ifall columns are the same height, it's a plain
scene, not a mountain scene! It is possible that she may not use all of
the ribbon.

Given the length of the ribbon and the width x height of the frame,
how many different mountain scenes can she create?
"""
import math


def mountain_scenes(w: int, h: int, n: int):
    """
    Parameters
    ----------
    w: int
        width of the scene
    h: int
        height of the scene
    n: int
        number of ribbon pieces
    """
    # Plain scenes
    ribbon_squares = min(n, w * h)
    plains = math.floor(ribbon_squares / w) + 1

    # Table to keep track of already calculated sub-solutions
    dp = [[None for _ in range(n+1)] for _ in range(w+1)]

    return recursion(1, w, h, n, dp) - plains

def recursion(i: int, width: int, height: int, ribbon: int, dp: list):
    if ribbon < 0:
        return 0
    if i > width:
        return 1
    if dp[i][ribbon] is not None:
        return dp[i][ribbon]
    scenes = 0
    for length in range(height+1):
        scenes += recursion(i + 1, width, height, ribbon - length, dp)
    dp[i][ribbon] = scenes
    return scenes

    
if __name__ == "__main__":
    print('-' * 60)
    print('Mountain scenes')
    print('-' * 60)
    
    test_cases = [
        ((2, 2, 4), 6),
        ((3, 2, 6), 24),
        ((3, 2, 4), 21),
        ((5, 5, 25), 7770),
        ((5, 5, 15), 6050),
        ((10, 1, 10), 1022),
        ((6, 4, 15), None),
        ((6, 4, 150), None),
        ((6, 4, 250), None),
        ((60, 40, 25), None)
    ]
    
    for (w, h, n), solution in test_cases:        
        res = mountain_scenes(w, h, n)
        string = f'Scene {w}x{h} and {n} ribbons'
        string += ' ' * (35 - len(string)) + f'Mountain scenes: {res}'
        if solution is not None:
            string += ' ' * (75 - len(string))
            string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string)
    print()