"""
Given n points in the plane and want to figure out the pair of 
points that are closest to each other.

Input: 
n >= 2 points p1 = (x1, y1), ..., pn = (xn, yn) in the plane.

Output:
The pair pi, pj of points with smallest Euclidean distance d(pi, pj)


"""
import math


def euclidean_squared_distance(p1: tuple, p2: tuple):
    # No need to compute the sqrt to find the minimum
    # distance between two points, the squared distance
    # is going to yield the same result and is faster.
    return sum((i - j) ** 2 for i, j in zip(p1, p2))

def euclidean_distance(p1: tuple, p2: tuple):
    return math.sqrt(sum((i - j) ** 2 for i, j in zip(p1, p2)))

def brute_force(points: list):
    """
    Compute distance between pairs of points one-by-one.
    Running time: O(n2)
    points -- list of tuples
    """
    n = len(points)
    p1 = points[0]
    p2 = points[1]
    min_distance = euclidean_squared_distance(p1, p2)
    for i in range(n-1):
        for j in range(i+1, n):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                p1 = points[i]
                p2 = points[j]

    return [p1, p2], min_distance


def closest_split_pair(px: list, py: list, delta: float):
    """
    Returns the closest pair and their distance wheneveir it's a split pair.
    It's a 'brute-force' search over a cleverly restricted set of point pairs.

    Running time: O(n)
    """
    x_left_max = px[len(px)//2][0]
    subset = [p for p in py if x_left_max - delta <= p[0] <= x_left_max + delta]
    best_dist = delta
    best_pair = []
    #print('closest_split_pair()------------')
    #print('x_left_max', x_left_max, '\ndelta', delta)
    #print(subset)
    for i in range(len(subset)):
        for j in range(min(6, len(subset)-i)):
            if i == i+j:
                continue
            distance = euclidean_distance(subset[i], subset[i+j])
            #print('-->inside loop', i, j, subset[i], subset[i+j], distance)
            if distance < best_dist:
                best_dist = distance
                best_pair = [subset[i], subset[i+j]]
    #print(best_pair, best_dist)
    return best_pair, best_dist


def closest_pair(px: list, py: list):
    """
    Running time: O(n log(n))
    """
    n = len(px)
    # Base case
    if n == 1:
        return points, float("inf")
    elif n <= 3:
        return brute_force(px)
    
    # Divide
    half = n // 2
    #print('closest_pair()-------------')
    #print('left------->', left_pair, dist_left)
    #print('right------->', right_pair, dist_right)
    left_pair, dist_left = closest_pair(px[:half], py[:half])    
    right_pair, dist_right = closest_pair(px[half:], py[half:])    
    dist_min = min(dist_left, dist_right)
    split_pair, dist_split = closest_split_pair(px, py, dist_min)

    # Merge
    if dist_split < dist_min:
        #print('res--->split', split_pair, dist_split)
        return split_pair, dist_split
    elif dist_left < dist_right:
        #print('res--->left', left_pair, dist_left)
        return left_pair, dist_left
    else:
        #print('res--->right', right_pair, dist_right)
        return right_pair, dist_right

def divide_and_conquer(points: list):
    if len(points) <= 3:
        return brute_force(points)
    
    px = sorted(points, key=lambda x: x[0])
    py = sorted(points, key=lambda x: x[1])
    return closest_pair(px, py)

if __name__ == '__main__':
    print('-' * 60)
    print('Closest pair of points in the plane')
    print('-' * 60)
    test_cases = [
        #([(0,), (11,), (2.1,), (2.5,), (2.51,)], [(2.5,), (2.51,)]), # 1D not implemented in divide_and_conquer
        ([(0, 0), (3, 13), (2, 3), (8, 13), (1, 1), (4, 8)], [(0, 0), (1, 1)]),
        ([(0, 0), (3, 13), (1, 1), (4, 8)], [(0, 0), (1, 1)]),
        ([(0, 0), (3, 13), (1, 1)], [(0, 0), (1, 1)]),
        ([(0, 0), (3, 13), (4, 4), (1, 88)], [(0, 0), (4, 4)]),
    ]
    
    case = 1
    for points, solution in test_cases:
        result = brute_force(points)
        string = f'   brute_force({case}) = {str(result[0])}'
        string += ' ' * (50 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result[0] else "NOT OK"}')
        
        result = divide_and_conquer(points)
        string = f'recursive_call({case}) = {str(result[0])}'
        string += ' ' * (50 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result[0] else "NOT OK"}\n')
        
        case += 1