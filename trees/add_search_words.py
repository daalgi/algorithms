"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words and 
finding if a string matches any previously added string.

Implement the WordDictionary class:
- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, 
it can be matched later.
- bool search(word) Returns true if there is any string 
in the data structure that matches word or false otherwise. 
word may contain dots '.' where dots can be matched with any letter.

Example:
Input
["WordDictionary","addWord","addWord","addWord","search",
"search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:
1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
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
        return self.search_suffix(word, 0, len(word), self.root)

    def search_suffix(self, word: str, start: int, end: int, node: TrieNode) -> bool:
        # Time complexity: O(n)
        # where n is the length of the `word`

        # Loop over the characters of `word`, from `start` to `end`
        for i in range(start, end):
            if word[i] == ".":
                # If the current character is `.`, any letter is valid,
                # so we can explore all the different paths and return
                # True if any of those has a word with the following
                # characters (from `i + 1` to `end`)
                for next_node in node.children.values():
                    if self.search_suffix(word, i + 1, end, next_node):
                        return True
                # If there was no path returning a word, return False
                return False

            elif word[i] not in node.children:
                # If the current character is not in the current TrieNode,
                # the word doesn't exist
                return False

            # Update pointer to the children node containing the
            # current character
            node = node.children[word[i]]

        # Once reached the end, return if the current node
        # is the end of a word
        return node.is_word


if __name__ == "__main__":
    print("-" * 60)
    print("Design `add` and `search` words data structure")
    print("-" * 60)

    t = Trie()
    words = ["bad", "dad", "mad"]
    for word in words:
        t.insert(word)
    print(">> Initialize Trie")
    print("Words:", words, "\n")

    test_cases = [
        # (search_word, solution)
        ("apple", False),
        ("bad", True),
        ("ba.", True),
        ("b.d", True),
        (".ad", True),
        (".a.", True),
        (".u.", False),
        ("...", True),
        ("..", False),
    ]

    for word, solution in test_cases:

        result = t.search(word)
        output = f"Does the word '{word}' exist?"
        output += " " * (45 - len(output)) + f"{result}"
        test_ok = result == solution
        output += " " * (60 - len(output)) + f"Test {'OK' if test_ok else 'NOT OK'}"
        print(output)
