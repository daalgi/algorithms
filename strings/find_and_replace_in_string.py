"""
https://leetcode.com/problems/find-and-replace-in-string/

You are given a 0-indexed string s that you must 
perform k replacement operations on. The replacement 
operations are given as three 0-indexed parallel 
arrays, indices, sources, and targets, all of 
length k.

To complete the ith replacement operation:
- Check if the substring sources[i] occurs at index 
indices[i] in the original string s.
- If it does not occur, do nothing.
- Otherwise if it does occur, replace that substring with targets[i].

For example, if s = "abcd", indices[i] = 0, 
sources[i] = "ab", and targets[i] = "eee", 
then the result of this replacement will be "eeecd".

All replacement operations must occur simultaneously, 
meaning the replacement operations should not affect 
the indexing of each other. The testcases will be 
generated such that the replacements will not overlap.

For example, a testcase with s = "abc", indices = [0, 1], 
and sources = ["ab","bc"] will not be generated because 
the "ab" and "bc" replacements overlap.

Return the resulting string after performing all replacement 
operations on s.

A substring is a contiguous sequence of characters in a string.

Example 1:
Input: s = "abcd", indices = [0, 2], 
sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"
Explanation:
"a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".

Example 2:
Input: s = "abcd", indices = [0, 2], 
sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation:
"ab" occurs at index 0 in s, so we replace it with "eee".
"ec" does not occur at index 2 in s, so we do nothing.

Constraints:
1 <= s.length <= 1000
k == indices.length == sources.length == targets.length
1 <= k <= 100
0 <= indexes[i] < s.length
1 <= sources[i].length, targets[i].length <= 50
s consists of only lowercase English letters.
sources[i] and targets[i] consist of only lowercase English letters.
"""
from typing import List


def sorting_one_scan(
    s: str, indices: List[int], sources: List[str], targets: List[str]
) -> str:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)

    # Note: this version handles overlappings
    # (not asked by the original question)

    # Sort the replacements by index, so we can determine
    # in one scan if there're overlappings
    replacements = sorted((i, so, ta) for i, so, ta in zip(indices, sources, targets))

    # Result array
    arr = [c for c in s]

    # Loop over the replacements
    i, n = 0, len(indices)
    while i < n:
        index, source, target = replacements[i]
        size = len(source)

        # Check if there's overlap between the current
        # replacement `i` and  the next `i+1`
        if i < n - 1 and index + size > replacements[i + 1][0]:
            # Skip the current and next replacement
            # due to overlapping
            i += 2
            continue

        # Check if the `source` exists in the string `s`
        # at the expected location
        if s[index : index + size] == source:
            # Replace the character at `index` with `source`
            arr[index] = target

            # If size > 1, remove the remaining chars in the
            # result array `arr`
            start = index
            index += 1
            while index < start + size:
                arr[index] = ""
                index += 1

        # Update index for next iteration
        i += 1

    return "".join(arr)


def sorting_one_scan2(
    s: str, indices: List[int], sources: List[str], targets: List[str]
) -> str:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)

    # Result array
    arr = [c for c in s]

    # Loop over the replacements
    for index, source, target in sorted(zip(indices, sources, targets)):

        size = len(source)

        # Check if the `source` exists in the string `s`
        # at the expected location
        if s[index : index + size] == source:
            # Replace the character at `index` with `source`
            arr[index] = target

            # If size > 1, remove the remaining chars in the
            # result array `arr`
            start = index
            index += 1
            while index < start + size:
                arr[index] = ""
                index += 1

    return "".join(arr)


def sorting_one_scan3(
    s: str, indices: List[int], sources: List[str], targets: List[str]
) -> str:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    for i, so, t in sorted(zip(indices, sources, targets), reverse=True):
        s = s[:i] + t + s[i + len(so) :] if s[i : i + len(so)] == so else s

    return s


if __name__ == "__main__":
    print("-" * 60)
    print("Find and replace in string")
    print("-" * 60)

    test_cases = [
        # (s, indices, sources, targets, solution)
        ("abcd", [0, 2], ["ab", "cd"], ["eeee", "ff"], "eeeeff"),
        ("abcd", [0, 2], ["abc", "cd"], ["eeee", "ff"], "abcd"),
        ("abcd", [0, 2], ["a", "cd"], ["eeee", "ff"], "eeeebff"),
        ("abcd", [0, 2], ["a", "ce"], ["eeee", "ff"], "eeeebcd"),
        ("abcd", [0, 2], ["b", "ce"], ["eeee", "ff"], "abcd"),
    ]

    for s, indices, sources, targets, solution in test_cases:

        print("String:", s)
        print("Indices:", indices)
        print("Sources:", sources)
        print("Targets:", targets)

        result = sorting_one_scan(s, indices, sources, targets)
        output = f"   sorting_one_scan = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        # Solutions not handling overlappings
        # (valid for the orignal question)
        result = sorting_one_scan2(s, indices, sources, targets)
        output = f"  sorting_one_scan2 = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sorting_one_scan3(s, indices, sources, targets)
        output = f"  sorting_one_scan3 = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
