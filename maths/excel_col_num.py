"""
https://leetcode.com/problems/excel-sheet-column-number/

Given a string columnTitle that represents the column 
title as appear in an Excel sheet, return its 
corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 
Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701

Constraints:
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""


def base_conversion(col: str) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    # Strategy: number conversion between different bases
    # - Hexadecimal to Decimal:
    #     (651)_16 = (6 * 16²) + (5 * 16¹) + (1 * 16⁰) = (1617)_10
    # - In general, base to decimal:
    #     (abcd)_base = (a * base³) + (b * base²) + (c * base¹) + (d * base⁰)
    num_letters = ord("Z") - ord("A") + 1
    origin = ord("A") - 1
    n = len(col)
    num = 0
    for i in range(n):
        num += (ord(col[i]) - origin) * num_letters ** (n - i - 1)
    return num


def base_conversion2(col: str) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Faster on leetcode
    num_letters = ord("Z") - ord("A") + 1
    origin = ord("A") - 1
    n = len(col)
    return sum(
        (ord(c) - origin) * num_letters ** (n - i - 1) for i, c in enumerate(col)
    )


if __name__ == "__main__":
    print("-" * 60)
    print("Sqrt(x)")
    print("-" * 60)

    test_cases = [
        ("A", 1),
        ("B", 2),
        ("Z", 26),
        ("AA", 27),
        ("MA", 339),
        ("DAG", 2737),
        ("YURI", 454073),
        ("ZYXASD", 320763174),
    ]

    for col, solution in test_cases:

        print("Col:", col)

        result = base_conversion(col)
        output = f"     base_conversion = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = base_conversion2(col)
        output = f"    base_conversion2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
