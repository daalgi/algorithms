"""
https://leetcode.com/problems/course-schedule-iii/

There are n different online courses numbered from 1 to n. 
You are given an array courses where courses[i] = [durationi, lastDayi] 
indicate that the ith course should be taken continuously for 
durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses 
simultaneously.

Return the maximum number of courses that you can take.

Example 1:
Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation: 
There are totally 4 courses, but you can take 3 courses at most:
- First, take the 1st course, it costs 100 days so you will finish it 
on the 100th day, and ready to take the next course on the 101st day.
- Second, take the 3rd course, it costs 1000 days so you will finish it 
on the 1100th day, and ready to take the next course on the 1101st day. 
- Third, take the 2nd course, it costs 200 days so you will finish it on 
the 1300th day. 
- The 4th course cannot be taken now, since you will finish it on the 
3300th day, which exceeds the closed date.

Example 2:
Input: courses = [[1,2]]
Output: 1

Example 3:
Input: courses = [[3,2],[4,3]]
Output: 0

Constraints:
1 <= courses.length <= 10^4
1 <= durationi, lastDayi <= 10^4
"""
from typing import List
import heapq
from copy import deepcopy


def brute_force(courses: List[List[int]]) -> int:
    # Time complexity: O((n+1)!)
    # Space complexity: O(n)
    # There are n! permutations. For every permutation, we can scan
    # over the `n` elements of the permutation to find the number
    # of courses that can be taken in each case.
    # Each permutation needs `n` space.
    pass


def dp_memoization(courses: List[List[int]]) -> int:
    # Time complexity: O(nd)
    # Space complexity: O(nd)
    # where `n` is the number of courses, and
    # `d` refers to the max value of the end day from
    # all the end days in the `courses` list.

    def dfs(last_ending: int, course: int) -> int:
        # Base case
        if course == n:
            # Reached the end of the list of courses
            return 0

        if last_ending > courses[course][1] - courses[course][0]:
            # The ending of the last course taken
            # overlaps with the current course,
            # so can't take it. Explore next courses.
            return dfs(last_ending, course + 1)

        return max(
            # Option 1: take the current course (+1),
            # and explore next courses
            1 + dfs(last_ending + courses[course][0], course + 1),
            # Option 2: don't take the current course,
            # and explore the next courses
            dfs(last_ending, course + 1),
        )

    n = len(courses)
    # Sort the courses by `last_day`, where course_i = [duration, last_day]
    courses = sorted(courses, key=lambda c: c[1])
    
    # Call the recursive function from a previous
    # last_day equal to 0, from the course number 0
    return dfs(0, 0)


def dp_tabulation(courses: List[List[int]]) -> int:
    pass


def heap(courses: List[List[int]]) -> int:
    # Time complexity: O()
    # Space complexity: O()

    # Sort the courses by the `last_day`
    courses.sort(key=lambda c: c[1])

    # Build a heap.
    # Strategy: if the current course can't be taken directly,
    # we need to find a course whose duration is maximum from
    # amongst the courses taken until now. Then, we remove 
    # the max duration and add the current course's duration.
    # At the end, the length of the heap represents the maximum
    # number of course that can be taken.
    heap = []
    time = 0
    for duration, last_day in courses:
        # Push to the min-heap with the sign changed,
        # to effectively have a max-heap
        heapq.heappush(heap, -duration)

        time += duration
        if time > last_day:
            # If `time` after adding the current course
            # exceeds the current course `last_day`,
            # we remove the longest course from the heap,
            # and since we're handling a min-heap as a max-heap,
            # we need to change the sign of the popped element
            # time -= longest_duration = -heappop()
            time += heapq.heappop(heap)

    return len(heap)


if __name__ == "__main__":
    print("-" * 60)
    print("Course schedule III")
    print("-" * 60)

    test_cases = [
        # (courses, solution)
        # courses = [course1, course2, ...]
        # course1 = [duration, last_day]
        ([[1, 2]], 1),
        ([[3, 2]], 0),
        ([[3, 2], [4, 3]], 0),
        ([[1, 3], [2, 3]], 2),
        ([[1, 2], [1, 3], [1, 4]], 3),
        ([[1, 2], [1, 3], [2, 4]], 3),
        ([[1, 2], [3, 3], [3, 4]], 2),
        ([[1, 2], [1, 3], [5, 8], [1, 4], [2, 10], [3, 3]], 5),
        ([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3),
        ([[2, x] for x in range(50000)], 24999),
    ]

    for courses, solution in test_cases:

        output = f"Courses: {courses}"
        if len(output) > 50:
            output = output[:60] + " ...], ...]"
        print(output)

        if len(courses) < 50:
            result = dp_memoization(deepcopy(courses))
            output = f"\t  dp_memoization = "
            output += " " * (25 - len(output))
            output += str(result)
            output += " " * (60 - len(output))
            test_ok = solution == result
            output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
            print(output)

        result = heap(deepcopy(courses))
        output = f"\t            heap = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
