"""
MAGICAL COWS
https://open.kattis.com/problems/magicalcows

Baxter Scott owns The Enlightened Dairy Co., a dairy company 
with magical cows. Early each morning, he brushes his teeth, 
strolls outside, and finds that the cows have doubled in number. 
With double the number of cows, he can produce double the quantity 
of milk. While he is ecstatic that he has so many cows and so 
much milk, the Dairy Regulator forces him to keep at most C 
cows on any given farm, which greatly complicates his business.

At The Enlightened Dairy Co., Baxter has access to an unlimited 
number of farms, each with a maximum capacity of C cows. On each 
farm, cows reproduce at the same rate: they always double in 
number when the clock strikes midnight. To stay within the 
Regulator’s rules, whenever a farm has strictly more than C cows,
Baxter selects half of the cows on that farm and moves them to an 
entirely new, empty farm. More precisely, if there are D≤C cows 
on a farm, he leaves all D cows on the farm, but if there are D>C 
cows on a farm, he leaves ⌈D2⌉ cows on the farm and takes ⌊D2⌋ cows 
to a new, empty farm. (Here ⌈ ⌉ and ⌊ ⌋ denote the ceiling and 
floor functions, which round up/down to the nearest integer, 
respectively.) He does this early every morning, before the 
Regulator could possibly show up, so that he can avoid paying 
hefty Moo Fees.

The Regulator needs to know how many farms she will be inspecting 
when she visits The Enlightened Dairy Co. The Regulator inspects 
every farm that has at least one cow, and does not inspect any 
farm with zero cows. Given the number of cows on each farm with 
at least one cow on Day 0, compute the number of farms that need 
inspecting on any given day.
"""
def number_of_farms(capacity: int, initial_cows: list, day: int):
    """
    Keyword arguments:
    capacity -- maximum numberof cows per farm
    initial_cows -- list with the number of initial cows in each of the original farms
    day -- day in which the regulator will inspect the farm
    """
    # Frequency list to keep track of the number of farms
    # with the different possible capacities at
    freq = [[0 for _ in range(capacity+1)] for _ in range(day+1)]

    # Count the initial frequency of farms with different number of cows
    for farm in initial_cows:
        freq[0][farm] += 1

    # Loop through the days `day+1`
    half = capacity / 2
    for d in range(1, day+1):        
        # Loop through the frequency list of `capacity+1` size
        for c in range(1, capacity+1):
            if c <= half:
                # If the current number of cows is at most half of the capacity,
                # double the cows, not increasing the number of farms
                freq[d][c*2] += freq[d-1][c]
            else:
                # If the current number of cows is more than half of the capacity,
                # double the number of farms
                freq[d][c] += freq[d-1][c] * 2
    
    # Sum the number of farms in the last day
    return sum(freq[-1])

    
if __name__ == "__main__":
    print('-' * 60)
    print('Magical cows')
    print('-' * 60)
    
    test_cases = [
        (2, [1, 2, 1, 2, 1], 1, 7),
        (2, [1, 2, 1, 2, 1], 2, 14),
        (8, [1, 3, 2, 1], 1, 4),
        (8, [1, 3, 2, 1], 2, 5),
        (8, [1, 3, 2, 1], 3, 8),
        (8, [1, 3, 2, 1], 4, 16),
        (8, [1, 3, 2, 1], 5, 32),
        (8, [1, 3, 2, 1], 6, 64),
    ]
    
    for capacity, initial_cows, day, solution in test_cases:
        
        res = number_of_farms(capacity, initial_cows, day)
        string = f'Number of cows {capacity, initial_cows, day}'
        string += ' ' * (50 - len(string)) + f'= {res}'
        if solution:
            string += ' ' * (75 - len(string))
            string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string)
    print()