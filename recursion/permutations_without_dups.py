"""
CRACKING THE CODING INTERVIEW
8.7 Permutations without Dups (wihtout duplicates):
Write a method to compute all permutations of a string
of unique characters.
"""
from typing import List
import itertools


def iterative(s: str) -> List[str]:
    # Time complexity: O(n² * n!)
    # Space complexity: O(n * n!)
    # 2 characters: "12" -> "12", "21"
    # 3 characters: "123" -> "123", "132", "213", "231", "312", "321"
    # 4 characters: "1234" -> "1234", "1243", "1423", "1432", ...

    n = len(s)
    if n == 0:
        return [""]

    # Initialize the `permutations` list with the first
    # character of the string `s`. Build the respective
    # permutations by adding the following characters in `s`
    # to the different possible positions in the elements
    # of the current state of `permutations`,
    # i.e.:
    # permutations = ['a']
    # add 'b' at the different positions:
    #   'a' -> 'ba', 'ab',
    # permutations = ['ba', 'ab']
    # add 'c' at the different positions:
    #   'ba' -> 'cba', 'bca', 'bac'
    #   'ab' -> 'cab', 'acb', 'abc'
    # permutations = ['cba', 'bca', 'bac', 'cab', 'acb', 'abc']
    # etc.
    permutations = [s[0]]

    # Loop over the characters of the input string `s`
    for char_index in range(1, n):
        # Store the current permutations as we add characters
        # i.e., in the first iteration of "abcd"
        # permutations = ['a']
        # we would end up having:
        # curr = ['ba', 'ab']
        curr = []

        # Loop over the current permutations
        curr_len = len(permutations[0])
        for perm in permutations:

            # Loop over the indices of the current permutation
            for index in range(curr_len + 1):
                # The new permutation is the result of
                # adding the current character s[char_index]
                # to the current `index` in the current
                # permutation `perm`
                c = s[char_index]
                new_perm = perm[:index] + c + perm[index:]
                curr.append(new_perm)

        # Update the `permutations` list with the ones
        # computed in the current iteration
        permutations = curr[:]

    return permutations


if __name__ == "__main__":
    print("-" * 60)
    print("Permutations without Dups")
    print("-" * 60)

    test_cases = [
        ("", [""]),
        ("a", ["a"]),
        ("ab", ["ab", "ba"]),
        ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
        ("abcdef", itertools.permutations("abcdef")),
        ("qwerasdf", itertools.permutations("qwerasdf")),
        ("1234qwera", itertools.permutations("1234qwera")),
    ]

    for s, solution in test_cases:

        print(f">>> iterative('{s}')")
        result = iterative(s)

        result = sorted(result)
        string = str(result)
        if len(string) > 60:
            string = string[:60] + "...]"
        print(string)

        solution = sorted(["".join(sol) for sol in solution])

        string = " " * 60
        test_ok = sorted(list(solution)) == sorted(result)
        print(string, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')
