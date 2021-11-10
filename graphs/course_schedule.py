"""
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, 
labeled from 0 to numCourses - 1. You are given an array 
prerequisites where prerequisites[i] = [ai, bi] indicates 
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 
you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
from collections import deque


def recursion_dfs(num_courses: int, prerequisites: list) -> bool:
    # Generate an adjacency list by means of a hashmap
    adj = {i: [] for i in range(num_courses)}
    for course, pre in prerequisites:
        adj[course].append(pre)

    # Use a set to keep track of the visited nodes (courses)
    # during a DFS path. If a course is revisited, there's a cycle
    # and the course schedule is not possible.
    visited = set()

    def dfs(course: int) -> bool:
        # DFS recursive function

        # Base cases
        if course in visited:
            # If the course has been visited during the current
            # DFS path, there's a cycle
            return False
        if adj[course] == []:
            # If the course has no prerequisites, the current
            # DFS is valid
            return True

        # Update the visited set
        visited.add(course)

        # Loop over the prerequisites of the current course
        for pre in adj[course]:
            if not dfs(pre):
                # If the DFS call for the current prerequisite
                # returns False, there's a cycle
                return False

        # If there're no cycles for the current course,
        # remove it from the `visited` set
        visited.remove(course)

        # To avoid unnecessary iterations, empty the adjacency list
        # for the current course, as if it were a course
        # with no prerequisites
        adj[course] = []

        return True

    # Loop over all the courses "manually", since the graph
    # could be not fully connected
    for course in range(num_courses):
        if not dfs(course):
            # If any connected graph returns False, there's a cycle,
            # so the course schedule is not possible
            return False

    # If there're no cycles, the course schedule is possible
    return True


def iter_dfs(num_courses: int, prerequisites: list) -> bool:
    # TODO correct implementation: one case not passing
    
    # Generate an adjacency list by means of a hashmap
    adj = {i: [] for i in range(num_courses)}
    for course, pre in prerequisites:
        adj[course].append(pre)

    # Loop over the courses one by one
    for course in range(num_courses):

        if adj[course] == []:
            # If the current course has no prerequisites,
            # skip the code below and continue with next iteration
            continue

        # Visited set used to detect cycles
        visited = set()

        # Stack to keep track of the prerequisites
        stack = deque(adj[course])

        # Loop over until the stack is empty
        while stack:

            pre = stack.pop()

            if pre in visited:
                # If the prerequisited has been visited, there's a cycle
                return False

            if adj[pre] == []:
                # If the current prerequisite has no prerequisites,
                # continue with next iteration
                continue

            # Set the current prerequisite as visited
            visited.add(pre)

            # Add the current prerequisite prerequisite's to the stack
            for p in adj[pre]:
                stack.append(p)

        # Update the current course adjacent list,
        # as it were a course with no prerequisites
        adj[course] = []

    return True


def iter_bfs(num_courses: int, prerequisites: list) -> bool:
    pass


if __name__ == "__main__":
    print("-" * 60)
    print("Course schedule")
    print("-" * 60)

    test_cases = [
        # (num_courses, prerequisites, is_possible)
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (3, [[1, 0], [2, 0], [2, 1]], True),
        (3, [[1, 0], [2, 0], [0, 2]], False),
        (8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]], True),
        (7, [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]], True),
    ]

    for num_courses, prerequisites, solution in test_cases:

        result = recursion_dfs(num_courses, prerequisites)
        string = f"recursion{num_courses, prerequisites} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = iter_dfs(num_courses, prerequisites)
        string = f"iterative{num_courses, prerequisites} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
