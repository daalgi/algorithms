"""
The function `all_construct(target, words)` accepts a string and 
an array of strings.

Returns a 2D array containing all of the ways that the
`target` can be constructed by concatenating elements of the `words` array.
Each single elemento of the 2D array represents one combination that 
constructs the `target`.

The elements  of `words` may be reused as many times as needed.

--------------
Analysis:
m = len(target)
n = len(words)

time: O(n^m)
space: O(n^m)

We can't do better than brute force (exponential complexity), 
because the function must return all the possible solutions.
"""
def all_construct(target: str, words: list, memo: dict = None):
    n = len(target)
    table = [[] for i in range(n+1)]
    table[0] = [[]]     # base case

    for i in range(n+1):
        for word in words:
            m = len(word)
            if target[i:i+m] == word:
                new_combinations = [[*t, word] for t in table[i] if isinstance(t, list)]
                for combination in new_combinations:
                    table[i+m].append(combination)

    #print(table)
    return table[n]


if __name__ == "__main__":
    from datetime import datetime
    target = 'abcdef'
    words = ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']
    #target = 'e'*22 + 'f'
    #words = ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']
    #print('\n' + '-' * 10, f'can_construct({target},', words, ')' + '-' * 10)    
    
    time = datetime.now()
    res = all_construct(target, words)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'O(n^m) time:   {time:10.0f} ms, solution:', res)
  
    
    print('\n' + '-' * 10, 'tests', '-' * 10)
    test_cases = [
        ('purple', ['purp', 'p', 'ur', 'le', 'purpl'], [['purp', 'le'], ['p', 'ur', 'p', 'le']]), # 2 solutions
        ('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], [['abc', 'def'], ['ab', 'c', 'def'], ['abcd', 'ef'], ['ab', 'cd', 'ef']]), # 4 solutions
        ('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], []), # 0 solutions
        ('eeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], []) # 0 solutions
    ]
    for target, words, solution in test_cases:
        res = all_construct(target, words)
        if len(res) == 0:
            print(f'can_construct({target},', words, ') =', res)        
        else:
            print(f'can_construct({target},', words, ') =')        
            for r in res:
                print(r)
        print(f'\tTest: {"OK" if solution == res else "NOT OK"}')
        