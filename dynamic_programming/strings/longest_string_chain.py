"""
https://leetcode.com/problems/longest-string-chain/

You are given an array of words where each word consists 
of lowercase English letters.

wordA is a predecessor of wordB if and only if we can 
insert exactly one letter anywhere in wordA without 
changing the order of the other characters to make it 
equal to wordB.

- For example, "abc" is a predecessor of "abac", while 
"cba" is not a predecessor of "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] 
with k >= 1, where word1 is a predecessor of word2, word2 is 
a predecessor of word3, and so on. A single word is trivially 
a word chain with k == 1.

Return the length of the longest possible word chain with 
words chosen from the given list of words.

Example 1:
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is 
["a","ba","bda","bdca"].

Example 2:
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain 
["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

Example 3:
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one 
of the longest word chains.
["abcd","dbqca"] is not a valid word chain because 
the ordering of the letters is changed.

Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
"""
from typing import List


def dp_memoization(words: List[str]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(n L²)
    # Space complexity: O(n)

    def dfs(word: str) -> int:
        if word in memo:
            return memo[word]

        curr_chain = 1
        for i in range(len(word)):
            predecessor = word[:i] + word[i + 1 :]
            if predecessor in words:
                curr_chain = max(curr_chain, dfs(predecessor) + 1)

        return curr_chain

    words = set(words)
    memo = {}
    return max(dfs(word) for word in words)


def dp_tabulation(words: List[str]) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(nlogn + n L²)
    # Space complexity: O(n)
    # where `n` is the number of words,
    # and `L` the max length of the words

    # Sort the words by length so we only need
    # one loop to scan them
    words.sort(key=len)

    # Longest chain result, at least 1 (one word)
    longest_chain = 1

    # Hashmap { word: longest_chain_for_word }
    dp = {}

    for word in words:
        # Add the current word to the hashmap
        dp[word] = 1

        # Generate the current word possible predecessors
        # by removing one letter
        for i in range(len(word)):
            predecessor = word[:i] + word[i + 1 :]
            if predecessor in dp and dp[word] < dp[predecessor] + 1:
                dp[word] = dp[predecessor] + 1

        # Check if the current word is the last one belonging
        # to the longest chain
        if dp[word] > longest_chain:
            longest_chain = dp[word]

    return longest_chain


if __name__ == "__main__":

    print("-" * 60)
    print("Longest string chain")
    print("-" * 60)

    test_cases = [
        (["a"], 1),
        (["abcd", "dbqca"], 1),
        (["a", "b", "ba", "bca", "bda", "bdca"], 4),
        (["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5),
    ]

    for words, solution in test_cases:

        print("Words:", words)

        result = dp_memoization([*words])
        output = f"    dp_memoization = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation([*words])
        output = f"     dp_tabulation = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
