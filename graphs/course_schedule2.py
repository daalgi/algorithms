"""
https://leetcode.com/problems/course-schedule-ii/

There are a total of numCourses courses you have to take, 
labeled from 0 to numCourses - 1. You are given an array 
prerequisites where prerequisites[i] = [ai, bi] indicates 
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take 
course 0 you have to first take course 1.
Return the ordering of courses you should take to finish 
all courses. If there are many valid answers, return any 
of them. If it is impossible to finish all courses, 
return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. 
So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. 
To take course 3 you should have finished both courses 1 and 2. 
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. 
Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""
from collections import deque


def recursion_dfs(num_courses: int, prerequisites: list) -> bool:
    # Generate an adjacency list by means of a hashmap
    adj = [[] for _ in range(num_courses)]
    for course, pre in prerequisites:
        adj[pre].append(course)

    # Use a set to keep track of the visited nodes (courses)
    # during a DFS path. If a course is revisited, there's a cycle
    # and the course schedule is not possible.
    visited = set()

    # Resulting order list, pre-populated with the courses
    # that are not a prerequisite for other courses
    order = [c for c in range(num_courses) if adj[c] == []]

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
        # order.add(course)

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
        
        # Post-order appending the course
        order.append(course)

        # Empty the adjacency list for the current course,
        # as if it were a course with no prerequisites
        adj[course] = []

        return True

    # Loop over all the courses "manually", since the graph
    # could be not fully connected
    for course in range(num_courses):
        if adj[course] != [] and not dfs(course):
            # If any connected graph returns False, there's a cycle,
            # so the course schedule is not possible
            return []

    # If there're no cycles, the course schedule is possible.
    # Return the reversed `order` list (courses added post-order)
    return order[::-1]


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

    # Resulting order list
    order = []
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
        # Add the course to the resulting order list
        order.append(course)
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
        return []
    # No cycles, it's possible to complete the courses
    return order


if __name__ == "__main__":
    print("-" * 60)
    print("Course schedule II")
    print("-" * 60)

    test_cases = [
        # (num_courses, prerequisites, is_possible)
        (2, [[1, 0]], [0, 1]),
        (2, [[1, 0], [0, 1]], []),
        (3, [[1, 0], [2, 0], [2, 1]], [0, 1, 2]),
        (3, [[1, 0], [2, 0], [0, 2]], []),
        (
            7,
            [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]],
            [6, 5, 4, 2, 3, 0, 1],
        ),
        # Two components
        (8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]], [3, 4, 5, 6, 0, 2, 7, 1]),
    ]

    for i, (num_courses, prerequisites, solution) in enumerate(test_cases):

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

        if i >= len(test_cases) - 1:
            print("**NOTE: problem with non-unique solutions!")

        print()

    # case = 0
    # num_courses = test_cases[case][0]
    # prerequisites = test_cases[case][1]
    # print(num_courses, prerequisites)
    # print(iter_bfs(num_courses, prerequisites))
