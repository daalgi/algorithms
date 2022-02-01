"""
https://leetcode.com/problems/satisfiability-of-equality-equations/

You are given an array of strings equations that 
represent relationships between variables where 
each string equations[i] is of length 4 and takes 
one of two different forms: "xi==yi" or "xi!=yi".
Here, xi and yi are lowercase letters (not necessarily 
different) that represent one-letter variable names.

Return true if it is possible to assign integers to 
variable names so as to satisfy all the given equations, 
or false otherwise.

Example 1:
Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, 
then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.

Example 2:
Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to 
satisfy both equations.

Constraints:
1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] is a lowercase letter.
equations[i][1] is either '=' or '!'.
equations[i][2] is '='.
equations[i][3] is a lowercase letter.
"""
from typing import List


def union_find(equations: List[str]) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)

    def find(child: str) -> str:
        if child not in parent:
            return child
        return find(parent[child])

    parent = {}
    for left, rel, _, right in equations:
        if rel == "=":
            left = find(left)
            right = find(right)
            if left != right:
                parent[left] = right

    for left, rel, _, right in equations:
        if rel == "!":
            if find(left) == find(right):
                return False

    return True


def union_find2(equations: List[str]) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)

    def find(child: str) -> str:
        if child in parent:
            if child == parent[child]:
                return child
            parent[child] = find(parent[child])

        else:
            parent[child] = child

        return parent[child]

    # Connected components hashmap { child: parent }
    parent = {}

    # Find the connected components defined by means
    # of all the equality equations
    for left, rel, _, right in equations:
        if rel == "=":
            left, right = find(left), find(right)
            if left != right:
                parent[right] = left

    # Loop over the inequality equations and check
    # whether the `left` and the `right` terms belong
    # to the same connected component
    # (there exists an equality relationship `rel`)
    for left, rel, _, right in equations:
        if rel == "!":
            if find(left) == find(right):
                # There exists an equality relationship
                # between `left` and `right`, so
                # the `equations` are incompatible
                return False

    return True


if __name__ == "__main__":
    print("-" * 60)
    print("Satisfiability of equality equations")
    print("-" * 60)

    test_cases = [
        (["a==b", "b!=a"], False),
        (["a==b", "b!=c"], True),
        (["a==b", "b!=c", "a==c"], False),
        (["b==a", "a==b", "a==c", "c==d", "d==e", "b==e", "a!=e"], False),
        (["b==a", "a==b", "a==c", "c==d", "d!=e", "b==e", "a!=e"], False),
        (["b==a", "a==b", "a==c", "c==d", "d!=e", "b!=e", "a!=e"], True),
    ]

    for equations, solution in test_cases:

        print(f"Equations:", str(equations))

        result = union_find(equations)
        output = f"     union_path = "
        output += f"{str(result)}"
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = union_find2(equations)
        output = f"    union_find2 = "
        output += f"{str(result)}"
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
