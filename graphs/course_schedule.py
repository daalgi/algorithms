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
To take course 1 you should have finished course 0, 
and to take course 0 you should also have finished course 1. 
So it is impossible.

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
        adj[pre].append(course)

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

        # Loop over the courses which have as a prerequisites
        # of the current course
        for next_course in adj[course]:
            if not dfs(next_course):
                # If the DFS call for the current `next_course`
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


def iter_bfs(num_courses: int, prerequisites: list) -> bool:
    # BFS

    # Generate an adjacency list by means of a hashmap
    adj = [[] for _ in range(num_courses)]
    for course, pre in prerequisites:
        # prerequisite: [course1, course2, ...]
        adj[pre].append(course)

    # Build indegree list to keep track of the number of incoming
    # edges in each node
    indegree = [0] * num_courses
    for course, pre in prerequisites:
        indegree[course] += 1

    # Keep track of the number of visited nodes
    count = 0
    # Initialize the queue with the courses with no prerequisites
    # (indegree = 0)
    queue = deque([c for c in range(num_courses) if indegree[c] == 0])
    # Loop over the courses until the queue is empty
    while queue:
        # Pop the next course
        course = queue.popleft()
        # Update the count of visited nodes
        count += 1
        # Loop over the courses that have as a prerequisite
        # the current course
        for next_course in adj[course]:
            # Reduce the incoming edges to the `next_course` course
            # due to the virtual removal of the current `course`
            indegree[next_course] -= 1
            # Check if there no prerequisites for the current
            # `next_course` course
            if indegree[next_course] == 0:
                # There're no prerequisites for the current `next_course`,
                # so add it to the queue
                queue.append(next_course)

    # Check the number of visited nodes:
    # - if not equal to the total number of courses, not ok,
    #   there's a cycle
    # - if equal to the total number of courses, ok, no cycles
    if count != num_courses:
        # There's a cycle, not possible to complete the courses
        return False
    # No cycles, it's possible to complete the courses
    return True


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
        (7, [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]], True),
        # Two components
        (8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]], True),
    ]

    for num_courses, prerequisites, solution in test_cases:

        result = recursion_dfs(num_courses, prerequisites)
        string = f"recursion_dfs{num_courses, prerequisites} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = iter_bfs(num_courses, prerequisites)
        string = f"iterative_bfs{num_courses, prerequisites} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()

    # case = 0
    # num_courses = test_cases[case][0]
    # prerequisites = test_cases[case][1]
    # print(num_courses, prerequisites)
    # print(iter_bfs(num_courses, prerequisites))
