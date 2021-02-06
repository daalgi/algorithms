"""
source:
https://app.codesignal.com/arcade/graphs-arcade/kingdom-roads/nCMisf4ZKpDLdHevE

Once upon a time, in a kingdom far, far away, there lived a 
King Byteasar I. As a kind and wise ruler, he did everything 
in his (unlimited) power to make life for his subjects 
comfortable and pleasant. One cold evening a messenger 
arrived at the king's castle with the latest news: all 
kings in the Kingdoms Union had started enforcing traffic 
laws! In order to not lose his membership in the Union, 
King Byteasar decided he must do the same within his kingdom. 
But what would the citizens think of it?

The king decided to start introducing the changes with 
something more or less simple: change all the roads in the 
kingdom from two-directional to one-directional (one-way). 
He personally prepared the roadRegister of the new roads, 
and now he needs to make sure that the road system is 
convenient and there will be no traffic jams, i.e. each 
city has the same number of incoming and outgoing roads. 
As the Hand of the King, you're the one who he has decreed 
must check his calculations.

Example:
For
roadRegister = [[False, True,  False, False],
                [False, False, True,  False],
                [True,  False, False, True ],
                [False, False, True,  False]]

the output should be
newRoadSystem(roadRegister) = True
"""

def new_road_system(roadRegister):
    for row, col in zip(map(sum, roadRegister), map(sum, zip(*roadRegister))):
        if row != col:
            return False        
    return True


if __name__ == '__main__':
    print('-' * 60)
    print('New road system\nAll cities with the same number of incoming and outcoming roads')
    print('-' * 60)

    testcases = [
        ([
            [False,True,False,False], 
            [False,False,True,False], 
            [True,False,False,True], 
            [False,False,True,False]
            ], True),
        ([
            [False,True,False], 
            [False,False,False], 
            [True,False,False]
            ], False),
    ]

    for roadRegister, solution in testcases:
        print(f'Road register: {roadRegister}')
        result = new_road_system(roadRegister)
        print(f'All cities with the same number of incoming and outcoming roads: {str(result)}')
        if solution is not None:
            print(f'Test: {"OK" if solution == result else "NOT OK"}')
        print()