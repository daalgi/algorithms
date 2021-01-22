"""
Constraints:
0 <= expenditure[i] <= 200
"""
from random import randint


def trailing_array(expenditure: list, d: int):
    n = len(expenditure)
    half = d // 2
    notifications = 0
    trailing = sorted(expenditure[:d])
    
    odd = True if d % 2 == 1 else False
    
    # Loop through the days of the dataset
    for i in range(d, n):

        # Compute median
        if odd:
            median = trailing[half]
        else:
            median = (trailing[half-1] + trailing[half]) / 2
            
        # Check if notification has to be sent
        if expenditure[i] >= median * 2:
            notifications += 1
        
        # Update the sorted array of trailing days
        last_added = first_removed = False
        new_trailing = []
        
        for j in range(d):
            # Skip the first element of the (unsorted) trailing array
            if not first_removed and trailing[j] == expenditure[i-d]:
                first_removed = True
                continue
            
            # Add the new element to the (sorted) new_trailing array
            if not last_added and trailing[j] >= expenditure[i]:
                new_trailing.append(expenditure[i])
                last_added = True
            
            # Add element from previous trailing array
            new_trailing.append(trailing[j])
            
        # If not added yet, add the last expenditure to the new_trailing array
        if not last_added:
            new_trailing.append(expenditure[i])
            
        # Update the reference to the trailing array
        trailing = new_trailing
            
    return notifications


def trailing_frequencies(expenditure: list, d: int, verbose: int = 0):
    n = len(expenditure)
    half = d // 2
    half_plus1 = half + 1
    notifications = 0
    odd = True if d % 2 == 1 else False

    # Frequencies array 
    # (counting sort idea)
    # IMPORTANT CONSTRAINT: max expenditure = 200
    # Since 200 is a fairly small integer, 
    # counting sort is extremely efficient for large 
    # arrays of `expenditure` and `d`
    freq = [0] * 201
    for i in range(d):
        freq[expenditure[i]] += 1
    
    # Loop through the days of the dataset
    for i in range(d, n):

        if verbose:
            print(f'\nExpenditure day i: {i}\t location of the median: {half}')

        # Identify which number falls in the median position
        # from the frequency array
        # Loop through the `freq` array up to the median position
        trailing_count = 0
        median_arr = []
        for index in range(201):
            
            if freq[index]:
                trailing_count += freq[index]
            
            if not median_arr and half <= trailing_count:
                median_arr.append(index)
            
            if half_plus1 <= trailing_count:
                median_arr.append(index)
                break

        if verbose:
            print('Median array:', median_arr)

        # Median of the current trailing days
        median = None
        if odd:
            median = median_arr[-1]

            if verbose:
                print('Odd number of trailing days --> median:', median)

        else:
            median = sum(median_arr) / 2

            if verbose:
                print('Even number of trailing days --> median:', median)
            
        # Check if notification has to be sent
        if expenditure[i] >= median * 2:
            notifications += 1

        # Update frequencies array
        freq[expenditure[i]] += 1
        freq[expenditure[i-d]] -= 1
            
    return notifications


if __name__ == '__main__':
    print('-' * 60)
    print('Fraudulent activity notifications')
    print('-' * 60)

    test_cases = [
        ([10, 20, 30, 40, 50], 3, 1),
        ([1, 2, 3, 4, 4], 4, 0),
        ([2, 3, 4, 2, 3, 6, 8, 4], 5, 2),
        ([2, 3, 1, 4, 4, 6, 5, 1], 3, None),
        ([2, 3, 1, 4, 4, 6, 5, 1], 4, None),
        ([randint(0, 200) for _ in range(20000)], 200, None),
        ([randint(0, 200) for _ in range(20000)], 201, None)
    ]
    
    for expenditure, days, solution in test_cases:
        
        array_string = str(expenditure[:6])
        if len(expenditure) > 6:
            array_string = array_string[:-1] + ', ...]'

        result = trailing_array([*expenditure], days)
        string = f'      trailing_array({array_string}, {days}) = {str(result)}'
        string += ' ' * (60 - len(string))
        if solution is not None:
            string += f'\t\tTest: {"OK" if solution == result else "NOT OK"}'
        print(string)

        result = trailing_frequencies([*expenditure], days, verbose=0)
        string = f'trailing_frequencies({array_string}, {days}) = {str(result)}'
        string += ' ' * (60 - len(string))
        if solution is not None:
            string += f'\t\tTest: {"OK" if solution == result else "NOT OK"}'
        print(string)
        print()

    print()


    expenditure, days, _ = test_cases[4]
    array_string = str(expenditure[:6])
    if len(expenditure) > 6:
        array_string = array_string[:-1] + ', ...]'
    string = f'--> Verbose example:'
    string += f'\nExpenditure: {array_string}\nDays: {days}'
    print(string)
    
    result = trailing_frequencies([*expenditure], days, verbose=1)
    string = f'\ntrailing_frequencies({array_string}, {days}) = {str(result)}'
    print(string)