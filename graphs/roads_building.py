"""
source:
https://app.codesignal.com/arcade/graphs-arcade/kingdom-roads/CSzczQWdnYwmyEjvv

Once upon a time, in a kingdom far, far away, there lived a 
King Byteasar II. There was nothing special about him or his 
kingdom. As a mediocre ruler, he preferred hunting and feasting 
over doing anything about his kingdom's prosperity.

Luckily, his adviser, the wise magician Bitlin, worked for 
the kingdom's welfare day and night. However, since there was 
no one to advise him, he completely forgot about one important 
thing: the roads! Over the years most of the two-way roads built by 
Byteasar's predecessors were forgotten and no longer traversable. 
Only a few roads can still be used.

Bitlin wanted each pair of cities to be connected, but couldn't 
find a way to figure out which roads are missing. Desperate, 
he turned to his magic crystal ball for help. The crystal 
showed him a programmer from the distant future: you! 
Now you're the only one who can save the kingdom. Given the 
existing roads and the number of cities in the kingdom, you 
should use the most modern technologies and find out which 
roads should be built again to connect each pair of cities. 
Since the crystal ball is quite old and meticulous, it will 
only transfer the information if it is sorted properly.

The roads to be built should be returned in an array sorted 
lexicographically, with each road stored as [cityi, cityj], 
where cityi < cityj.

Example:
For cities = 4 and roads = [[0, 1], [1, 2], [2, 0]],
the output should be
roadsBuilding(cities, roads) = [[0, 3], [1, 3], [2, 3]]
"""

def roadsBuilding(cities, roads):
    # Adjacency matrix
    matrix = [[False for _ in range(cities)] for _ in range(cities)]
    for road in roads:
        matrix[road[0]][road[1]] = True
        matrix[road[1]][road[0]] = True
        
    # Roads to build
    build = []
    for i in range(cities):
        for j in range(i+1, cities):
            if not matrix[i][j]:
                build.append([i, j])            
    
    return build
    


if __name__ == '__main__':
    print('-' * 60)
    print('Roads building\nRoads to be built to have each pair of cities connected')
    print('-' * 60)

    testcases = [
        (
            [[0,1], [1,2], [2,0]], 4, [[0,3], [1,3], [2,3]]),
        (
            [[1,2], [0,2], [1,4], [4,2], [3,5], [1,0], 
            [5,0], [3,1], [0,4], [5,1], [3,2], [3,0], [2,5]],
            6, [[3,4], [4,5]]
        )
        
    ]

    for roads, cities, solution in testcases:
        print(f'Number of cities: {cities}')
        print(f'Current roads: {roads}')
        result = roadsBuilding(cities, roads)
        print(f'Roads to be built: {result}')
        if solution is not None:
            print(f'Test: {"OK" if solution == result else "NOT OK"}')
        print()