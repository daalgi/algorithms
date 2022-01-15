"""
https://leetcode.com/problems/jump-game-iv/

Given an array of integers arr, you are initially positioned 
at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.

Return the minimum number of steps to reach the last 
index of the array.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. 
Note that index 9 is the last index of the array.

Example 2:
Input: arr = [7]
Output: 0
Explanation: Start index is the last index. 
You do not need to jump.

Example 3:
Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which 
is last index of the array.

Constraints:
1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8
"""
from typing import List
from collections import defaultdict, deque
import heapq


def bfs(arr: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    n = len(arr)
    if n == 1:
        return 0

    # Hashtable to identify the indices where each
    # number can be found in the input list `arr`
    # { number: [index_i, index_j, ...], ... }
    indices = defaultdict(list)
    for i in range(n):
        indices[arr[i]].append(i)

    # Hashset to keep track of the indices visited
    visited = set()
    # Queue to store the next jumps
    q = deque([(0, 0)])
    while q:
        steps, node = q.popleft()

        # If the current `node` is the last in `arr`,
        # return the number of steps
        if node == n - 1:
            return steps

        # If `node` has already been `visited`,
        # continue with the next one in the queue
        if node in visited:
            continue

        # Add the current `node` to the `visited` hashset
        visited.add(node)

        # Check the next nodes we can jump to directly
        # (same number in `arr`)
        for next_node in indices[arr[node]]:
            if next_node != node:
                q.append((steps + 1, next_node))

        # Check the nearby nodes (node - 1, node + 1)
        for next_node in [node - 1, node + 1]:
            if 0 < next_node < n:
                q.append((steps + 1, next_node))

        # Remove the indices for the
        # current number in `node`: arr[node].
        # This way we avoid adding them again to the queue later on
        indices[arr[node]] = []

    return


if __name__ == "__main__":
    print("-" * 60)
    print("Jump game IV")
    print("-" * 60)

    test_cases = [
        # (edges, source, destination, min_dist, path)
        ([1], 0),
        ([1, 3, 1], 1),
        ([1, 3, 2], 2),
        ([100, -23, -23, 404, 100, 23, 23, 23, 3, 404], 3),
        ([7, 6, 9, 6, 9, 6, 9, 7], 1),
        ([7] * 1000 + [1], 2),
    ]

    for arr, solution in test_cases:

        arr_str = str(arr)
        if len(arr_str) > 60:
            arr_str = arr_str[:55] + " ...]"
        print(f"Array:", arr_str)

        result = bfs(arr)
        output = f"    bfs = "
        output += " " * (15 - len(output))
        test_ok = solution == result
        output += f"{str(result)}"
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
