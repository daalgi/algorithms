"""
https://leetcode.com/problems/h-index/

Given an array of integers citations where 
citations[i] is the number of citations a 
researcher received for their ith paper, return 
compute the researcher's h-index.

According to the definition of h-index on Wikipedia: 
A scientist has an index h if h of their n papers 
have at least h citations each, and the other n - h 
papers have no more than h citations each.

If there are several possible values for h, the 
maximum one is taken as the h-index.

Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 
5 papers in total and each of them had received 
3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 
citations each and the remaining two with no more 
than 3 citations each, their h-index is 3.

Example 2:
Input: citations = [1,3,1]
Output: 1

Constraints:
n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""
from typing import List
from copy import deepcopy


def quicksort(citations: List[int]) -> int:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)

    citations.sort()
    n = len(citations)
    for i in range(n):
        if citations[i] >= n - i:
            return n - i

    return 0


def countsort(citations: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    n = len(citations)

    # Array of `n+1` elements where the index `i` indicates
    # the number of citations and the element the number
    # of publications with `i` citations.
    # If an article has `n` or more citations, it can't be
    # the h-index we look for, we can compute it as
    # an `n` citations publication
    counts = [0] * (n + 1)
    for c in citations:
        if c >= n:
            counts[n] += 1
        else:
            counts[c] += 1

    # Loop over the `count` array from the end backwards
    # to find when the number of accumulated publications
    # is at least `i` (current index)
    curr_count = 0
    for i in range(n, -1, -1):
        curr_count += counts[i]
        if curr_count >= i:
            return i

    return 0


if __name__ == "__main__":
    print("-" * 60)
    print("H-index")
    print("-" * 60)

    test_cases = [
        ([1], 1),
        ([0, 8], 1),
        ([0, 8, 9, 10], 3),
        ([1, 2], 1),
        ([1, 2, 2], 2),
        ([1, 3, 1], 1),
        ([1, 2, 8, 8, 9], 3),
        ([3, 0, 6, 1, 5], 3),
        ([1, 2, 5, 8, 8, 8], 4),
    ]

    for citations, solution in test_cases:

        print("Citations:", citations)

        result = quicksort(deepcopy(citations))
        output = f"      quicksort = "
        output += str(result)
        test_ok = solution == result
        output += " " * (45 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = countsort(deepcopy(citations))
        output = f"      countsort = "
        output += str(result)
        test_ok = solution == result
        output += " " * (45 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
