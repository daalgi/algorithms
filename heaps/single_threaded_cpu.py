"""
https://leetcode.com/problems/single-threaded-cpu/

You are given n tasks labeled from 0 to n - 1 represented 
by a 2D integer array tasks, where 
tasks[i] = [enqueueTimei, processingTimei] means that the ith
task will be available to process at enqueueTimei and will 
take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one 
task at a time and will act in the following way:
- If the CPU is idle and there are no available tasks to process, 
the CPU remains idle.
- If the CPU is idle and there are available tasks, 
the CPU will choose the one with the shortest processing time. 
If multiple tasks have the same shortest processing time, 
it will choose the task with the smallest index.
- Once a task is started, the CPU will process the entire 
task without stopping.
- The CPU can finish a task then start a new one instantly.

Return the order in which the CPU will process the tasks.

Example 1:
Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows: 
- At time = 1, task 0 is available to process. 
Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. 
Available tasks = {}.
- At time = 2, task 1 is available to process. 
Available tasks = {1}.
- At time = 3, task 2 is available to process. 
Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts 
processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. 
Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing 
task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing 
task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.
Example 2:

Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]
Explanation: The events go as follows:
- At time = 7, all the tasks become available. 
Available tasks = {0,1,2,3,4}.
- Also at time = 7, the idle CPU starts processing task 4. 
Available tasks = {0,1,2,3}.
- At time = 9, the CPU finishes task 4 and starts processing 
task 3. Available tasks = {0,1,2}.
- At time = 13, the CPU finishes task 3 and starts processing 
task 2. Available tasks = {0,1}.
- At time = 18, the CPU finishes task 2 and starts processing 
task 0. Available tasks = {1}.
- At time = 28, the CPU finishes task 0 and starts processing 
task 1. Available tasks = {}.
- At time = 40, the CPU finishes task 1 and becomes idle.

Constraints:
tasks.length == n
1 <= n <= 10^5
1 <= enqueueTimei, processingTimei <= 10^9
"""
from copy import deepcopy
from typing import List
import heapq


def sort_heap(tasks: List[List[int]]) -> List[int]:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)

    n = len(tasks)
    # Sort the tasks by `start`, `duration`, `index`
    # Note: for much faster runtimes, avoid `*` to spread a list
    # tasks = sorted([(*tasks[i], i) for i in range(n)])
    tasks = sorted([(tasks[i][0], tasks[i][1], i) for i in range(n)])

    # Time pointers
    time, curr_task_end, last_task_start = tasks[0][0], 0, tasks[-1][0]
    # Current task pointer
    task_index = 0
    # Result list
    order = []
    # Min-heap (duration, task_index)
    heap = []
    # Loop until there are no tasks left coming later
    # and no tasks left in the heap
    while time <= last_task_start or heap:

        # Add the new tasks at the current time to the heap
        while task_index < n and time >= tasks[task_index][0]:
            task = tasks[task_index]
            heapq.heappush(heap, (task[1], task[2]))
            task_index += 1

        # If the CPU is idle and there are tasks waiting
        # in the heap, process the next task
        if heap and time >= curr_task_end:
            task = heapq.heappop(heap)
            curr_task_end = time + task[0]
            order.append(task[1])

        # Update the `time` for next iteration
        if task_index > n - 1:
            time = curr_task_end
        else:
            if not heap:
                time = tasks[task_index][0]
            else:
                time = min(tasks[task_index][0], curr_task_end)

    return order


def sort_heap2(tasks: List[List[int]]) -> List[int]:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    # Note: it seems more optimized than the previous algorithm,
    # but the runtime is much slower in Leetcode

    n = len(tasks)
    # Sort the tasks by `start`, `duration`, `index`
    tasks = sorted([(tasks[i][0], tasks[i][1], i) for i in range(n)])
    # Time and task pointers
    time, task_index = tasks[0][0], 0
    # Result list
    order = []
    # min-heap to keep the shortest tasks at the top
    heap = []
    # Loop until the length of the list `order` is completely filled
    while len(order) < n:

        # Check the tasks started up until the current `time`
        while task_index < n and time >= tasks[task_index][0]:
            heapq.heappush(heap, (tasks[task_index][1], tasks[task_index][2]))
            task_index += 1

        # Update time for next iteration
        if heap:
            # If there're tasks in the heap,
            # add the one at the top to the `order` list
            task = heapq.heappop(heap)
            order.append(task[1])
            time += task[0]
            # Note: this works because whenever there's a task
            # in the `heap`, we update the time for next iter
            # to the end of that task, and then all the new
            # tasks during the new and prev times will be added
            # at once at the beginning of the loop,
            # so there's no need to take care of the
            # `curr_task_end` variable as in the previous algorithm

        else:
            # If there's no task in the `heap`,
            # forward the `time` until the start of the
            # next task
            time = tasks[task_index][0]

    return order


if __name__ == "__main__":
    print("-" * 60)
    print("Single-threaded CPU")
    print("-" * 60)

    test_cases = [
        # (tasks, solution)
        ([[1, 8]], [0]),
        ([[1, 8], [3, 10], [5, 2]], [0, 2, 1]),
        ([[7, 1], [6, 3], [1, 3]], [2, 1, 0]),
        ([[0, 2], [1, 4], [2, 1], [3, 2]], [0, 2, 3, 1]),
        ([[1, 2], [2, 4], [3, 2], [4, 1]], [0, 2, 3, 1]),
        ([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]], [4, 3, 2, 0, 1]),
        (
            [
                [7, 10],
                [7, 12],
                [7, 5],
                [7, 4],
                [7, 2],
                [9900, 200],
                [9998, 100],
                [9999, 99],
            ],
            [4, 3, 2, 0, 1, 5, 7, 6],
        ),
    ]

    for tasks, solution in test_cases:

        print(f"Tasks: {tasks}")

        result = sort_heap(deepcopy(tasks))
        output = f"        sort_heap = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sort_heap2(deepcopy(tasks))
        output = f"       sort_heap2 = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
