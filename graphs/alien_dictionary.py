"""
https://leetcode.com/problems/alien-dictionary/

There is a new alien language that uses the English alphabet. However,
the order among the letters is unkown to you.

You are given a list of `words` from the alien language's dictionary,
where the strings in `words` are sorted lexicographically by the rules
of this new language.

Return a string of the unique letters in the new alien language sorted
in lexicographically increasing order by the new language's rules. If
there is no solution, return "". If there are multiple solutions,
return any of them.

A string `s` is lexicographically smaller than a string `t` if at the
first letter where they differ, the letter in `s` comes before the letter
in `t` in the alien language. If the first `min(s.length, t.length)`
letters are the same, then `s` is smaller if and only if 
`s.length < t.length`.

Example 1:
Input: words = ["wrt", "wrf", "er", "ett", "rftt"]
Output: "wertf"
"""
from collections import deque


def recursion_dfs(words: list) -> str:
    # Topological sort
    pass


def iter_bfs(words: list) -> str:
    # Topological sort
    # Time complexity: O(c) 
    #   where c is the total number of characters
    # Space complexity: O(1)
    #   since the size of the alphabet is constant (and small)

    # Create adjacency list
    adj = dict()
    for word in words:
        for c in word:
            if c not in adj:
                adj[c] = set()

    # Create an indegree list, which keeps track of the
    # number of incoming edges in each letter (26 letters)
    indegree = [0 for _ in range(26)]

    # Compare two words at a time, letter by letter
    for i in range(1, len(words)):
        first = words[i - 1]
        second = words[i]
        min_length = min(len(first), len(second))
        # Loop over the characters of both words
        for j in range(min_length):
            if first[j] == second[j]:
                # If both letters are equal, no relationship
                # can be inferred
                continue

            # Character from which the edge comes out
            char_out = first[j]
            # Character to which the edge comes in
            char_in = second[j]
            # If `char_in` relationship is not still in the
            # adjacency list for `char_out`, add it
            if char_in not in adj[char_out]:
                adj[char_out].add(char_in)
                # Update the `indegree` of the `char_in` character
                indegree[ord(char_in) - ord("a")] += 1

            # Once we found the first non-equal letter, break the loop
            break

        else:
            # In case the previous loop `j` ended without `break`,
            # there's an invalid/incongruent relationship,
            # so stop the algorithm
            return ""

    # BFS
    # Store the resulting characters in a list
    result = []
    # Initialize the queue with the characters with `indegree = 0`
    queue = deque([c for c in adj if indegree[ord(c) - ord("a")] == 0])
    # Loop over the characters in the queue until it's empty
    while queue:
        # Pop the first character in the queue and add it to the result
        c = queue.popleft()
        result.append(c)
        # Loop over the neighbors of the current character
        for neighbor in adj[c]:
            # Update the indegree list
            index = ord(neighbor) - ord("a")
            indegree[index] -= 1
            # If the current indegree = 0, then add it to the queue
            if indegree[index] == 0:
                queue.append(neighbor)

    return "".join(result) if len(result) == len(adj) else ""


if __name__ == "__main__":
    print("-" * 60)
    print("Alien dictionary")
    print("-" * 60)

    test_cases = [
        # (words, solution)
        (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
        (["z", "x"], "zx"),
        (["z", "x"], "zx"),
        (["z", "x", "z"], ""),
    ]

    for i, (words, solution) in enumerate(test_cases):

        # result = recursion_dfs(words)
        # string = f"recursion({i}) = "
        # string += " " * (15 - len(string))
        # string += str(result)
        # string += " " * (60 - len(string))
        # print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = iter_bfs(words)
        string = f"iter({i}) = "
        string += " " * (15 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
