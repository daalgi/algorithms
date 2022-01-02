"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the 
values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 10^4
0 <= Node.val <= 10^4
 
Follow up: If the BST is modified often 
(i.e., we can do insert and delete operations) 
and you need to find the kth smallest frequently, 
how would you optimize?
"""
import heapq
from collections import deque
import sys

sys.path.insert(1, "./")

from tree_node import (
    TreeNode,
    list_traversal_to_bt,
    print_tree,
)


def bfs_min_heap(root: TreeNode, k: int) -> int:
    # Breadth First Search
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Traverse the tree and store the values
    # in a min-heap.
    # IMPORTANT: it's much more efficient to
    # fill a list and later on turn it into a heap
    # than to fill a heap
    heap = []
    q = deque([root])
    while q:
        node = q.popleft()
        heap.append(node.data)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    # Transform the list into a min-heap
    heapq.heapify(heap)

    # Pop elements of the heap until k = 0
    kth_min = None
    while k:
        kth_min = heapq.heappop(heap)
        k -= 1

    return kth_min


def dfs_inorder(root: TreeNode, k: int) -> int:
    # Depth First Search - Inorder traversal
    # Time complexity: O(n)
    # Space complexity: O(n)

    def dfs(node: TreeNode) -> None:
        if not node:
            return
        dfs(node.left)
        arr.append(node.data)
        dfs(node.right)

    # Build an inorder traversal of the BST,
    # which will result in a list sorted in
    # ascending order
    arr = []
    dfs(root)
    return arr[k - 1]


def bfs_inorder(root: TreeNode, k: int) -> int:
    # Depth First Search - Inorder traversal
    # Time complexity: O(H + k)
    # Space complexity: O(H)
    #   where H is the height of the tree
    # Iterative version of DFS-inorder, which
    # removes the overhead of the recursion calls,
    # and can early stop once the kth-element
    # is reached.

    # Pointer to the current node
    node = root

    # Use a stack to
    stack = deque()
    while True:

        # Reach the bottom left child from the
        # current `node`, and stack all the nodes
        # along the way
        while node:
            stack.append(node)
            node = node.left

        # Pop the last node added to the stack
        # (the bottom left of the current subtree)
        node = stack.pop()
        # Return the kth-smallest element (k is 1 based)
        if k == 1:
            return node.data

        # Reduce k (we'll stop when k = 1)
        k -= 1
        # Next inorder
        node = node.right


if __name__ == "__main__":
    print("-" * 60)
    print("Kth smallest element in a BST")
    print("-" * 60)

    test_cases = [
        ([1], 1, 1),
        ([-10], 1, -10),
        ([2, 1], 1, 1),
        ([2, 1], 2, 2),
        ([2, 1, 3], 1, 1),
        ([2, 1, 3], 2, 2),
        ([2, 1, 3], 3, 3),
        ([3, 1, 4, None, 2], 3, 3),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
    ]

    for nums, k, solution in test_cases:

        root = list_traversal_to_bt(nums)
        print("Binary Tree:")
        print_tree(root)

        result = bfs_min_heap(root, k)
        output = f"\t bfs_min_heap = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dfs_inorder(root, k)
        output = f"\t  dfs_inorder = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)
        
        result = bfs_inorder(root, k)
        output = f"\t  bfs_inorder = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (45 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
