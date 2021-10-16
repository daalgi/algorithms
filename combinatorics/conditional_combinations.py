from itertools import combinations


def conditional_combinations(iterable, r, pair_incompatibilities: set = None):
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
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1

        current_combination = tuple(pool[i] for i in indices)
        
        # Check if the current combination has incompatibilities
        if pair_incompatibilities and any(
            c in pair_incompatibilities for c in combinations(current_combination, 2)
        ):
            continue
        
        yield current_combination


if __name__ == "__main__":
    items = list(range(150))
    r = 4
    pair_incompatibilities = set([
        (3, 4),
        (4, 5),
        (4, 6),
    ])
    comb = conditional_combinations(items, r, pair_incompatibilities)
    print('Number of combinations:', len(list(comb)))
