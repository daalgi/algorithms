"""
https://leetcode.com/problems/word-pattern/

Given a pattern and a string s, find if s 
follows the same pattern.

Here follow means a full match, such that there 
is a bijection between a letter in pattern 
and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


def hashmap(pattern: str, s: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)
    # Note: overly complicated solution
    words = s.split()
    n = len(pattern)
    if n != len(words):
        return False

    first_indices, words_set, groups, last_group = {}, set(), [], 0
    for i in range(n):
        if pattern[i] not in first_indices:
            # If it's the first appearance of the pattern's character
            if words[i] in words_set:
                return False
            first_indices[pattern[i]] = i
            words_set.add(words[i])
            groups.append(last_group)
            last_group += 1

        else:
            # If the character has already appeared
            if words[i] not in words_set:
                return False
            if words[i] != words[first_indices[pattern[i]]]:
                return False
            groups.append(groups[first_indices[pattern[i]]])

    return True


def hashmap2(pattern: str, s: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)

    words = s.split()

    # Check if the number of words is equal
    # to the number of characters in the pattern
    if len(pattern) != len(words):
        return False

    # Check if the number of unique words is the
    # same as the number of unique characters in the pattern
    if len(set(pattern)) != len(set(words)):
        return False

    # Loop over the words and characters, adding not yet seen
    # words and characters to the hashmap `word_to_pattern`
    #   word_to_pattern = { "word1": "a", "word2": "b", ...}
    word_to_pattern = {}
    for i in range(len(pattern)):
        if words[i] not in word_to_pattern:
            word_to_pattern[words[i]] = pattern[i]
        elif word_to_pattern[words[i]] != pattern[i]:
            return False

    return True


def hashmap3(pattern: str, s: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)
    words = s.split()
    # `map` and `string.index` or `list.index` example:
    #   s = "abcba"
    #   list(map(s.index, s)) = [0, 1, 2, 1, 0]
    return list(map(pattern.index, pattern)) == list(map(words.index, words))

def hashmap4(pattern: str, s: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)
    words = s.split()
    return [words.index(w) for w in words] == [pattern.index(p) for p in pattern]

def hashmap5(pattern: str, s: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)
    words = s.split()
    return len(words) == len(pattern) and len(set(zip(pattern, words))) == len(
        set(words)
    ) == len(set(pattern))


if __name__ == "__main__":
    print("-" * 60)
    print("Word pattern")
    print("-" * 60)

    test_cases = [
        # ( pattern, s, solution )
        ("a", "cat", True),
        ("ab", "cat dog", True),
        ("ab", "cat cat", False),
        ("aaa", "cat dog cat", False),
        ("aba", "cat dog cat", True),
        ("aab", "cat cat cat", False),
        ("bab", "dog cat cat", False),
        ("bab", "dog cat dog", True),
    ]

    for pattern, s, solution in test_cases:

        print("Pattern:", pattern)
        print("String:", s)

        result = hashmap(pattern, s)
        output = f"     hashmap = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap2(pattern, s)
        output = f"    hashmap2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap3(pattern, s)
        output = f"    hashmap3 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap4(pattern, s)
        output = f"    hashmap4 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap5(pattern, s)
        output = f"    hashmap5 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
