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

Height of the tree: m (worst case scenario)
Each node might have up to n sub-nodes (worst case scenario)

Brute force and memoized:
time: O(n^m)
space: O(m)

Can't do better due to the nature of the problem, which
demands to return all the possible solutions.
"""
def all_construct_slow(target: str, words: list):
    if target == '': return [[]]
    
    result = []
    for word in words:
        n = len(word)
        if target[:n] == word:
            suffix = target[n:]
            suffix_ways = all_construct_slow(suffix, words)
            result += [[word] + s for s in suffix_ways]
    
    return result


def all_construct0(target: str, words: list, memo: dict = None):
    if not memo: memo = {}
    if target in memo: return memo[target]
    if target == '': return [[]]
    
    result = []
    for word in words:
        n = len(word)
        if target[:n] == word:
            suffix = target[n:]
            suffix_ways = all_construct0(suffix, words, memo)
            #memo[suffix] = suffix_ways
            result += [[word] + s for s in suffix_ways]
    
    memo[target] = result
    return result


def all_construct1(target: str, words: list, memo: dict = None):
    if not memo: memo = {}
    if target in memo: return memo[target]
    if target == '': return [[]]
    
    result = []
    for word in words:
        n = len(word)
        if target[:n] == word:
            suffix = target[n:]
            suffix_ways = all_construct1(suffix, words, memo)
            memo[suffix] = suffix_ways
            result += [[word] + s for s in suffix_ways]
    
    #memo[target] = result
    return result


def all_construct(target: str, words: list, memo: dict = None):
    if not memo: memo = {}
    if target in memo: return memo[target]
    if target == '': return [[]]
    
    result = []
    for word in words:
        n = len(word)
        if target[:n] == word:
            suffix = target[n:]
            suffix_ways = all_construct(suffix, words, memo)
            memo[suffix] = suffix_ways
            result += [[word] + s for s in suffix_ways]
    
    memo[target] = result
    return result



if __name__ == "__main__":
    from datetime import datetime
    target = 'abcdef'
    words = ['ab', 'abc', 'cd', 'def', 'abcd']
    target = 'e'*22 + 'f'
    words = ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']

    print('\n' + '-' * 10, f'can_construct({target},', words, ')' + '-' * 10)    
    
    time = datetime.now()
    res = all_construct(target, words)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Dynamic programming, O(n * m^2) time:   {time:10.0f} ms, solution:', res)
    
    time = datetime.now()
    res = all_construct1(target, words)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Dynamic programming1, O(n * m^2) time:  {time:10.0f} ms, solution:', res)

    time = datetime.now()
    res = all_construct0(target, words)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Dynamic programming0, O(n * m^2) time:  {time:10.0f} ms, solution:', res)
    
    time = datetime.now()
    res = all_construct_slow(target, words)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Brute force, O(m * n^m) time:           {time:10.0f} ms, solution:', res, '\n')
    
    
    print('\n' + '-' * 10, 'tests', '-' * 10)
    test_cases = [
        ('purple', ['purp', 'p', 'ur', 'le', 'purpl']), # 2 solutions
        ('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']), # 4 solutions
        ('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']), # 0 solutions
        ('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']), # 
        ('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']) # 0 solutions
    ]
    for target, words in test_cases:
        print(f'can_construct({target},', words, ') =\n')
        for r in all_construct(target, words):
            print(r)
        print()