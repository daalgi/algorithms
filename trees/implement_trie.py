"""
https://leetcode.com/problems/implement-trie-prefix-tree/

A trie (pronounced as "try") or prefix tree is a tree data 
structure used to efficiently store and retrieve keys in a 
dataset of strings. There are various applications of this 
data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is 
in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a 
previously inserted string word that has the prefix prefix, 
and false otherwise.

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, 
search, and startsWith.
"""
from dataclasses import dataclass, field


@dataclass
class TrieNode:
    children: dict = field(default_factory=dict)
    is_word: bool = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Time complexity: O(n)
        # where n is the length of the word
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        # Time complexity: O(n)
        # where n is the length of the word
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.is_word

    def starts_with(self, prefix: str) -> bool:
        # Time complexity: O(n)
        # where n is the length of the prefix
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


if __name__ == "__main__":
    print("-" * 60)
    print("Implement trie prefix tree")
    print("-" * 60)

    t = Trie()
    print(">> Initialize Trie\n")

    test_cases = [
        # (new_word, search, starts_with, search_after_insert)
        ("apple", False, False, True),
        ("app", False, True, True),
        ("apartment", False, False, True),
        ("bedroom", False, False, True),
        ("bed", False, True, True),
        ("python", False, False, True),
    ]

    for word, first_search, starts_with, second_search in test_cases:

        result = t.search(word)
        output = f"Does the word '{word}' exist?"
        output += " " * (45 - len(output)) + f"{result}"
        test_ok = result == first_search
        output += " " * (60 - len(output)) + f"Test {'OK' if test_ok else 'NOT OK'}"
        print(output)

        result = t.starts_with(word)
        output = f"Does any word start with '{word}'?"
        output += " " * (45 - len(output)) + f"{result}"
        test_ok = result == starts_with
        output += " " * (60 - len(output)) + f"Test {'OK' if test_ok else 'NOT OK'}"
        print(output)

        t.insert(word)
        print(f">> Insert word: '{word}'")

        result = t.search(word)
        output = f"Does the word '{word}' exist?"
        output += " " * (45 - len(output)) + f"{result}"
        test_ok = result == second_search
        output += " " * (60 - len(output)) + f"Test {'OK' if test_ok else 'NOT OK'}"
        print(output)

        print()
