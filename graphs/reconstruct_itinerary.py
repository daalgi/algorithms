"""
https://leetcode.com/problems/reconstruct-itinerary/

You are given a list of airline tickets where 
tickets[i] = [fromi, toi] represent the departure 
and the arrival airports of one flight. 
Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", 
thus, the itinerary must begin with "JFK". If there are multiple 
valid itineraries, you should return the itinerary that has 
the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller 
lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. 
You must use all the tickets once and only once.

Example 1:
Input: tickets = [
    ["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]
]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [
    ["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],
    ["ATL","JFK"],["ATL","SFO"]
]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is 
["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Constraints:
1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
"""
from typing import List
from collections import defaultdict


def dfs_recursive(tickets: List[List[str]]) -> List[str]:
    # Time complexity: O(ElogE)
    # Space complexity: O(E)

    def dfs(node: str):
        # DFS recursive function

        # Loop over the nodes to which `node`
        # can travel from
        while adj[node]:
            next_node = adj[node].pop()
            dfs(next_node)

        # When there's no more nodes to travel
        # from the current `node`, `node` will be the
        # last destination in the current path
        # (we return the reversed list `route`)
        # i.e.
        #   adj = { 1: [3, 2], 2: [], 3: [1] }
        #           (sorted in reverse order)
        #   node = 1, adj[1].pop() = 2
        #       node = 2, adj[2] = [] --> route = [2]
        #       node = 3, adj[3].pop() = 1
        #           node = 1, adj[1] = [] --> route = [2, 1]
        #       node = 3, adj[3] = [] --> route = [2, 1, 3]
        #   node = 1, adj[1] = [] --> route = [2, 1, 3, 1]
        #   route[::-1] = [1, 3, 1, 2]
        route.append(node)

    # Adjacency list
    adj = defaultdict(list)
    for f, t in tickets:
        adj[f].append(t)

    # Sort in reverse order the adjacency list of each node,
    # so when we pop() them later on, we first pop the
    # first destination in lexicographic order
    # (instead of doing pop(0), which is more expensive computationally)
    for f in adj:
        if len(adj[f]) > 1:
            adj[f].sort(reverse=True)

    # DFS recursive call
    route = []
    dfs("JFK")
    return route[::-1]


if __name__ == "__main__":
    print("-" * 60)
    print("Reconstruct itinerary")
    print("-" * 60)

    test_cases = [
        # (tickets, solution)
        (
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
            ["JFK", "MUC", "LHR", "SFO", "SJC"],
        ),
        (
            [
                ["JFK", "SFO"],
                ["JFK", "ATL"],
                ["SFO", "ATL"],
                ["ATL", "JFK"],
                ["ATL", "SFO"],
            ],
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
        ),
    ]

    for tickets, solution in test_cases:

        print(f"Tickets:", tickets)
        result = dfs_recursive(tickets)
        output = f"  dfs_recursive = "
        output += " " * (20 - len(output))
        test_ok = solution == result
        output += f"{str(result)}"
        output += " " * (60 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
