"""
CRACKING THE CODING INTERVIEW
4.12 Path with sum:
You are given a binary tree in which each node contains an 
integer value (which might be positive or negative). 
Design an algorithm to count the number of paths that sum 
to a given value. The path does not need to start or end at 
the root or a leaf, but it must go downwards (traveling only 
from parent nodes to child nodes).

https://leetcode.com/problems/path-sum-iii/

Given the root of a binary tree and an integer 
targetSum, return the number of paths where 
the sum of the values along the path equals 
targetSum.

The path does not need to start or end at the 
root or a leaf, but it must go downwards (i.e., 
traveling only from parent nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], 
targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], 
targetSum = 22
Output: 3

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 10^9
-1000 <= targetSum <= 1000

"""
from collections import defaultdict
import sys

sys.path.insert(1, "./")


from tree_node import (
    TreeNode,
    sorted_array_to_bst,
    print_tree,
)


def brute_force(root: TreeNode, target: int) -> int:
    # Brute Force, looking at all possible paths.
    # Strategy: traverse to each node, and recursively
    # try all paths downwards.
    # Time complexity: O(n²)
    # Space complexity: O(n)

    def dfs(node: TreeNode, running_sum: int, first_time_visited: bool) -> None:
        # Base case: reached a leaf, stop
        if not node:
            return

        nonlocal count
        # Add the current node to the current sum
        running_sum += node.data
        if running_sum == target:
            count += 1

        # Continue exploring the current path
        dfs(node.left, running_sum, False)
        dfs(node.right, running_sum, False)

        # Start a new path from the current node children,
        # as if the starting node starts at
        # `node.left` and `node.right`.
        # Use the flag `first_time_visited` to avoid
        # exploring the same path twice
        if first_time_visited:
            dfs(node.left, 0, True)
            dfs(node.right, 0, True)

    count = 0
    dfs(root, 0, True)
    return count


def one_scan(root: TreeNode, target: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    def dfs(node: TreeNode, running_sum: int) -> None:
        # Base case: reached leaf node
        if not node:
            return

        nonlocal count

        # Update `running_sum` with the current `node`
        running_sum += node.data
        
        # Check the difference with `target`,
        # effectively as a "prefix_sum on the fly", example:
        # target = 3
        # path1: 4 -> 2 -> 1
        #   node = 4, running_sum = 4, diff = 1, prev_sums={0: 1}
        #   node = 2, running_sum = 6, diff = 3, prev_sums={0: 1, 4: 1}
        #   node = 1, running_sum = 7, diff = 4, prev_sums={0: 1, 4: 1, 6: 1}
        #       --> diff in prev_sum --> count += 1
        # path1: 4 -> 2 -> 3
        #   node = 3, running_sum = 9, diff = 6, prev_sums={0: 1, 4: 1, 6: 1}
        #       --> diff in prev_sum --> count += 1
        diff = running_sum - target
        if diff in prev_sums:
            count += prev_sums[diff]

        # Add `running_sum` to the hashmap
        prev_sums[running_sum] += 1

        # Further explore the subtrees
        dfs(node.left, running_sum)
        dfs(node.right, running_sum)

        # Remove `running_sum` after finishing the path
        prev_sums[running_sum] -= 1

    # Total number of paths summing up `target`
    count = 0
    # Hashmap to keep track of the count of running sums
    # for a given path { sum: count }
    prev_sums = defaultdict(int)
    # Initialize the count running_sum 0, frequency 1,
    # so if we have
    #   running_sum = 3 + 4 + 1,  target = 8
    #   diff = running_sum - target = 0
    #   diff in prev_sums --> count = 1
    prev_sums[0] = 1
    
    dfs(root, 0)
    return count


if __name__ == "__main__":
    print("-" * 60)
    print("Path sum III")
    print("-" * 60)

    array = [1, 2, 3, 4, 5, 6, 7, 8]
    test_cases = [
        # ( sorted_array_to_bst, target, solution )
        (array, 1, 1),
        (array, 2, 1),
        (array, 3, 2),
        (array, 4, 1),
        (array, 5, 2),
        (array, 6, 2),
        (array, 7, 2),
        (array, 8, 1),
        (array, 9, 1),
        (array, 10, 1),
        (array, 11, 1),
        (array, 12, 0),
        (array, 13, 1),
    ]

    print("\n>>>>> Binary Tree:")
    case = 0
    arr = test_cases[case][0]
    root = sorted_array_to_bst(arr)
    print_tree(root)

    for nums, target, solution in test_cases:

        print("Target:", target)
        root = sorted_array_to_bst(nums)

        result = brute_force(root, target)
        output = f"     brute_force = "
        output += str(result)
        output += " " * (45 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = one_scan(root, target)
        output = f"        one_scan = "
        output += str(result)
        output += " " * (45 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
