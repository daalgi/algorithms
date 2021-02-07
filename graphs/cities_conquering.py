"""
source:
https://app.codesignal.com/arcade/graphs-arcade/kingdom-roads/pmmMeP4JkqgKbzyTy

Once upon a time, in a kingdom far, far away, there lived a 
King Byteasar VII. Since he reigned during the Dark Times, 
very little is known about his reign. It is known that when 
he ascended the throne, there were n cities in the kingdom, 
connected by several two-way roads. But before the young king 
managed to start ruling, an enemy arrived at the gates: the evil 
emperor Bugoleon invaded the kingdom and started to conquer the 
cities, advancing day after day.

It is not known how long it took to capture each of the 
cities, but you've recently discovered an ancient manuscript 
describing that each day, Bugoleon captured all the cities 
that had at most 1 neighboring free city at that given moment. 
Knowing this fact, the number of cities n and all the roads of 
the kingdom, determine in how many days each of the cities 
was conquered.

Example:
For n = 10 and
roads = [[1, 0], [1, 2], [8, 5], [9, 7], 
         [5, 6], [5, 4], [4, 6], [6, 7]]
the output should be
citiesConquering(n, roads) = [1, 2, 1, 1, -1, -1, -1, 2, 1, 1].
"""
def citiesConquering(n, roads):
    # Generate adjacency matrix
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for road in roads:
        matrix[road[0]][road[1]] = 1
        matrix[road[1]][road[0]] = 1
    
    # List to store the days each city was conquered
    res = [-1] * n
    
    # Loop through the days, at most `n`
    for day in range(n):
        new_cities_conquered = []
        # print_matrix(matrix, element_space=3)

        # Loop through the cities
        for city in range(n):
            
            if res[city] < 1 and sum(matrix[city]) < 2:
                # City with only 1 neighboring free city, 
                # and not previously conquered
                res[city] = day + 1
                new_cities_conquered.append(city)
        
        if new_cities_conquered:
            # Add 1 day to the previously conquered cities
            for city in range(n):
                if city in new_cities_conquered:
                    # Remove conquered city from adjacency matrix
                    for k in range(n):
                        matrix[city][k] = 0
                        matrix[k][city] = 0

        else:
            # If no new cities conquered, break the loop
            break
    
    return res


def print_matrix(matrix: list, element_space: int = 8):
    for row in matrix:
        for col in row:
            print(f'{str(col):>{element_space}}', end='')
        print()

if __name__ == '__main__':
    print('-' * 60)
    print('Cities conquering')
    print('-' * 60)
    
    roads = [
        [[1,0], [1,2], [8,5], [9,7], [5,6], [5,4], [4,6], [6,7]],
        [],
        [[0,1], [1,2], [2,3], [3,4], [4,5], [5,0]],
        [[0,1], [1,2], [2,3], [3,4], [4,5], [5,6], [6,7]],
    ]

    testcases = [
        (roads[0], 10, [1, 2, 1, 1, -1, -1, -1, 2, 1, 1]),
        (roads[1], 5, [1, 1, 1, 1, 1]),
        (roads[2], 6, [-1, -1, -1, -1, -1, -1]),
        (roads[3], 8, [1, 2, 3, 4, 4, 3, 2, 1]),
    ]

    for roads, cities, solution in testcases:
        print(f'\nRoads: {roads}')
        res = citiesConquering(cities, roads)
        print(f'Day in each city was conquered: {res}')
        if solution:
            print(f'Test: {"OK" if res == solution else "NOT OK"}\n')
        else:
            print()