"""
DISJOINT SET (UNION FIND)
The main idea is to have all connected vertices with the same
parent node (root), whether directly or indirectly connected.
To check if two vertices are connected, we only need to check
if they have the same root node.

Two main functions:
- The `find` function locates the root node of a given vertex.
- The `union` function connects two previously unconnected
vertices by giving the mthe same root node.

## Find function basic implementation:
```
def find(self, x):
    while x != self.root[x]:
        x = self.root[x]
    return x
```
## Find function optimized with path compression:
```
def find(self, x):
    if x == self.root[x]:
        return x
    self.root[x] = self.find(self.root[x])
    return self.root[x]
```
## Union function basic implementation
```
def union(self, x, y):
    rootX = self.find(x)
    rootY = self.find(y)
    if rootX != rootY:
        self.root[rootY] = rootX
```
## Union function optimized by union by rank
```
def union(self, x, y):
    rootX = self.find(x)
    rootY = self.find(y)
    if rootX != rootY:
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
```
"""


class UnionFindQuickFind:
    def __init__(self, size):
        # Time complexity: O(n)
        # Space complexity: O(n)
        self.root = [i for i in range(size)]
        self.size = size

    def find(self, x: int) -> int:
        # Time complexity: O(1)
        return self.root[x]

    def union(self, x: int, y: int):
        # Time complexity: O(n)
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # If the root of `y` is not the same,
            # update all the vertices whose root
            # is `root_y`
            for i in range(self.size):
                if self.root[i] == root_y:
                    self.root[i] = root_x

    def connected(self, x: int, y: int) -> bool:
        # Time complexity: O(1)
        return self.find(x) == self.find(y)


class UnionFindQuickUnion:
    def __init__(self, size):
        # Time complexity: O(n)
        # Space complexity: O(n)
        self.root = [i for i in range(size)]
        self.size = size

    def find(self, x: int) -> int:
        # Time complexity: O(n)
        # (only in the worst case, in general <= O(n),
        # so we can say that QuickUnion is faster than QuickFind)
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x: int, y: int):
        # Time complexity: O(n)
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

    def connected(self, x: int, y: int) -> bool:
        # Time complexity: O(n)
        return self.find(x) == self.find(y)


class UnionFindQuickUnionByRank:
    def __init__(self, size: int):
        # Time complexity: O(n)
        # Space comlexity: O(n)
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.size = size

    def find(self, x: int) -> int:
        # Time complexity: O(h) = O(logn)
        # where `h` is the height of the tree
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x: int, y: int):
        # Time complexity: O(h) = O(logn)
        # where `h` is the height of the tree
        # "Union by rank" selects the root of
        # the highest tree to become the root of
        # the shallowest tree.
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                # If both trees have equal height
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x: int, y: int) -> bool:
        # Time complexity: O(h) = O(logn)
        # where `h` is the height of the tree
        return self.find(x) == self.find(y)


class UnionFindPathCompression:
    def __init__(self, size: int):
        # Time complexity: O(n)
        # Space comlexity: O(n)
        self.root = [i for i in range(size)]

    def find(self, x: int) -> int:
        # Time complexity: O(logn)
        # Best case: O(1)
        # Worst case: O(n), when the tree is skewed
        # Average case: O(logn), when the tree is skewed
        # "Path compression" builds recursively a tree of height 1,
        # where the root has a direct edge to all the nodes.
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        # Time complexity: O(logn)
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

    def connected(self, x: int, y: int) -> bool:
        # Time complexity: O(logn)
        return self.find(x) == self.find(y)


class UnionFindPathCompressionUnionByRank:
    def __init__(self, size: int):
        # Time complexity: O(n)
        # Space complexity: O(n)
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x: int) -> int:
        # Time complexity: α(n) = O(1)
        # α(n) is O(1) on average
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        # Time complexity: α(n) = O(1)
        # α(n) is O(1) on average
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    print("-" * 60)
    print("Union find")
    print("-" * 60)

    edges_list = [
        # (edges, size)
        ([[0, 1], [1, 2], [2, 0], [3, 5], [1, 4]], 6),
        ([[0, 1], [3, 2], [2, 0], [3, 5], [1, 4]], 6),
        ([[0, 1], [1, 2], [2, 3], [3, 4], [5, 6]], 7),
    ]

    test_cases = [
        # (edges, size, check_vertices, solution)
        (*edges_list[0], [5, 1], False),
        (*edges_list[0], [2, 1], True),
        (*edges_list[1], [5, 1], True),
        (*edges_list[1], [4, 3], True),
        (*edges_list[2], [0, 4], True),
        (*edges_list[2], [0, 5], False),
    ]

    for i, (edges, size, check_vertices, solution) in enumerate(test_cases):

        if i == 0 or test_cases[i][0] != test_cases[i - 1][0]:
            print("\nEdges:", str(edges))

        print("Check vertices:", check_vertices)

        ufqf = UnionFindQuickFind(size)
        ufqu = UnionFindQuickUnion(size)
        ufqubr = UnionFindQuickUnionByRank(size)
        ufpc = UnionFindPathCompression(size)
        ufpcubr = UnionFindPathCompressionUnionByRank(size)

        for x, y in edges:
            ufqf.union(x, y)
            ufqu.union(x, y)
            ufqubr.union(x, y)
            ufpc.union(x, y)
            ufpcubr.union(x, y)

        result = ufqf.connected(*check_vertices)
        output = f"                     union_find_quick_find = "
        output += f"{str(result)}"
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = ufqu.connected(*check_vertices)
        output = f"                    union_find_quick_union = "
        output += f"{str(result)}"
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = ufqubr.connected(*check_vertices)
        output = f"            union_find_quick_union_by_rank = "
        output += f"{str(result)}"
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = ufpc.connected(*check_vertices)
        output = f"               union_find_path_compression = "
        output += f"{str(result)}"
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = ufpcubr.connected(*check_vertices)
        output = f" union_find_path_compression_union_by_rank = "
        output += f"{str(result)}"
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
