"""
The function `count_construct(target, words)` accepts a string and 
an array of strings.

Returns the number of ways that the `target` can be constructed
by concatenating elements of the `words` array.

The elements  of `words` may be reused as many times as needed.

--------------
Analysis:
m = len(target)
n = len(words)

time: O(n * m^2)
space: O(m)
"""
def count_construct(target: str, words: list):
    n = len(target)
    table = [1] + [0] * n
    for i in range(n+1):
        if table[i] > 0:
            for word in words:
                m = len(word)
                if target[i:i+m] == word:
                    table[i+m] += table[i]
    #print(table)
    return table[n]


if __name__ == "__main__":
    from datetime import datetime
    target = 'abcdef'
    words = ['ab', 'abc', 'cd', 'def', 'abcd']
    print('\n' + '-' * 10, f'can_construct({target}, ', words, ')', '-' * 10)    
    
    time = datetime.now()
    res = count_construct(target, words)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'O(m^2 * n) time:   {time:10.0f} ms, solution:', res)
    
    print('\n' + '-' * 10, 'tests', '-' * 10)
    test_cases = [
        ('purple', ['purp', 'p', 'ur', 'le', 'purpl'], 2),
        ('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], 1),
        ('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], 0),
        ('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], 4),
        ('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], 0)
    ]
    for target, words, solution in test_cases:
        res = count_construct(target, words)
        print(f'can_construct({target}, ', words, f') = {res}',
            f'\tTest: {"OK" if solution == res else "NOT OK"}')
    print()
