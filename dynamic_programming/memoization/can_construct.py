"""

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
def can_construct_slow(target: str, words: list):
    if target == '': return True
    
    for word in words:
        n = len(word)
        if target[:n] == word:
            if can_construct_slow(target[n:], words):
                return True
    
    return False


def can_construct0(target: str, words: list, memo: dict = None):
    if not memo: memo = {}
    if target in memo: return memo[target]
    if target == '': return True

    for word in words:
        n = len(word)
        if target[:n] == word:
            suffix = target[n:]
            if can_construct0(suffix, words, memo):
                memo[target] = True
                return True
    
    memo[target] = False
    return False


def can_construct(target: str, words: list, memo: dict = None):
    if not memo: memo = {}
    if target in memo: return memo[target]
    if target == '': return True

    for word in words:
        n = len(word)
        if target[:n] == word:
            suffix = target[n:]
            memo[suffix] = can_construct(suffix, words, memo)
            if memo[suffix]:
                return True
    
    memo[target] = False
    return False



if __name__ == "__main__":
    from datetime import datetime
    #target = 'abcdef'
    #words = ['ab', 'abc', 'cd', 'def', 'abcd']
    target = 'e'*500 + 'f'
    words = ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']
    print('\n' + '-' * 10, f'can_construct({target},', words, ')' + '-' * 10)
    
    time = datetime.now()
    res = can_construct0(target, words)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Dynamic programming0, O(n * m^2) time: {time:10.0f} ms, solution:', res)
    
    time = datetime.now()
    res = can_construct(target, words)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Dynamic programming, O(n * m^2) time:  {time:10.0f} ms, solution:', res)
    
    """
    time = datetime.now()
    res = can_construct_slow(target, words)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Brute force, O(m * n^m) time:          {time:10.0f} ms, solution:', res, '\n')
    """
    
    print('\n' + '-' * 10, 'tests', '-' * 10)
    test_cases = [
        ('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']), # true
        ('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']), # false
        ('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']), # true
        ('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']) # false
    ]
    for target, words in test_cases:
        print(f'can_construct({target},', words, ') = ', can_construct(target, words))
    