"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the 
letters of a different word or phrase, typically using 
all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from typing import List
from collections import defaultdict


def sorted_strings(strs: List[str]) -> List[List[str]]:
    # Time complexity: O(n²k klogk)
    # Space complexity: O(nk)
    # Strategy: use the sorted strings to decide whether a
    # string belongs to a group.

    # Keep track of the result `groups`
    groups = []
    # Keep track of the sorted string that defines each group
    # (used to decide whether the current string belongs to
    # a certain group)
    sorted_s_groups = []
    # Loop over the strings, O(n)
    n = len(strs)
    for i in range(n):
        # Sorte the current string, O(klogk)
        sorted_s = sorted(strs[i])
        # Loop over the current list of groups, O(n)
        for j in range(len(sorted_s_groups)):
            # If the current sorted string is equal to any
            # string in `sorted_s_groups`,
            # add the current string to that `group[j]`
            # Comparison O(k)
            if sorted_s == sorted_s_groups[j]:
                groups[j].append(strs[i])
                # If group found, get out the loop, and
                # continue with next `i` iteration
                break

        else:
            # If the previos `j` loop was not finished with `break`,
            # the current string doesn't belong to any group,
            # so create a new one
            groups.append([strs[i]])
            # and add the sorted string to the `sorted_s_groups`
            # for later comparisons
            sorted_s_groups.append(sorted_s)

    return groups


def sorted_strings_opt(strs: List[str]) -> List[List[str]]:
    # Time complexity: O(n klogk)
    # Space complexity: O(nk)
    # Strategy: use the sorted strings to decide whether a
    # string belongs to a group.
    # Use a dictionary mapping the sorted string with a group.
    # Note that strings are not hashable, so we can
    # use instead tuples of characters as keys of the dictionary.
    groups = defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return list(groups.values())


def char_counts(strs: List[str]) -> List[List[str]]:
    # Time complexity: O(nk)
    # Space complexity: O(nk)
    # Strategy: use the character count to decide whether a
    # string belongs to a group.
    # Use a dictionary mapping the character count with a group.
    # There are 26 English letters, so we can create a tuple
    # of length 26 and store the repetitions of each character.
    groups = defaultdict(list)
    ord_a = ord("a")
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord_a] += 1

        groups[tuple(count)].append(s)

    return list(groups.values())


if __name__ == "__main__":
    print("-" * 60)
    print("Group anagrams")
    print("-" * 60)

    test_cases = [
        ([""], [[""]]),
        (["a"], [["a"]]),
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
    ]

    for strs, solution in test_cases:

        print(f"Strings: {strs}")

        result = sorted_strings(strs)
        output = f"\t    sorted_strings = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sorted_strings_opt(strs)
        output = f"\tsorted_strings_opt = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = char_counts(strs)
        output = f"\t       char_counts = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
