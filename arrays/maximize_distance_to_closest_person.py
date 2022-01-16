"""
https://leetcode.com/problems/maximize-distance-to-closest-person/

You are given an array representing a row of seats where 
seats[i] = 1 represents a person sitting in the ith seat, 
and seats[i] = 0 represents that the ith seat is 
empty (0-indexed).

There is at least one empty seat, and at least one 
person sitting.

Alex wants to sit in the seat such that the distance 
between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

Example 1:
Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), 
then the closest person has distance 2.
If Alex sits in any other open seat, the closest 
person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:
Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), 
the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

Example 3:
Input: seats = [0,1]
Output: 1

Constraints:
2 <= seats.length <= 2 * 10^4
seats[i] is 0 or 1.
At least one seat is empty.
At least one seat is occupied.
"""
from typing import List


def two_pass(seats: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    n = len(seats)

    i = 0
    while i < n and not seats[i]:
        i += 1
    first_seated = i

    i = n - 1
    while i > -1 and not seats[i]:
        i -= 1
    last_seated = i

    dist = [0] * n
    for i in range(first_seated + 1, n):
        if not seats[i]:
            dist[i] = dist[i - 1] + 1

    for i in range(last_seated - 1, first_seated, -1):
        if not seats[i]:
            dist[i] = min(dist[i], dist[i + 1] + 1)

    for i in range(first_seated - 1, -1, -1):
        dist[i] = dist[i + 1] + 1

    return max(dist)


def two_pointers(seats: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Use two pointers, `prev` and `curr`, to point to the last
    # indices where there was a 1, so we can measure the
    # distance between two consecutive 1s, i.e.:
    #   1 0 0 0 1 0 0 1
    #   p       c
    #   --> distance = (c + p) // 2 = (4 + 0) // 2 = 2
    #   0 0 0 0 1 0 0 1
    #   p       c
    #   --> distance = c - p = 4 - 0 = 4
    prev = 0
    n = len(seats)
    max_dist = 0
    for curr in range(n):
        if seats[curr]:
            if seats[prev]:
                # If `prev` points to a 1
                max_dist = max(max_dist, (curr - prev) // 2)
            else:
                # If `prev` points to the first element, and
                # this element is a 0
                max_dist = curr - prev
            # Update the pointer `prev` to the current 1
            prev = curr

    # Check if there're empty seats at the end
    if seats[prev]:
        max_dist = max(max_dist, n - 1 - prev)

    return max_dist


def two_pointers2(seats: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    # Optimized

    n = len(seats)
    prev = curr = 0

    # From the start of the array to the first 1
    while not seats[curr]:
        curr += 1
    max_dist = curr - prev
    prev = curr

    # From the first 1 to the end of the array
    for c in range(curr + 1, n):
        if seats[c]:
            curr_dist = (c - prev) // 2
            if curr_dist > max_dist:
                max_dist = curr_dist
            prev = c

    # From the last 1 to the end of the array
    if seats[prev]:
        max_dist = max(max_dist, n - 1 - prev)

    return max_dist


if __name__ == "__main__":
    print("-" * 60)
    print("Maximize distance to closest person")
    print("-" * 60)

    test_cases = [
        ([1, 0], 1),
        ([0, 1], 1),
        ([0, 1, 0, 0], 2),
        ([1, 0, 0, 1], 1),
        ([0, 1, 0, 0, 0, 1], 2),
        ([0, 0, 0, 0, 0, 1, 0, 0, 0, 1], 5),
        ([0, 0, 0, 1, 0, 0, 0, 0], 4),
        ([1, 1, 1, 1, 0, 1, 1, 1], 1),
    ]

    for seats, solution in test_cases:

        print("Seats", seats)

        result = two_pass(seats)
        output = f"       two_pass = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = two_pointers(seats)
        output = f"   two_pointers = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = two_pointers2(seats)
        output = f"  two_pointers2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
