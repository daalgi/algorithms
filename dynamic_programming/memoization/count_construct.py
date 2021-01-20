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

Height of the tree: m (worst case scenario)
Each node might have up to n sub-nodes (worst case scenario)

Brute force:
time: O(m * n^m)
space: O(m^2)

Memoized:
time: O(n * m^2)
space: O(m^2)

"""
def count_construct_slow(target: str, words: list):
    if target == '': return 1
    
    count = 0
    for word in words:
        n = len(word)
        if target[:n] == word:
            num_ways_for_rest = count_construct_slow(target[n:], words)
            count += num_ways_for_rest
    
    return count


def count_construct0(target: str, words: list, memo: dict = None):
    if not memo: memo = {}
    if target in memo: return memo[target]
    if target == '': return 1

    count = 0
    for word in words:
        n = len(word)
        if target[:n] == word:
            suffix = target[n:]
            num_ways_for_rest = count_construct0(suffix, words, memo)
            #memo[suffix] = num_ways_for_rest
            count += num_ways_for_rest
    
    memo[target] = count
    return count


def count_construct1(target: str, words: list, memo: dict = None):
    if not memo: memo = {}
    if target in memo: return memo[target]
    if target == '': return 1

    count = 0
    for word in words:
        n = len(word)
        if target[:n] == word:
            suffix = target[n:]
            num_ways_for_rest = count_construct1(suffix, words, memo)
            memo[suffix] = num_ways_for_rest
            count += num_ways_for_rest
    
    #memo[target] = count
    return count


def count_construct(target: str, words: list, memo: dict = None):
    if not memo: memo = {}
    if target in memo: return memo[target]
    if target == '': return 1

    count = 0
    for word in words:
        n = len(word)
        if target[:n] == word:
            suffix = target[n:]
            num_ways_for_rest = count_construct(suffix, words, memo)
            memo[suffix] = num_ways_for_rest
            count += num_ways_for_rest
    
    memo[target] = count
    return count



if __name__ == "__main__":
    from datetime import datetime
    #target = 'abcdef'
    #words = ['ab', 'abc', 'cd', 'def', 'abcd']
    target = 'e'*22 + 'f'
    words = ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']

    print('\n' + '-' * 10, f'can_construct({target},', words, ')' + '-' * 10)    
    
    time = datetime.now()
    res = count_construct(target, words)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Dynamic programming, O(n * m^2) time:   {time:10.0f} ms, solution:', res)
    
    time = datetime.now()
    res = count_construct1(target, words)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Dynamic programming1, O(n * m^2) time:  {time:10.0f} ms, solution:', res)

    time = datetime.now()
    res = count_construct0(target, words)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Dynamic programming0, O(n * m^2) time:  {time:10.0f} ms, solution:', res)

    time = datetime.now()
    res = count_construct_slow(target, words)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Brute force, O(m * n^m) time:           {time:10.0f} ms, solution:', res, '\n')
    
    
    print('\n' + '-' * 10, 'tests', '-' * 10)
    test_cases = [
        ('purple', ['purp', 'p', 'ur', 'le', 'purpl']), # 2
        ('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']), # 1
        ('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']), # 0
        ('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']), # 4
        ('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']) # 0
    ]
    for target, words in test_cases:
        print(f'can_construct({target},', words, ') = ', count_construct(target, words))