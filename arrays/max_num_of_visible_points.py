"""
https://leetcode.com/problems/maximum-number-of-visible-points/

You are given an array points, an integer angle, and your 
location, where location = [posx, posy] and points[i] = [xi, yi] 
both denote integral coordinates on the X-Y plane.

Initially, you are facing directly east from your position. 
You cannot move from your position, but you can rotate. In other 
words, posx and posy cannot be changed. Your field of view in 
degrees is represented by angle, determining how wide you can 
see from any given view direction. Let d be the amount in degrees 
that you rotate counterclockwise. Then, your field of view is the 
inclusive range of angles [d - angle/2, d + angle/2].

You can see some set of points if, for each point, the angle formed 
by the point, your position, and the immediate east direction from 
your position is in your field of view.

There can be multiple points at one coordinate. There may be points 
at your location, and you can always see these points regardless of 
your rotation. Points do not obstruct your vision to other points.

Return the maximum number of points you can see.

Example 1:

Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
Output: 3
Explanation: The shaded region represents your field of view. 
All points can be made visible in your field of view, 
including [3,3] even though [2,2] is in front and in the same 
line of sight.

Example 2:
Input: points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
Output: 4
Explanation: All points can be made visible in your 
field of view, including the one at your location.

Example 3:
Input: points = [[1,0],[2,1]], angle = 13, location = [1,1]
Output: 1
Explanation: You can only see one of the two points, as shown above.

Constraints:
1 <= points.length <= 10^5
points[i].length == 2
location.length == 2
0 <= angle < 360
0 <= posx, posy, xi, yi <= 100
"""
from typing import List
from copy import deepcopy
from math import atan2, pi


def sliding_window(points: List[List[int]], angle: int, location: List[int]) -> int:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)

    def angle_from_location(point: List[int]):
        # Change system origin and convert to polar coordinates
        # Change origin
        point[0] -= location[0]
        point[1] -= location[1]

        # Change cartesian to polar system (only angle)
        ang = atan2(point[1], point[0]) * 180 / pi

        # Return angle converted into
        # counter-clockwise 0 to 360 deg angle
        return ang if ang >= 0 else ang + 360

    # Remove points at `location`, which are always visible
    initial_points = len(points)
    points = [p for p in points if p != location]
    points_at_location = initial_points - len(points)
    if not points:
        # If all the points are at `location`
        return points_at_location

    # Calculate the angle between `location` and each point,
    # and sort them
    angles = sorted(angle_from_location(p) for p in points)

    # Duplicate `points` to handle the circular array
    angles += [a + 360 for a in angles]
    n = len(angles)

    # Use two pointers to keep track of the angles between
    # a set of points
    max_visible = 0
    start = end = 0
    while end < n:
        
        # Move `end` pointer
        while end < n and angles[end] - angles[start] <= angle:
            end += 1

        # Current visible points = `end - start`
        max_visible = max(end - start, max_visible)

        # Move `start` pointer
        while end < n and start < end and angles[end] - angles[start] > angle:
            start += 1

    return points_at_location + max_visible


if __name__ == "__main__":
    print("-" * 60)
    print("Maximum number of visible points")
    print("-" * 60)

    test_cases = [
        # (points, angle, location, solution)
        (
            [[2, 1], [2, 2], [1, 2], [0, 2], [0, 1], [0, 0], [1, 0], [2, 0]],
            90,
            [1, 1],
            3,
        ),
        ([[2, 1], [2, 2], [3, 3]], 90, [1, 1], 3),
        ([[2, 1], [2, 2], [3, 4], [1, 1]], 90, [1, 1], 4),
        ([[1, 0], [2, 1]], 13, [1, 1], 1),
    ]

    for points, angle, location, solution in test_cases:

        print("Points:", points)
        print("Angle:", angle)
        print("Location:", location)

        result = sliding_window(deepcopy(points), angle, location)
        output = "    sliding_window = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
