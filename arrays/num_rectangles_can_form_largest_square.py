"""
https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

You are given an array rectangles where 
rectangles[i] = [li, wi] represents the ith rectangle 
of length li and width wi.

You can cut the ith rectangle to form a square with 
a side length of k if both k <= li and k <= wi. 
For example, if you have a rectangle [4,6], you can 
cut it to get a square with a side length of at most 4.

Let maxLen be the side length of the largest square 
you can obtain from any of the given rectangles.

Return the number of rectangles that can make a square 
with a side length of maxLen.

Example 1:
Input: rectangles = [[5,8],[3,9],[5,12],[16,5]]
Output: 3
Explanation: The largest squares you can get from each 
rectangle are of lengths [5,3,5,5].
The largest possible square is of length 5, and you 
can get it out of 3 rectangles.

Example 2:
Input: rectangles = [[2,3],[3,7],[4,3],[3,7]]
Output: 3

Constraints:
1 <= rectangles.length <= 1000
rectangles[i].length == 2
1 <= li, wi <= 10^9
li != wi
"""
from typing import List


def two_passes(rectangles: List[List[int]]) -> int:
    # Time complexity: O(2n) = O(n)
    # Space complexity: O(1)

    max_len = curr_len = 0
    for rect in rectangles:
        curr_len = min(rect)
        if curr_len > max_len:
            max_len = curr_len

    count = 0
    for rect in rectangles:
        if min(rect) >= max_len:
            count += 1

    return count


def one_pass(rectangles: List[List[int]]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)

    max_len = curr_len = count = 0
    for rect in rectangles:
        curr_len = min(rect)
        if curr_len > max_len:
            max_len = curr_len
            count = 1
        elif curr_len == max_len:
            count += 1

    return count


if __name__ == "__main__":
    print("-" * 60)
    print("Number of rectangles that can form the largest square")
    print("-" * 60)

    test_cases = [
        # (rectangles, solution)
        ([[5, 8], [3, 9], [5, 12], [16, 5]], 3),
        ([[2, 3], [3, 7], [4, 3], [3, 7]], 3),
        ([[2, 3], [3, 7], [4, 3], [4, 7]], 1),
    ]

    for rectangles, solution in test_cases:

        print("Rectangles:", rectangles)

        result = two_passes(rectangles)
        output = "    two_passes = "
        print_result = str(result)
        output += print_result
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = one_pass(rectangles)
        output = "      one_pass = "
        print_result = str(result)
        output += print_result
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
