"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/

A company has n employees with a unique ID for each 
employee from 0 to n - 1. The head of the company is 
the one with headID.

Each employee has one direct manager given in the 
manager array where manager[i] is the direct manager 
of the i-th employee, manager[headID] = -1. Also, it 
is guaranteed that the subordination relationships 
have a tree structure.

The head of the company wants to inform all the company 
employees of an urgent piece of news. He will inform 
his direct subordinates, and they will inform their 
subordinates, and so on until all employees know about 
the urgent news.

The i-th employee needs informTime[i] minutes to inform 
all of his direct subordinates (i.e., After informTime[i] 
minutes, all his direct subordinates can start spreading 
the news).

Return the number of minutes needed to inform all the 
employees about the urgent news.

Example 1:
Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee 
in the company.

Example 2:
Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], 
informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is 
the direct manager of all the employees in the 
company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
 
Constraints:
1 <= n <= 10^5
0 <= headID < n
manager.length == n
0 <= manager[i] < n
manager[headID] == -1
informTime.length == n
0 <= informTime[i] <= 1000
informTime[i] == 0 if employee i has no subordinates.
It is guaranteed that all the employees can be informed.
"""
from typing import List
from collections import deque


def bfs_iter(
    n: int,
    head_id: int,
    manager: List[int],
    inform_time: List[int],
) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Build adjacency list:
    # [[sub1, sub2, ...], ...]
    adj = [[] for _ in range(n)]
    for i in range(n):
        if manager[i] > -1:
            adj[manager[i]].append(i)

    # Variable to keep track of the max time to reach all
    # the employees
    max_time = 0

    # BFS to explore all the company employees by levels
    # with a queue: (current_time, current_manager)
    q = deque([(0, head_id)])
    while q:
        curr_time, curr_manager = q.popleft()
        # Add the time that the current manager needs to inform
        # its subordinates
        curr_time += inform_time[curr_manager]

        # If the current manager has no subordinates,
        # check if the current time is the maximum so far
        if not adj[curr_manager] and curr_time > max_time:
            max_time = curr_time

        # Loop over the subordinates
        for sub in adj[curr_manager]:
            q.append((curr_time, sub))

    return max_time


if __name__ == "__main__":
    print("-" * 60)
    print("Time needed to inform all employees")
    print("-" * 60)

    test_cases = [
        # ( n, head_id, manager, inform_time, solution )
        (1, 0, [-1], [0], 0),
        (6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0], 1),
        (6, 2, [2, 2, -1, 0, 2, 2], [7, 0, 1, 0, 0, 0], 8),
        (
            15,
            0,
            [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            3,
        ),
    ]

    for n, head_id, manager, inform_time, solution in test_cases:

        print("Head id:", head_id)
        print("Manager:    ", manager)
        print("Inform time:", inform_time)

        result = bfs_iter(n, head_id, manager, inform_time)
        output = f"     bfs_iter = "
        output += f"{result:>4}"
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
