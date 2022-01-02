"""
https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of strings 
words, return all words on the board.

Each word must be constructed from letters of 
sequentially adjacent cells, where adjacent cells 
are horizontally or vertically neighboring. The same 
letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],
["i","h","k","r"],["i","f","l","v"]], 
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 10^4
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class TrieNode:
    letters: dict = field(default_factory=dict)
    is_word: bool = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Time complexity: O(n)
        # where n is the length of the word
        curr = self.root
        for c in word:
            if c not in curr.letters:
                curr.letters[c] = TrieNode()
            curr = curr.letters[c]
        curr.is_word = True


def brute_force(board: List[List[str]], trie: Trie, num_words: int) -> List[str]:
    # Backtrack - Brute force
    # Time complexity: O(M * N * W * 4^(L))
    # Space complexity: O(W)
    # where `M` and `N` are the rows and columns of the board,
    # `W` is the number of words
    # `L` is the average length of a word
    # `S` is the sum of the length of all words
    pass


def backtrack(board: List[List[str]], trie: Trie, num_words: int) -> List[str]:
    # Backtrack - with a Trie data structure
    # Time complexity: O(M * N * 4^(L))
    # Space complexity: O(S)
    # where `M` and `N` are the rows and columns of the board,
    # `W` is the number of words
    # `L` is the average length of a word
    # `S` is the sum of the length of all words

    def dfs(r: int, c: int, chars: List[str], node: TrieNode) -> None:
        # Depth First Search

        # If the current node in the trie is a word,
        # add it to the result list
        if node.is_word:
            res.add("".join(ch for ch in chars))
            # To avoid to add the same word in future scans,
            # modify the trie
            node.is_word = False

        # To avoid revisiting the current cell during the
        # current path, temporarily modify the cell's value with a `#`
        temp, board[r][c] = board[r][c], "#"

        # Loop over the possible moves from the current cell
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            # Check if the new cell (nr, nc) is a valid
            # solution to further explore
            if (
                not (0 <= nr < rows)
                or not (0 <= nc < cols)
                or board[nr][nc] == "#"
                or board[nr][nc] not in node.letters
            ):
                continue

            new_letter = board[nr][nc]

            # Add the new character to the current word
            chars.append(new_letter)
            # Further explore
            dfs(nr, nc, chars, node.letters[new_letter])
            # Remove the new character added to further explore
            # other moves
            chars.pop()

        # Change back the value of the current cell
        # to its original value
        board[r][c] = temp
        return

    # Result set (using a list is slower in leetcode)
    res = set()
    # Possible cell moves
    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
    # Loop over the cells of the board
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):

            # Current letter (or character)
            letter = board[r][c]

            # If the character in the current cell is not
            # in any of the first character of the words,
            # skip this cell
            if letter not in trie.root.letters:
                continue

            # If the number of words in the result list
            # equals the number of words in the trie,
            # early stop (no further words can be added)
            if len(res) == num_words:
                return list(res)

            # Explore the current cell
            dfs(r, c, [letter], trie.root.letters[letter])

    # print(res)
    return list(res)


if __name__ == "__main__":
    print("-" * 60)
    print("Word search II")
    print("-" * 60)

    boards = [
        [["a", "b"], ["c", "d"]],
        [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        [
            ["o", "a", "b", "n"],
            ["o", "t", "a", "e"],
            ["a", "h", "k", "r"],
            ["a", "f", "l", "v"],
        ],
        [["a" for _ in range(20)] for _ in range(20)],
    ]

    test_cases = [
        # (board, words, solution)
        (boards[0], ["abcd"], []),
        (
            boards[0],
            ["abcd", "acdb", "bacd", "cdba", "dbac"],
            ["acdb", "bacd", "cdba", "dbac"],
        ),
        (
            boards[0],
            ["abcd", "ab", "ac", "dc", "da", "ad", "dcab", "dbca"],
            ["ac", "ab", "dc", "dcab"],
        ),
        (
            boards[1],
            ["vrenaaoeta", "vlfiihkreaaai", "vlfiihkreaaa"],
            ["vrenaaoeta", "vlfiihkreaaa"],
        ),
        (boards[1], ["oath", "pea", "eat", "rain"], ["oath", "eat"]),
        (boards[2], ["oa", "oaa"], ["oa", "oaa"]),
        (
            boards[3],
            ["qqqqqq", "eeeeeee", "a", "pppppppppp", "aa", "zzzz", "aao"],
            ["a", "aa"],
        ),
        (
            boards[3],
            ["a", "aa", "aaaa", "aaaaaa", "aaaaaaaa"],
            ["a", "aa", "aaaa", "aaaaaa", "aaaaaaaa"],
        ),
        (
            boards[3],
            ["aaaaaaaa", "aaaaaaaab", "aaaaaaaac", "aaaaaaaaa", "maaaaaa"],
            ["aaaaaaaa", "aaaaaaaaa"],
        ),
    ]

    for board, words, solution in test_cases:

        t = Trie()
        for word in words:
            t.insert(word)

        print("Words:", words)
        result = backtrack(board, t, len(words))
        output = f"\t backtrack ="
        output += " " * (15 - len(output)) + f"{result}"
        test_ok = sorted(result) == sorted(solution)
        output += " " * (60 - len(output)) + f"Test {'OK' if test_ok else 'NOT OK'}"
        print(output)

        print()
