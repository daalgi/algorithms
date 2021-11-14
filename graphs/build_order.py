"""
CRACKING THE CODING INTERVIEW
4.7 Build Order:
You are given a list of projects and a list of dependencies 
(which is a list of pairs of projects, where the second project
is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow
the projects to be built. 
If there is no valid build order, return an error.

Example:
input: projects = (a, b, c, d, e, f)
       dependencies = (a, d), (f, b), (b, d), (f, a), (d, c)
output: [f, e, a, b, d, c]
"""


from collections import deque


def recursion(num_projects: int, dependencies: list) -> list:
    # DFS post-order - Topsort
    # Time complexity: O(V + E)

    # Edge case
    if num_projects == 0:
        return []

    # Build the adjacency list
    adj = [[] for _ in range(num_projects)]
    for dependency, project in dependencies:
        # dependency -> [project1, project2, ...]
        adj[dependency].append(project)

    # Set to keep track of the built dependencies
    built = set()

    # Resulting list with the build order.
    # Pre-populate it with the projects that are no
    # other project's dependecy
    res = [i for i in range(num_projects) if adj[i] == []]

    def dfs(dependency: int):
        # DFS recursive function
        # Base cases
        if dependency in built:
            # If the dependency has already been built
            # within the current DFS path, there's a cycle
            return False
        if adj[dependency] == []:
            # No project depends on the current dependency
            return True

        # Update the built set
        built.add(dependency)

        # Loop over the projects that depend on the current dependency
        for project in adj[dependency]:

            if not dfs(project):
                # If there's a cycle, build error
                return False

        # If there's no cycle for the current DFS path,
        # remove the current project from the built set
        built.remove(dependency)

        # Post-order
        res.append(dependency)

        # Set the current dependency as built,
        # so it's not needed for other projects/dependencies
        adj[dependency] = []

        # If no cycle, return True to continue with the next project
        return True

    for project in range(num_projects):
        if not dfs(project):
            return False

    # Return the inverted resulting list (added in post-order DFS)
    return res[::-1]


def recursion2(num_projects: int, dependencies: list) -> list:
    # DFS - Topsort
    # Time complexity: O(V + E)
    # NOTE: not valid when there're cycles in the graph

    # Build the adjacency list
    adj = [[] for _ in range(num_projects)]
    for dependency, project in dependencies:
        # dependency -> [project1, project2, ...]
        adj[dependency].append(project)

    # Keep track of the projects built
    built = [False] * num_projects

    # Resulting list with the ordering
    ordering = [None] * num_projects

    # Index for ordering the array
    index = num_projects - 1

    def dfs(index, dependency) -> int:
        # DFS recursive function

        # Set the dependency as built
        built[dependency] = True
        # Loop over the projects that depend on the current dependency
        for project in adj[dependency]:
            if not built[project]:
                # If the project hasn't been built,
                # explore it with DFS to see if it's a dependency
                # for other project
                index = dfs(index, project)

        # Add the current dependency to the resulting ordering list
        ordering[index] = dependency

        # Return the next index in the ordering list
        return index - 1

    # Loop over all the projects
    for project in range(num_projects):
        if not built[project]:
            # If the project hasn't been built, explore it
            # with the DFS
            index = dfs(index, project)

    return ordering


def iter_bfs(num_projects: int, dependencies: list) -> list:
    # BSF (Kahn's Algorithm)

    # Build the adjacency list
    adj = [[] for _ in range(num_projects)]
    for dependency, project in dependencies:
        # project -> [dependency1, dependency2, ...]
        # adj[project].append(dependency)
        # dependency -> [project1, project2, ...]
        adj[dependency].append(project)

    # Indegree list tracks the incoming edges to each node (project)
    indegree = [0] * num_projects
    for dependency, project in dependencies:
        indegree[project] += 1

    # Start a queue with the current projects with no incoming edges
    # (indegree = 0)
    queue = deque([p for p in range(num_projects) if indegree[p] == 0])
    # print("adjacency list", adj)
    # print("indegree", indegree)
    # print("queue", list(queue))
    # Resulting order list
    order = [None] * num_projects
    # Start of the index in the resulting list of the current project
    index = 0
    # index = num_projects - 1
    # Loop over until the queue is empty
    while queue:
        # Pop next project, which currently has no incoming edges
        dependency = queue.popleft()
        # Add it to resulting order list
        order[index] = dependency
        # Update the order index for next project
        index += 1

        # Loop over the dependencies of the current project
        for project in adj[dependency]:
            # Since the current dependency has been added to
            # the resulting order list,
            # we can remove it from the "pending" dependencies,
            # so we remove its edge to the current project
            indegree[project] -= 1
            # Check if after removing the edge, the project
            # as no incoming edges
            if indegree[project] == 0:
                # If so, add it to the queue
                queue.append(project)

    # If the current index is not equal to the total number of projects
    if index != num_projects:
        # There's a cycle in the graph
        return False
    # Return the resulting list
    return order


if __name__ == "__main__":
    print("-" * 60)
    print("Build order")
    print("-" * 60)

    test_cases = [
        # ( num_projects, dependencies, solution )
        (2, [[1, 0]], [1, 0]),
        (3, [[0, 1], [1, 2]], [0, 1, 2]),
        (2, [[1, 0], [0, 1]], False),
        (3, [[1, 2], [0, 1]], [0, 1, 2]),
        (3, [[1, 2], [0, 1], [2, 0]], False),
        (4, [[1, 2], [0, 1], [3, 0]], [3, 0, 1, 2]),
        (4, [[1, 2], [0, 1], [1, 0]], False),
        # Multiple solutions !
        (5, [[0, 3], [2, 0], [1, 0], [4, 3]], [1, 2, 4, 0, 3]),
        (6, [(0, 3), (5, 1), (1, 3), (5, 0), (3, 2)], [4, 5, 0, 1, 3, 2]),
        (
            7,
            [[5, 0], [5, 2], [0, 2], [0, 1], [1, 6], [2, 6], [4, 3]],
            [4, 5, 0, 1, 2, 3, 6],
        ),
    ]

    for i, (num_projects, dependencies, solution) in enumerate(test_cases):

        result = recursion(num_projects, dependencies)
        string = f" recursion({dependencies}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\n\tTest: {"OK" if solution == result else "NOT OK"}')

        # detect cycles not implemented in `recursion2`!
        result = recursion2(num_projects, dependencies)
        string = f"recursion2({dependencies}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\n\tTest: {"OK" if solution == result else "NOT OK"}')

        result = iter_bfs(num_projects, dependencies)
        string = f"  iter_bfs({dependencies}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\n\tTest: {"OK" if solution == result else "NOT OK"}')

        if i >= len(test_cases) - 3:
            print("NOTE: problem with non-unique solutions!")

        print()

    # case = 0
    # num_projects = test_cases[case][0]
    # dependencies = test_cases[case][1]
    # print(num_projects, dependencies)
    # print(recursion(num_projects, dependencies))
    # print(recursion2(num_projects, dependencies))
    # print(iter_bfs(num_projects, dependencies))
