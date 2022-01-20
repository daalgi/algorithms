"""
https://leetcode.com/problems/strings-differ-by-one-character/

Given a list of strings dict where all the 
strings are of the same length.

Return true if there are 2 strings that only differ by 1 
character in the same index, otherwise return false.

Example 1:
Input: dict = ["abcd","acbd", "aacd"]
Output: true
Explanation: Strings "abcd" and "aacd" differ only by one 
character in the index 1.

Example 2:
Input: dict = ["ab","cd","yz"]
Output: false

Example 3:
Input: dict = ["abcd","cccc","abyd","abab"]
Output: true

Constraints:
The number of characters in dict <= 10^5
dict[i].length == dict[j].length
dict[i] should be unique.
dict[i] contains only lowercase English letters.
 

Follow up: Could you solve this problem in O(n * m) 
where n is the length of dict and m is the length of each string.
"""
from typing import List
from collections import defaultdict


def brute_force(strings: List[str]) -> bool:
    # Time complexity: O(n²m)
    # Space complexity: O(1)
    # where `n` is the number of strings,
    # and `m` is the length of each string.
    n = len(strings)
    m = len(strings[0])
    for i in range(n - 1):
        for j in range(i + 1, n):
            k, different = 0, 0
            while k < m and different < 2:
                if strings[i][k] != strings[j][k]:
                    different += 1
                k += 1

            if different <= 1:
                return True

    return False


def hashmap(strings: List[str]) -> bool:
    # Time complexity: O(nm²)
    # Space complexity: O(nm²)
    # where `n` is the number of strings,
    # and `m` is the length of each string.

    # Strategy: build a hashset of all the combinations of
    # strings with one different character, represented by "*",
    # i.e. ["*bcd", "a*cd", "ab*d", "abc*", ...]

    hashset = set()
    # Loop over the strings
    num_strings, len_string = len(strings), len(strings[0])
    for i in range(num_strings):
        # Current string
        s = strings[i]
        # Loop over the indices of the characters
        # of the current stringt
        for j in range(len_string):
            curr = s[:j] + "*" + s[j + 1 :]

            if curr in hashset:
                return True

            hashset.add(curr)

    return False


def hashmap2(strings: List[str]) -> bool:
    # Time complexity: O(nm²)
    # Space complexity: O(nm²)
    # where `n` is the number of strings,
    # and `m` is the length of each string.

    # Strategy: instead of building a hashset of
    # all the combinations of strings (see `hashmap` solution),
    # we can compare all strings removing one character
    # i.e. ["*bcd", "a*cd", "ab*d", "abc*", ...]

    # Loop over the indices of the characters
    # O(m)
    len_string = len(strings[0])
    for i in range(len_string):

        # For the given index, build a set of strings
        # without the character `i`, i.e.
        # strings = ["abcd", "abcc"], i = 0
        # seen = ["bcd", "bcc"]
        # No need to keep the combinations of different
        # chars `i`, we only care about 1 different char.
        seen = set()

        # Loop over the strings
        # O(n)
        for s in strings:
            # The current substring removing the `i` char
            # O(m)
            curr = s[:i] + s[i + 1 :]
            # Check if it's been already added to the hashset
            # O(m) (need to hash `curr`)
            if curr in seen:
                return True

            seen.add(curr)

    return False


def rolling_hash(strings: List[str]) -> bool:
    # Time complexity: O(nm)
    # Space complexity: O(nm)
    # where `n` is the number of strings,
    # and `m` is the length of each string.

    # Strategy: compute a hash for each string, and then
    # go through each character position `j`, compute the hash
    # without that character and check if it's in the list.

    # Limit hash large numbers with a large prime number
    mod = 1e9 + 7
    num_strings, len_string = len(strings), len(strings[0])

    # Build a list with the hashes of each string,
    # hash[i] = s[0] * 26 ** (m - 1)
    #         + s[1] * 26 ** (m - 2)
    #         + ...
    #         + s[m - 2] * 26 ** 1
    #         + s[m - 1] * 26 ** 0
    # where `m` is the num of chars in a string
    # `26` is the number of lowercase characters
    base = 26
    hashes = [0] * num_strings
    for i in range(num_strings):
        for j in range(len_string):
            hashes[i] = (base * hashes[i] + (ord(strings[i][j]) - ord("a"))) % mod

    # Loop over each character index
    # Note: loop from right-to-left to easily calculate the
    # multiplying factor for each `j` char index
    mult = 1
    for j in range(len_string - 1, -1, -1):

        # Hashtable to map a hash to the strings that produce
        # that hash. Include a list to account for collisions
        # { hash: [string1, string2, ...] },
        seen = defaultdict(list)

        # Loop over the strings
        for i in range(num_strings):
            # Hash for the string `i` removing the char `j`
            new_hash = (hashes[i] - mult * (ord(strings[i][j]) - ord("a"))) % mod
            if new_hash in seen:
                # If the new hash is in the set of `seen` hashes
                # for the current char index, make sure that the
                # strings are the same
                # (avoid collisions of two different strings
                # with the same hash)
                # Loop over the strings with hash `new_hash`
                for string in seen[new_hash]:
                    if sum(c1 != c2 for c1, c2 in zip(string, strings[i])) == 1:
                        # If the current string `string[i]` and the
                        # same hash `new_hash` and previously seen `string`
                        # have only one character different, return True
                        return True

            seen[new_hash].append(strings[i])

        # Update the char index multiplier for next iteration
        mult = base * mult % mod

    return False


if __name__ == "__main__":
    print("-" * 60)
    print("Strings differ by one character")
    print("-" * 60)

    test_cases = [
        # ( strings, solution )
        (["ab", "ad", "bc"], True),
        (["ab", "ba", "bc"], True),
        (["ab", "cd", "bc"], False),
        (["abcd", "acbd", "aacd"], True),
        (["abcd", "cccc", "abyd", "abab"], True),
        (["abcd", "cccc", "abyc", "abab"], False),
    ]

    for strings, solution in test_cases:

        print("Strings:", strings)

        result = brute_force(strings)
        output = f"    brute_force = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap(strings)
        output = f"        hashmap = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap2(strings)
        output = f"       hashmap2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = rolling_hash(strings)
        output = f"   rolling_hash = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
