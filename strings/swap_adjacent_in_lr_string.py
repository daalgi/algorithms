"""
https://leetcode.com/problems/swap-adjacent-in-lr-string/

In a string composed of 'L', 'R', and 'X' characters, 
like "RXXLRXRXL", a move consists of either replacing 
one occurrence of "XL" with "LX", or replacing one 
occurrence of "RX" with "XR". Given the starting string 
start and the ending string end, return True if and only 
if there exists a sequence of moves to transform one 
string to the other.

Example 1:
Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

Example 2:
Input: start = "X", end = "L"
Output: false

Constraints:
1 <= start.length <= 10^4
start.length == end.length
Both start and end will only consist of characters in 
'L', 'R', and 'X'.
"""


def two_pointers(start: str, end: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)
    i, j, n = 0, 0, len(start)
    while i < n or j < n:

        # Skip Xs in `start`
        while i < n and start[i] == "X":
            i += 1

        # Skip Xs in `end`
        while j < n and end[j] == "X":
            j += 1

        # Check if reached the end in both strings
        if i == j == n:
            return True

        # Check if only one string reached the end
        if i != j and (i == n or j == n):
            return False

        # Check that both chars are equal
        if start[i] != end[j]:
            return False

        # If "L", the index of `start` must be
        # equal or greater than the index of `end`
        # ("L" can only move backwards in `start`)
        if start[i] == "L" and i < j:
            return False

        # If "R", the index of `start` must be
        # equal or smaller than the index of `end`
        # ("R" can only move forward in `start`)
        if start[i] == "R" and i > j:
            return False

        # Update indices for next iteration
        i += 1
        j += 1


if __name__ == "__main__":
    print("-" * 60)
    print("Swap adjacent in LR string")
    print("-" * 60)

    test_cases = [
        # (start, end, solution)
        ("X", "L", False),
        ("R", "X", False),
        ("R", "L", False),
        ("RXXLRXRXL", "XRLXXRRLX", True),
        ("RXR", "XXR", False),
        ("XXXXXLXXXX", "LXXXXXXXXX", True),
        ("RXXXRXXXLXXXRXXXRXXXRXXXLXXX", "RXXXRXXXLXXXRXXXRXXXRXXXLRXX", False),
        ("RXXXRXXXLXXXRXXXRXXXRXXXLXXX", "RXXXRXXXLXXXRXXXRXXXRXXXLXXX", True),
    ]

    for s1, s2, solution in test_cases:

        print("String 1:", s1)
        print("String 2:", s2)

        result = two_pointers(s1, s2)
        output = f"     two_pointers = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
