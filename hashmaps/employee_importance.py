"""
https://leetcode.com/problems/employee-importance/

You have a data structure of employee information, 
including the employee's unique ID, importance value, 
and direct subordinates' IDs.

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee.
employees[i].importance is the importance value of 
the ith employee.
employees[i].subordinates is a list of the IDs of 
the direct subordinates of the ith employee.

Given an integer id that represents an employee's ID, 
return the total importance value of this employee and 
all their direct and indirect subordinates.

Example 1:
Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
Output: 11
Explanation: Employee 1 has an importance value of 5 and 
has two direct subordinates: employee 2 and employee 3.
They both have an importance value of 3.
Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.

Example 2:
Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
Output: -3
Explanation: Employee 5 has an importance value of -3 and 
has no direct subordinates.
Thus, the total importance value of employee 5 is -3.

Constraints:
1 <= employees.length <= 2000
1 <= employees[i].id <= 2000
All employees[i].id are unique.
-100 <= employees[i].importance <= 100
One employee has at most one direct leader and may have several subordinates.
The IDs in employees[i].subordinates are valid IDs.
"""
from typing import List
from collections import deque


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def hashtable_bfs(employees: List[int], id: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    hashmap = {e.id: e for e in employees}
    q = deque([hashmap[id]])
    value = 0
    while q:
        emp = q.popleft()
        value += emp.importance

        for sub_id in emp.subordinates:
            if sub_id in hashmap:
                q.append(hashmap[sub_id])

        del hashmap[emp.id]

    return value


def hashtable_bfs2(employees: List[int], id: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    hashmap = {e.id: e for e in employees}
    q = deque([hashmap[id]])
    value = 0
    while q:
        emp = q.popleft()
        value += emp.importance

        for sub_id in emp.subordinates:
            # Each subordinate has only one manager,
            # no need to keep track of the already
            # added employees
            q.append(hashmap[sub_id])

    return value


def hashtable_dfs(employees: List[int], id: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    def dfs(emp_id: int) -> int:
        sub_imp = sum(dfs(sub_id) for sub_id in hashmap[emp_id].subordinates)
        return sub_imp + hashmap[emp_id].importance

    hashmap = {e.id: e for e in employees}
    return dfs(id)


if __name__ == "__main__":
    print("-" * 60)
    print("Employee importance")
    print("-" * 60)

    test_cases = [
        # (employees, id, solution)
        # where employee_i = [id, importance, subordinates]
        ([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1, 11),
        ([[1, 2, [5]], [5, -3, []]], 5, -3),
        ([[101, 3, []], [2, 5, [101]]], 2, 8),
        ([[1, 5, [2, 3]], [2, 3, [4]], [3, 4, []], [4, 1, []]], 1, 13),
    ]

    for employees, id, solution in test_cases:

        print("Employees:", employees)
        print("id:", id)

        employees = [Employee(*e) for e in employees]

        res = hashtable_bfs(employees, id)
        output = "    hashtable_bfs = "
        output += str(res)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if res == solution else "NOT OK"}'
        print(output)

        res = hashtable_bfs2(employees, id)
        output = "   hashtable_bfs2 = "
        output += str(res)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if res == solution else "NOT OK"}'
        print(output)

        res = hashtable_dfs(employees, id)
        output = "    hashtable_dfs = "
        output += str(res)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if res == solution else "NOT OK"}'
        print(output)

        print()
