from collections import defaultdict


def one_hashtable(queries, verbose=False):
    numbers = defaultdict(int)
    ans = []
    for action, num in queries:        
        if action == 1:
            numbers[num] += 1
        elif action == 2:
            numbers[num] = max(numbers[num] - 1, 0)
        elif action == 3:
            if num in numbers.values():
                ans.append(1)
            else:
                ans.append(0)

        if verbose:
            print(action, num)
            print(numbers)
            print()

    return ans 

def two_hashtables(queries, verbose=False):
    numbers = defaultdict(int)
    frequencies = defaultdict(int)
    ans = []
    for action, num in queries:   

        if action == 1:
            # Insert
            numbers[num] += 1
            freq = numbers[num]
            frequencies[freq] += 1
            # Remove (decrease) previous frequency if it exists
            if frequencies[freq-1]:
                frequencies[freq-1] -= 1

        elif action == 2:
            # Delete only if the number has already been inserted
            if numbers[num]:
                freq = numbers[num]
                numbers[num] -= 1                
                frequencies[freq] -= 1
                
                # Add the new frequency of `num`
                new_freq = numbers[num]
                if new_freq:
                    frequencies[new_freq] += 1
                    
        elif action == 3:
            # Check frequencies
            if frequencies[num]:
                ans.append(1)
            else:
                ans.append(0)
        
        if verbose:
            print(action, num)
            print(numbers)
            print(frequencies)
            print()

    return ans  


if __name__ == "__main__":
    print('-' * 60)
    print('Frequency queries')
    print('-' * 60)
    test_cases = [
        ([(1, 5), (1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 5), (3, 2)], [0, 1]),
        ([(3, 4), (2, 1003), (1, 16), (3, 1)], [0, 1]),
        ([(1, 3), (2, 3), (3, 2), (1, 4), (1, 5), (1, 5), (1, 4), (3, 2), (2, 4), (3, 2)], [0, 1, 1])
    ]
    for arr, solution in test_cases:
        
        arr_string = str(arr[:3])
        if len(arr) > 3:
            arr_string = arr_string[:-1] + ', ...]'

        res = one_hashtable(arr)
        string = f'1-hashtable: array = {arr_string}'
        string += ' ' * (58 - len(string)) + f'result = {res}'
        string += ' ' * (80 - len(string))
        string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string)

        res = two_hashtables(arr)
        string = f'2-hashtable: array = {arr_string}'
        string += ' ' * (58 - len(string)) + f'result = {res}'
        string += ' ' * (80 - len(string))
        string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string, '\n')    