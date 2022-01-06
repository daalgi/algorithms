"""
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, 
return true if word exists in the grid.

The word can be constructed from letters of sequentially 
adjacent cells, where adjacent cells are horizontally or 
vertically neighboring. The same letter cell may not be 
used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 
Follow up: Could you use search pruning to make your solution faster 
with a larger board?
"""
from dataclasses import dataclass, field
from typing import List
from copy import deepcopy


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


def with_trie(board: List[List[str]], word: str) -> bool:
    # Time complexity: O(M * N * 4^L)
    # Space complexity: O(L)
    # where `M` and `N` are the rows and columns of the board,
    # `L` is the length of the word
    # NOTE: the time complexity doesn't improve the brute force approach,
    # so there's no need to use a Trie for this problem.

    def dfs(r: int, c: int, chars: List[str], node: TrieNode) -> None:
        # Depth First Search

        # If the current node in the trie is a word, return true
        if node.is_word:
            return True

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
            if dfs(nr, nc, chars, node.letters[new_letter]):
                # If the word exists, return true
                return True
            # No need to explore other possibilities removing
            # the current character, there's only one word
            # chars.pop()

        # Change back the value of the current cell
        # to its original value
        board[r][c] = temp
        # Not found in the current path
        return False

    # Build a trie
    trie = Trie()
    trie.insert(word)
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

            # Explore the current cell
            if dfs(r, c, [letter], trie.root.letters[letter]):
                # If the word was found, return true
                return True

    # If not found
    return False


def brute_force(board: List[List[str]], word: str) -> bool:
    # Time complexity: O(M * N * 4^L)
    # Space complexity: O(L)
    # where `M` and `N` are the rows and columns of the board,
    # `L` is the length of the word

    def dfs(r: int, c: int, index: int):
        if index == word_length:
            return True

        temp, board[r][c] = board[r][c], "#"

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if (
                not (0 <= nr < rows)
                or not (0 <= nc < cols)
                or board[nr][nc] == "#"
                or board[nr][nc] != word[index]
            ):
                continue

            if dfs(nr, nc, index + 1):
                return True

        board[r][c] = temp
        return False

    word_length = len(word)
    # Possible cell moves
    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
    # Loop over the cells of the board
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):

            # If the character in the current cell is not
            # in any of the first character of the words,
            # skip this cell
            if board[r][c] != word[0]:
                continue

            # Explore the current cell
            if dfs(r, c, 1):
                # If the word was found, return true
                return True

    # If not found
    return False


if __name__ == "__main__":
    print("-" * 60)
    print("Word search")
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
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        [["a" for _ in range(20)] for _ in range(20)],
    ]

    test_cases = [
        # (board, word, solution)
        (boards[0], "abcd", False),
        (boards[0], "dcab", True),
        (boards[0], "dbac", True),
        (boards[0], "dcac", False),
        (boards[1], "oath", True),
        (boards[2], "oah", True),
        (boards[2], "oa", True),
        (boards[2], "vreno", False),
        (boards[3], "ABCCED", True),
        (boards[3], "SEE", True),
        (boards[3], "ADFCSEE", True),
        (boards[3], "ABCB", False),
        (boards[4], "qqqqqq", False),
        (boards[4], "aaaaaaaab", False),
        (boards[4], "aaaaaaaaa", True),
    ]

    for board, word, solution in test_cases:

        print("Word:", word)

        result = brute_force(deepcopy(board), word)
        output = f"\t brute_force ="
        output += " " * (20 - len(output)) + f"{result}"
        test_ok = result == solution
        output += " " * (60 - len(output)) + f"Test {'OK' if test_ok else 'NOT OK'}"
        print(output)

        result = with_trie(deepcopy(board), word)
        output = f"\t   with_trie ="
        output += " " * (20 - len(output)) + f"{result}"
        test_ok = result == solution
        output += " " * (60 - len(output)) + f"Test {'OK' if test_ok else 'NOT OK'}"
        print(output)

        print()
