"""
https://leetcode.com/problems/student-attendance-record-i/

You are given a string s representing an attendance 
record for a student where each character signifies 
whether the student was absent, late, or present on 
that day. The record only contains the following 
three characters:
    'A': Absent.
    'L': Late.
    'P': Present.
The student is eligible for an attendance award if 
they meet both of the following criteria:
- The student was absent ('A') for strictly fewer 
than 2 days total.
- The student was never late ('L') for 3 or more 
consecutive days.

Return true if the student is eligible for an attendance 
award, or false otherwise.

Example 1:
Input: s = "PPALLP"
Output: true
Explanation: The student has fewer than 2 absences and 
was never late 3 or more consecutive days.

Example 2:
Input: s = "PPALLL"
Output: false
Explanation: The student was late 3 consecutive days in 
the last 3 days, so is not eligible for the award.

Constraints:
1 <= s.length <= 1000
s[i] is either 'A', 'L', or 'P'.
"""


def one_scan(s: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)

    total_absent, consecutive_late, i, n = 0, 0, 0, len(s)
    while i < n:
        if s[i] == "A":
            total_absent += 1
            if total_absent > 1:
                return False
            consecutive_late = 0
        elif s[i] == "L":
            consecutive_late += 1
            if consecutive_late > 2:
                return False
        else:
            consecutive_late = 0

        i += 1

    return True


def counting(s: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)
    return s.count("A") <= 1 and s.count("LLL") == 0


if __name__ == "__main__":
    print("-" * 60)
    print("Student attendance record I")
    print("-" * 60)

    test_cases = [
        ("PPALLP", True),
        ("PPALLL", False),
        ("ALL", True),
        ("ALLPPPPPPPAPPP", False),
    ]

    for s, solution in test_cases:

        print("Attendance record:", s)

        result = one_scan(s)
        output = f"     one_scan = "
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = counting(s)
        output = f"     counting = "
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
