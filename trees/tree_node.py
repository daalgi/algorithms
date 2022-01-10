"""
TreeNode (Binary Search Tree)
"""
from collections import deque


class TreeNode:
    def __init__(self, d: int = 0):
        self.data = d
        self.size = 1
        self.left = None
        self.right = None
        self.parent = None

    def insert_in_order(self, d: int):
        if d <= self.data:
            if self.left is None:
                self.set_left_child(TreeNode(d))
            else:
                self.left.insert_in_order(d)
        else:
            if self.right is None:
                self.set_right_child(TreeNode(d))
            else:
                self.right.insert_in_order(d)

        self.size += 1

    def find(self, d: int):
        if d == self.data:
            return self
        elif d < self.data:
            return self.left.find(d) if self.left else None
        elif d > self.data:
            return self.right.find(d) if self.right else None
        return None

    def set_left_child(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def set_right_child(self, node):
        self.right = node
        if node is not None:
            node.parent = self


# def list_to_tree(arr: list) -> TreeNode:
#     if len(arr) == 0:
#         return None
#     root = TreeNode(arr[0])
#     for e in arr[1:]:
#         root.insert_in_order(e)
#     return root

# def create_binary_tree_from_list(arr: list, index: int = 0) -> TreeNode:
#     """
#     Function used for testing purposes.
#     arr = [1, None, 2, 3] represents the following Binary Tree:
#              1
#            /   \
#         None    2
#                /
#               3
#     """
#     if index >= len(arr) or arr[index] is None:
#         return None

#     if index == 0:
#         node = TreeNode(arr[0])

#     e = arr[index]
#     left = index * 2 + 1
#     right = left + 1
#     node = TreeNode(e)
#     node.left = create_binary_tree_from_list(arr, left)
#     node.right = create_binary_tree_from_list(arr, right)
#     return node


def binary_tree_to_list(root: TreeNode) -> list:
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            res.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return res


def list_traversal_to_bt(nums: list) -> TreeNode:
    if not nums:
        return None

    root = TreeNode(nums[0])
    queue = deque([root])
    i = 1
    n = len(nums)

    while queue:

        node = queue.popleft()
        if i < n and nums[i] is not None:
            num = nums[i]
            node.left = TreeNode(num)
            queue.append(node.left)
        i += 1

        if i < n and nums[i] is not None:
            num = nums[i]
            node.right = TreeNode(num)
            queue.append(node.right)
        i += 1

    return root


def sorted_array_to_bst(nums: list) -> TreeNode:
    n = len(nums)

    # The root of the tree will be
    # the middle point of the array
    mid = (n - 1) // 2
    root = TreeNode(nums[mid])

    # Base case
    if n == 1:
        return root

    # Use a stack to emulate the recursive call stack.
    # The stack contains a tuple of values (TreeNode, left, right),
    stack = deque([(root, 0, n - 1)])

    # Loop over until the stack is empty
    while stack:

        # Pop the last tuple in the stack
        node, left, right = stack.pop()
        # print('\n-->', left, mid, right, '>>', node.data)

        # Update the `node.data` for the popped node and
        # its boundaries `left` and `right`
        mid = (left + right) // 2
        node.data = nums[mid]

        # Check if there're still elements of the array to be added
        if mid < right:
            # If the `mid` index is less than the `right` index,
            # there're still nodes to be added to the tree in this side.
            # Create child node to the right with a default data (0),
            # which will be updated when popped from the stack
            node.right = TreeNode(0)
            node.right.parent = node
            # Add the child to the stack, along with the new array
            # boundaries for which the node is in the middle
            stack.append((node.right, mid + 1, right))

        if left < mid:
            # If the `left` index is less than the `mid` index,
            # there're still nodes to be added to the tree in this side.
            # Create child node to the left with a default data (0),
            # which will be updated when popped from the stack
            # Add the child to the stack, along with the new array
            # boundaries for which the node is in the middle
            node.left = TreeNode(0)
            node.left.parent = node
            stack.append((node.left, left, mid - 1))

    # Return the root node
    return root


def find_in_bst(root: TreeNode, data) -> TreeNode:
    # Finds a node in a Binary Search Tree
    if not root:
        return None
    if root.data == data:
        return root
    if root.data > data:
        return find_in_bst(root.left, data)
    if root.data < data:
        return find_in_bst(root.right, data)


def find_in_bt(root: TreeNode, data: int) -> TreeNode:
    # Finds a node in a Binary Tree
    if not root:
        return None
    if root.data == data:
        return root
    return find_in_bt(root.left, data) or find_in_bt(root.right, data)


def clone_bt(root: TreeNode) -> TreeNode:
    # Pre-order traversal - Recursive
    if not root:
        return None

    new_root = TreeNode(root.data)
    new_root.left = clone_bt(root.left)
    new_root.right = clone_bt(root.right)

    return new_root


def print_tree(node: TreeNode, level=0):
    if node != None:
        print_tree(node.left, level + 1)
        print(" " * 4 * level + "->", node.data)
        print_tree(node.right, level + 1)


def in_order_traversal(node: TreeNode):
    if node is not None:
        in_order_traversal(node.left)
        print(node.data)
        in_order_traversal(node.right)


def pre_order_traversal(node: TreeNode):
    if node is not None:
        print(node.data)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def post_order_traversal(node: TreeNode):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data)


if __name__ == "__main__":
    root = TreeNode(5)
    root.insert_in_order(1)
    root.insert_in_order(2)
    root.insert_in_order(3)
    root.insert_in_order(4)
    root.insert_in_order(6)
    root.insert_in_order(7)
    in_order_traversal(root)
