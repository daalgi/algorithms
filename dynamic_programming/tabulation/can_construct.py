"""
The function `can_construct(target, words)` accepts 
a target string and an array of strings.

It returns a boolean indicating whether or not the 
`target` can be constructed by concatenating elements of the
`words` array.

Elements of `words` may be reused as many times as needed.

--------------
Analysis:

m = len(target)
n = len(words)

time: O(m^2 * n)
space: O(m)

"""
def can_construct(target: str, words: list):
    n = len(target)
    table = [True] + [False] * n

    for i in range(n):
        if table[i]:
            for word in words:
                m = len(word)
                if target[i:i+m] == word:
                    if not table[i + m]:
                        table[i + m] = True
                        
    return table[n]


if __name__ == "__main__":
    from datetime import datetime
    target = 'abcdef'
    words = ['ab', 'abc', 'cd', 'def', 'abcd']
    print('\n' + '-' * 10, f'can_construct({target}, ', words, ')', '-' * 10)    
    
    time = datetime.now()
    res = can_construct(target, words)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'O(m^2 * n) time:   {time:10.0f} ms, solution:', res)
    
    print('\n' + '-' * 10, 'tests', '-' * 10)
    test_cases = [
        ('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], True),
        ('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], False),
        ('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], True),
        ('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'], False)
    ]
    for target, words, solution in test_cases:
        res = can_construct(target, words)
        print(f'can_construct({target}, ', words, ') = ', res,
            f'\tTest: {"OK" if solution == res else "?"}')
    print()
