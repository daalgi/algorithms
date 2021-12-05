"""
https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated 
sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused 
multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""


def hashset_not_valid(s: str, words: list) -> bool:
    # Time complexity: O(n+m)
    # Space complexity: O(n)

    # NOT VALID ALGORITHM!
    # It doesn't evaluate all possible solutions.
    # It can fail if a word in the dictionary
    # is a substring of another word in the dictionary.
    # We need to compute all possible solutions, and
    # use DP to avoid repeated work.

    # Convert the list of words to a hashset, O(n)
    wordset = set(words)
    # Loop over the characters of the string `s`
    # O(m)
    m = len(s)
    start, end = 0, 1
    while end <= m:
        if s[start:end] in wordset:
            # If the current string interval is in the dictonary,
            # update the `start` pointer
            start = end
        # Update the `end` pointer
        end += 1
    # If the last string inteval is in the dictionary
    if end - start == 1:
        return True
    return False


def brute_force_recc(s: str, words: list) -> bool:
    # Time complexity: O(n²)

    # Size of the string
    m = len(s)

    # Create a hashset from the list of words: O(n)
    hashset = set(words)

    def wb(start: int, end: int) -> bool:
        # Recursive function

        # Base case
        if start == end:
            # All the characters in the substring can
            # be divided into words contained in the hashset,
            # so the cursor `start` has reached `end`
            return True

        # Loop over the characters of the string
        # from the current start
        for i in range(start, end + 1):
            if (
                s[start : start + i] in hashset 
                and wb(start + i, end)
            ):
                # If the current substring is in the hashset
                # and the recursive call returns True,
                #
                return True

        return False

    return wb(0, m - 1)


def dp_iter(s: str, words: list) -> bool:
    # Size of the string `s`
    m = len(s)
    # Table to track at which indices there's a word in
    # the dictionary that fits, with no unmatched character.
    # It should have the size of the string `s` + 1.
    # We'll start from the end backwards, so the last
    # element is made True (base case)
    table = [False] * (m + 1)
    table[m] = True

    # Loop over the characters of the string,
    # from the end backwards
    for i in range(m - 1, -1, -1):
        # Loop over the words in the dictionary
        for word in words:
            n = len(word)
            # Check if `word` can fit in the current
            # index `i` of the string
            if i + n <= m and s[i : i + n] == word:
                # If the length is appropriate and the
                # characters match, update the table
                # for the current index `i` and make it
                # equal to the value in the forward index
                # `i + n`, where `n` is the length of the
                # current word. If there isn't any unmatched
                # character to the right and before the last
                # , then table[i] = True;
                # if
                table[i] = table[i + n]
            if table[i]:
                # If there's a word fitting in the current
                # index, early stop the `words` loop and
                # continue with the `i` loop
                break

    # Return the first index in the table.
    # If true, it means that there wasn't any unmatched
    # character.
    return table[0]


if __name__ == "__main__":
    print("-" * 60)
    print("Word break")
    print("-" * 60)

    test_cases = [
        ("abcde", ["ace", "ab", "de", "c"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("applependapple", ["apple", "pen"], False),
        ("applepenaaaapplea", ["apple", "pen", "a"], True),
        ("leetcode", ["leet", "code"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ]

    for s, words, solution in test_cases:

        print(words)

        result = hashset_not_valid(s, words)
        string = f"hashset_not_valid('{s}') = "
        string += " " * (45 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = dp_iter(s, words)
        string = f" brute_force_recc('{s}') = "
        string += " " * (45 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = dp_iter(s, words)
        string = f"          dp_iter('{s}') = "
        string += " " * (45 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
