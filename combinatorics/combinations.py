"""
https://docs.python.org/3/library/itertools.html#itertools.combinations

Python itertools.combinations
"""
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        # Determine the index `i` that will increment by 1
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            # Last combination reached
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)



if __name__ == "__main__":
    items = list(range(7))
    r = 3
    comb = combinations(items, r)
    print('Number of combinations:', len(list(comb)))
    for i in comb:
        print(i)