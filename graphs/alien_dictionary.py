"""
https://leetcode.com/problems/alien-dictionary/
(premium)

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


def dfs_pre_order(
    c: str, visited: dict, adj: dict, res: list = None, verbose: bool = False
):
    # DFS recursive function
    # Pre-order dfs: append result before the recursive call

    if c in visited:
        # If the current character is in visited, return
        # the value its value in the dictionary
        # - if False, the node has been visited, but it's
        #   not in the current path, no problem.
        # - if True, the node is in the current path, we saw
        #   it twice, so there's a cycle.
        return visited[c]

    # Set the current character in the current paht
    visited[c] = True
    # DFS pre-order: append the result before the recursive call
    res.append(c)
    if verbose:
        print("Character", c)
        print("\t>>Neighbors:", adj[c])
        print("--> Append", c, "\tCurrent res", res)

    # Loop over the neighbors of the current character
    for neighbor in adj[c]:

        if dfs_pre_order(neighbor, visited, adj, res, verbose):
            # If the character is in the current path,
            # there's a cycle
            return True

    # Set the current character out of the current path,
    # so it'll be marked only as visited
    visited[c] = False


def dfs_post_order(
    c: str, visited: dict, adj: dict, res: list = None, verbose: bool = False
):
    # DFS recursive function
    # Post-order dfs: once the recursive call has finished,
    # we finally append the result

    if c in visited:
        # If the current character is in visited, return
        # the value its value in the dictionary
        # - if False, the node has been visited, but it's
        #   not in the current path, no problem.
        # - if True, the node is in the current path, we saw
        #   it twice, so there's a cycle.
        return visited[c]

    # Set the current character in the current paht
    visited[c] = True

    if verbose:
        print("Character", c)
        print("\t>>Neighbors:", adj[c])

    # Loop over the neighbors of the current character
    for neighbor in adj[c]:

        if dfs_post_order(neighbor, visited, adj, res, verbose):
            # If the character is in the current path,
            # there's a cycle
            return True

    # Set the current character out of the current path,
    # so it'll be marked only as visited
    visited[c] = False

    # Post-order dfs: once the recursive call has finished,
    # we finally append the result
    res.append(c)
    if verbose:
        print("--> Append", c, "\tCurrent res", res)


def recursion_dfs(words: list, pre: bool = True, verbose: bool = False) -> str:
    # Topological sort
    # Post-order DFS

    # Create adjacency list
    adj = {c: set() for word in words for c in word}

    # Compare two words at a time, letter by letter, to
    # populate the adjacency list (graph) with
    # lexicographic order relationships
    for i in range(1, len(words)):
        first = words[i - 1]
        second = words[i]
        min_len = min(len(first), len(second))
        for j in range(min_len):

            # If the letters are equal, continue with next iteration
            if first[j] == second[j]:
                continue

            # If the two characters are not equal, establish
            # the relationship between the first and the second
            adj[first[j]].add(second[j])

            # Once a first non-equal character has been detected,
            # break the foor loop
            break

    # Visited dictionary to keep track of visited nodes
    visited = {}  # False=visited, True=current path
    # Result list storing the characters in reverse order
    # (post-order dfs)
    res = []

    # Loop over the characters in the adjacency list
    for c in adj:
        if pre and dfs_pre_order(c, visited, adj, res, verbose):
            # If True, the character is in the current path,
            # so there's a cycle
            return ""
        elif not pre and dfs_post_order(c, visited, adj, res, verbose):
            # If True, the character is in the current path,
            # so there's a cycle
            return ""

    if pre:
        # Pre-order dfs
        return "".join(res)
    # Reverse list for post-order dfs
    return "".join(res[::-1])


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
        # No solution
        (["z", "x", "z"], ""),
        (["agr", "cx", "am", "bz"], ""),
        # Unique solutions
        (["z", "x"], "zx"),
        (["z", "x"], "zx"),
        (["aaa", "aab", "aac"], "abc"),
        # Multiple solutions:
        (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
        (["aab", "acb", "bb"], "acb"),
        (["aab", "aba", "cc"], "abc"),
        (["aab", "ab", "bm"], "abm"),
        (["wm", "wb", "m", "a"], "wmab"),
    ]

    for i, (words, solution) in enumerate(test_cases):

        result = recursion_dfs(words, pre=True)
        string = f" rec_dfs_pre({i}) = "
        string += " " * (15 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = recursion_dfs(words, pre=False)
        string = f"rec_dfs_post({i}) = "
        string += " " * (15 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = iter_bfs(words)
        string = f"    iter_bfs({i}) = "
        string += " " * (15 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        if i > len(test_cases) - 5:
            print("  ** Multiple valid solutions")

        print()

    print("\nVerbose example:")
    case = -3
    words = test_cases[case][0]
    print("Words:", words)
    print("\n>> DFS pre-order:\n")
    print("Result:", recursion_dfs(words, pre=True, verbose=True))
    print("\n\n>> DFS post-order:\n")
    print("Result:", recursion_dfs(words, pre=False, verbose=True))
    print()
