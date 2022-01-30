"""
https://leetcode.com/problems/number-of-matching-subsequences/

Given a string s and an array of strings words, return 
the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from 
the original string with some characters (can be none) 
deleted without changing the relative order of the 
remaining characters.

For example, "ace" is a subsequence of "abcde".
 
Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a 
subsequence of s: "a", "acd", "ace".

Example 2:
Input: s = "dsahjpjauf", 
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2

Constraints:
1 <= s.length <= 5 * 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
"""
from typing import List
from collections import defaultdict


def two_pointers(words: List[str], target: str) -> int:
    # Time compleixty: O(n t)
    # Space complexity: O(1)
    # where `t` is the length of `target`
    # `n` is the number of `words`

    def is_subsequence(word: str, target: str) -> bool:
        w = len(word)
        i = j = 0
        while i < w and j < t:
            if word[i] == target[j]:
                i += 1
            j += 1
        return i == w

    t = len(target)
    count = 0
    for word in words:
        if is_subsequence(word, target):
            count += 1

    return count


def hashmap(words: List[str], target: str) -> int:
    # Time complexity: O(t + n log t)
    # Space complexity: O(t)
    # where `t` is the length of `target`
    # `n` is the number of `words`

    def is_subsequence(word: str) -> bool:
        # Time complexity: O(log t)
        # Space complexity: O(1)

        # Loop over the chars of `word`
        w = len(word)
        target_pointer = -1
        for i in range(w):

            # Check if the current char is in `target`
            if word[i] not in indices:
                return False

            # If the current char is in `target`,
            # but the largest index in `target` is
            # still smaller than the current `target_pointer`,
            # `source` is not a subsequence of `target`
            current_indices = indices[word[i]]
            if target_pointer >= current_indices[-1]:
                return False

            # Use binary search to optimize the look-up
            # of the left-most next `target_pointer`,
            # that is, find its smallest index which is greater
            # than the current `target_pointer`
            # (subsequence must respect the order in which the
            # characters appear)
            left, right = 0, len(current_indices) - 1
            while left < right:
                mid = (left + right) // 2
                if target_pointer < current_indices[mid]:
                    right = mid
                else:
                    left = mid + 1
            target_pointer = current_indices[right]

        return True

    # Store the indices of the chars of `target`
    # in a hashmap, for O(1) look-up
    t = len(target)
    indices = defaultdict(list)
    for i in range(t):
        indices[target[i]].append(i)

    count = 0
    for word in words:
        if is_subsequence(word):
            count += 1

    return count


def buckets_with_slicing(words: List[str], target: str) -> int:
    # Time complexity: O(t + L)
    # Space complexity: O(n)
    # where `t` is the length of the string `target`,
    # `n` is the length of the list `words`,
    # and `L` is sum of the length of all the `words`

    count = 0
    buckets = defaultdict(list)
    for word in words:
        buckets[word[0]].append(word[1:])

    for letter in target:
        curr_bucket = buckets[letter]
        buckets[letter] = []
        for suffix in curr_bucket:
            if not suffix:
                count += 1
            else:
                buckets[suffix[0]].append(suffix[1:])

    return count


def buckets_with_pointers(words: List[str], target: str) -> int:
    # Time complexity: O(t + L)
    # Space complexity: O(n)
    # where `t` is the length of the string `target`,
    # `n` is the length of the list `words`,
    # and `L` is sum of the length of all the `words`

    count = 0

    # Put the words into buckets by means of a hashmap
    # { first_char: [word1_suffix, word2_suffix, ...], }
    # Instead of words, keep the indices only, so we can
    # reduce the time complexity by no needing to slice words
    # { first_char: [(word_i, letter_i), (word_j, letter_j), ...], }
    buckets = defaultdict(list)
    for i, word in enumerate(words):
        buckets[word[0]].append((i, 0))

    # Loop over the letters of `target` (only once), O(t)
    for letter in target:
        curr_bucket = buckets[letter]
        buckets[letter] = []

        # Loop over the bucket for the current `letter`.
        for word_i, letter_i in curr_bucket:
            # print("\t", words[word_i], "->", words[word_i][letter_i])
            new_letter_i = letter_i + 1
            if new_letter_i == len(words[word_i]):
                count += 1
            else:
                buckets[words[word_i][new_letter_i]].append((word_i, new_letter_i))

    return count


def buckets_with_iterators(words: List[str], target: str) -> int:
    # Time complexity: O(t + L)
    # Space complexity: O(n)
    # where `t` is the length of the string `target`,
    # `n` is the length of the list `words`,
    # and `L` is sum of the length of all the `words`

    # Strategy: next letter pointer
    # since `target` can be very large, let's think about
    # ways to iterate through `target` only once.
    # Put words into buckets by starting char, i.e.
    #   ["dog", "cat", "cop"]
    #   {"d": {"og"}, "c": {"at", "op"}}

    ord_a = ord("a")
    count = 0
    buckets = [[] for _ in range(26)]
    for word in words:
        it = iter(word)
        buckets[ord(next(it)) - ord_a].append(it)

    for letter in target:
        letter_index = ord(letter) - ord_a
        curr_bucket = buckets[letter_index]
        buckets[letter_index] = []

        while curr_bucket:
            it = curr_bucket.pop()
            nxt = next(it, None)
            if nxt:
                buckets[ord(nxt) - ord_a].append(it)
            else:
                count += 1

    return count


if __name__ == "__main__":
    print("-" * 60)
    print("Number of matching subsequences")
    print("-" * 60)

    test_cases = [
        # (words, target, solution)
        (["b"], "a", 0),
        (["b", "a"], "aaabba", 2),
        (["bear", "abc", "dear", "ceda"], "abcdeabrd", 3),
        (["a", "bb", "acd", "ace"], "abcde", 3),
        (["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"], "dsahjpjauf", 2),
    ]

    for words, target, solution in test_cases:

        words_str = str(words)
        if len(words_str) > 60:
            words_str = words_str[:55] + " ...]"
        print("Words:", words_str)
        print("Target:", target)

        result = two_pointers(words, target)
        output = f"             two_pointers = "
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap(words, target)
        output = f"                  hashmap = "
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = buckets_with_iterators(words, target)
        output = f"   buckets_with_iterators = "
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = buckets_with_slicing(words, target)
        output = f"     buckets_with_slicing = "
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = buckets_with_pointers(words, target)
        output = f"    buckets_with_pointers = "
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
