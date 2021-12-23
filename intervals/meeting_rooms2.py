"""
https://www.lintcode.com/problem/919/


Given an array of meeting time intervals consisting of start and 
end times [[s1,e1],[s2,e2],…] (si < ei), find the minimum number 
of conference rooms required.

Example 1:
Input: meetings = [[0, 30],[5, 10],[15, 20]]
Output: 2
Two meeting rooms needed:
- Meeting room 1: [0, 30]
- Meeting room 2: [5, 10], [15, 20]

Example 2:
Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
"""
from typing import List
from copy import deepcopy
import heapq


def heap(meetings: List[List[int]]) -> int:
    # Time complexity: O()
    # Space complexity: O(n)

    # Sort meetings by starting time
    # O(nlogn)
    meetings.sort()

    # Maximum number of needed `rooms`
    max_rooms = 1
    # Heap to keep track of the ongoing meetings and their ending time
    ongoing = []
    for meeting in meetings:
        if not ongoing:
            # Add ending time to the `ongoing` heap
            heapq.heappush(ongoing, meeting[1])
        elif ongoing[0] > meeting[0]:
            # If the current meeting start conflicts with
            # the earliest ending in the `ongoing` heap,
            # add the current meeting to the `ongoing` heap
            heapq.heappush(ongoing, meeting[1])
        else:
            # If the current meeting starts after the ending
            # of the earliest `ongoing` meeting,
            # pop all the non-overlapping meetings from the heap
            while ongoing and ongoing[0] <= meeting[0]:
                heapq.heappop(ongoing)
            # Add the current meeting to the heap
            heapq.heappush(ongoing, meeting[1])

        # Check the current needed rooms
        if max_rooms < len(ongoing):
            max_rooms = len(ongoing)

    return max_rooms


if __name__ == "__main__":
    print("-" * 60)
    print("Meeting rooms II")
    print("-" * 60)

    test_cases = [
        ([[1, 2]], 1),
        ([[1, 2], [2, 3]], 1),
        ([[1, 2], [1, 5], [1, 5]], 3),
        ([[1, 2], [3, 5], [2, 5], [1, 5]], 3),
        ([[1, 2], [3, 5], [7, 8], [2, 5], [6, 7]], 2),
        ([[1, 2], [2, 4], [5, 8], [9, 13]], 1),
        ([[1, 2], [2, 9], [3, 4], [0, 1]], 2),
        (
            [
                (65, 424),
                (351, 507),
                (314, 807),
                (387, 722),
                (19, 797),
                (259, 722),
                (165, 221),
                (136, 897),
            ],
            7,
        ),
    ]

    for meetings, solution in test_cases:

        output = f"Meetings: {meetings}"
        if len(output) > 60:
            output = output[:60] + " ...]]"
        print(output)

        result = heap(deepcopy(meetings))
        output = f"\t   heap = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
