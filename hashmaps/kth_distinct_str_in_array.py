"""
https://leetcode.com/problems/kth-distinct-string-in-an-array/

A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth 
distinct string present in arr. If there are fewer than k distinct 
strings, return an empty string "".

Note that the strings are considered in the order in which they appear 
in the array.

Example 1:
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 

Example 2:
Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.

Example 3:
Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct 
strings, we return an empty string "".

Constraints:
1 <= k <= arr.length <= 1000
1 <= arr[i].length <= 5
arr[i] consists of lowercase English letters.
"""
from typing import List
from collections import Counter


def solution1(arr: List[str], k) -> str:
    # Time complexity: O(n)
    # Space complexity: O(n)
    count = Counter(arr)
    n = len(arr)
    i = 0
    while k and i < n:
        if count[arr[i]] == 1:
            k -= 1
        i += 1

    return arr[i - 1] if k == 0 else ""


if __name__ == "__main__":
    print("-" * 60)
    print("Kth distinct string in an array")
    print("-" * 60)

    test_cases = [
        # (array, k, solution)
        (["a"], 1, "a"),
        (["a", "a"], 1, ""),
        (["a", "b", "a"], 3, ""),
        (["aaa", "a", "a"], 2, ""),
        (["aaa", "aa", "a"], 1, "aaa"),
        (["d", "b", "c", "b", "c", "a"], 1, "d"),
        (["d", "b", "c", "b", "c", "a"], 2, "a"),
    ]

    for arr, k, solution in test_cases:

        output = f"Array: {arr}"
        if len(output) > 60:
            output = output[:60] + "...]"
        output += f"\n    k: {k}"
        print(output)

        result = solution1(arr, k)
        output = f"\t     solution1 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
