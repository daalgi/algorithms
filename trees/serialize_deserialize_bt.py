"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or 
object into a sequence of bits so that it can be stored in a 
file or memory buffer, or transmitted across a network connection 
link to be reconstructed later in the same or another computer 
environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization 
algorithm should work. You just need to ensure that a binary tree 
can be serialized to a string and this string can be deserialized 
to the original tree structure.

Clarification: The input/output format is the same as how LeetCode 
serializes a binary tree. You do not necessarily need to follow this 
format, so please be creative and come up with different 
approaches yourself.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-1000 <= Node.val <= 1000
"""
from collections import deque
import sys

sys.path.insert(1, "./")

from tree_node import (
    TreeNode,
    list_traversal_to_bt,
    binary_tree_to_list,
    print_tree,
)


def bfs(root: TreeNode) -> int:
    # Breath First Search
    # Time complexity: O(n)
    # Space complexity: O(n)

    def serialize(root: TreeNode) -> str:
        # Edge case: empty tree
        if not root:
            return ""
        # List to store the nodes of the binary tree.
        # If a node has no children, those children
        # are represented null values (NULL = "N"),
        # unless they are leaf nodes at the last level.
        # Initialize it with the root value
        res = [str(root.data)]
        # Queue to keep track of the nodes at each level
        q = deque([root])
        while q:
            # Current length of the queue (in the current level)
            n = len(q)
            # Loop over the nodes in the current level
            for _ in range(n):
                # Current node from the queue
                node = q.popleft()
                # Loop over the children of the current node
                for child in [node.left, node.right]:
                    if child:
                        q.append(child)
                        res.append(str(child.data))
                    else:
                        # If there's no child, add a null sign
                        res.append(NULL)

        # Remove the null values at the end
        while res[-1] == NULL:
            res.pop()
        # print(res)

        return SEPARATOR.join(res)

    def deserialize(s: str) -> TreeNode:
        if not s:
            return None

        arr = s.split(SEPARATOR)
        n = len(arr)
        root = TreeNode(int(arr[0]))
        # Index of the `arr` list pointing to the next element
        i = 1
        # Queue to keep track of the nodes
        q = deque([root])
        # Loop while the queue has elements
        while q:
            node = q.popleft()
            if i < n and arr[i] != NULL:
                node.left = TreeNode(int(arr[i]))
                q.append(node.left)
            i += 1

            if i < n and arr[i] != NULL:
                node.right = TreeNode(int(arr[i]))
                q.append(node.right)
            i += 1

        return root

    SEPARATOR, NULL = ",", "N"
    s = serialize(root)
    new_root = deserialize(s)
    return new_root


def bfs2(root: TreeNode) -> TreeNode:
    def serialize(root: TreeNode) -> str:
        if not root:
            return ""
        res = ["#"]
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.data))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("#")

        return " ".join(res)

    def deserialize(s: str) -> TreeNode:
        if s == "# #":
            return None
        nodes = s.split()
        root = TreeNode(int(nodes[1]))
        q = deque([root])
        index = 1
        while q:
            node = q.popleft()

            index += 1
            if nodes[index] is not "#":
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)

            index += 1
            if nodes[index] is not "#":
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)

        return root

    if not root:
        return []
    s = serialize(root)
    new_root = deserialize(s)
    return new_root


def dfs_preorder(root: TreeNode) -> TreeNode:
    def serialize(node: TreeNode) -> TreeNode:
        if node:
            arr.append(str(node.data))
            serialize(node.left)
            serialize(node.right)
        else:
            arr.append(NULL)

    def deserialize() -> TreeNode:
        data = next(new_arr)
        if data == NULL:
            return None

        node = TreeNode(int(data))
        node.left = deserialize()
        node.right = deserialize()
        return node

    # Edge case
    if not root:
        return []

    # Config
    SEPARATOR, NULL = ",", "N"

    # Serialize
    arr = []
    serialize(root)
    # Can't omit the the NULLs at the end, otherwise
    # when deserializing, `next()` will reach the end of the list
    # and cause an error.
    # while arr[-1] == NULL:
    #     arr.pop()
    s = SEPARATOR.join(arr)

    # Deserialize
    # Make the array an iterator, so we can access
    # its elements with `next()`
    new_arr = iter(s.split(SEPARATOR))
    new_root = deserialize()

    return new_root


if __name__ == "__main__":
    print("-" * 60)
    print("Binary tree maximum path sum")
    print("-" * 60)

    test_cases = [
        # (input should equal output)
        ([]),
        ([1]),
        ([-10]),
        ([-10, 1]),
        ([1, 2, 10]),
        ([1, 2, 3, None, None, 4, 5]),
        ([1, 2, 3, 4, None, 6, 6]),
        ([1, 2, 3, None, None, 4, 5, 6, 7, 8, 9, None, 10, None, 11]),
        ([1, 2, 3, None, None, None, 4, 5, 6, 7, 8]),
    ]

    for nums in test_cases:

        root = list_traversal_to_bt(nums)
        print(">>> Binary Tree: " + "." * 20)
        print_tree(root)

        new_root = bfs(root)
        result = binary_tree_to_list(new_root)
        output = f"\n bfs = "
        print(output)
        if new_root:
            print_tree(new_root)

        new_root = bfs2(root)
        result = binary_tree_to_list(new_root)
        output = f"\n bfs2 = "
        print(output)
        if new_root:
            print_tree(new_root)

        new_root = dfs_preorder(root)
        result = binary_tree_to_list(new_root)
        output = f"\n dfs_preorder = "
        print(output)
        if new_root:
            print_tree(new_root)

        print()
