"""
CRACKING THE CODING INTERVIEW
10.2 Group anagrams:
Write a method to sort an array of strings so that all the
anagrams are next to each other.
"""
from collections import defaultdict


def group_anagrams(array: list) -> list:
    # Time complexity: O(n mlogm)
    # where `n` is the length of the array
    # and `m` is the length of the longest word in the array.
    # No other specific ordering of the words is required.

    # Hash table mapping words with the characters sorted
    # and the list of indices in `array` where those
    # can be found
    hashmap = defaultdict(list)

    # Loop over the words of the array to identify
    # the groups of anagrams
    n = len(array)
    for i in range(n):

        # String with the characters sorted
        s = "".join(sorted(array[i]))

        # Add the index to the mapping
        hashmap[s].append(i)

    # Loop over the stored indices of each anagram and build
    # the grouped list `res`
    res = list()
    for anagrams in hashmap:
        for index in hashmap[anagrams]:
            res.append(array[index])

    # Equivalent list comprehension method
    # return [array[index] for anagram in hashmap for index in hashmap[anagram]]

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Group anagrams")
    print("-" * 60)

    test_cases = [
        (["bad", "satan", "abd", "santa"], ["bad", "abd", "satan", "santa"]),
        (["care", "ba", "acre", "race"], ["care", "acre", "race", "ba"]),
    ]

    for array, solution in test_cases:

        result = group_anagrams([*array])

        string = f"sol{array} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
