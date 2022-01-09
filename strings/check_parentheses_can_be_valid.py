"""
https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

A parentheses string is a non-empty string consisting only 
of '(' and ')'. It is valid if any of the following 
conditions is true:
- It is ().
- It can be written as AB (A concatenated with B), 
where A and B are valid parentheses strings.
- It can be written as (A), where A is a valid parentheses string.

You are given a parentheses string s and a string locked, 
both of length n. locked is a binary string consisting only 
of '0's and '1's. For each index i of locked,
- If locked[i] is '1', you cannot change s[i].
- But if locked[i] is '0', you can change s[i] to either '(' or ')'.

Return true if you can make s a valid parentheses string. 
Otherwise, return false.

Example 1:
Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', 
so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged 
to make s valid.

Example 2:
Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s 
is already valid.

Example 3:
Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.

Constraints:
n == s.length == locked.length
1 <= n <= 10^5
s[i] is either '(' or ')'.
locked[i] is either '0' or '1'.


Strategy:
https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/discuss/1646594/Left-to-right-and-right-to-left
A useful trick (when doing any parentheses validation) 
is to greedily check balance left-to-right, and then right-to-left.
- Left-to-right check ensures that we do not have orphan ')' parentheses.
- Right-to-left checks for orphan '(' parentheses.

We go left-to-right:
- Count `wild` (not locked) characters.
- Track the balance `bal` for locked parentheses.
    - If the balance goes negative, we check if we have 
    enough `wild` characters to compensate.
- In the end, check that we have enough `wild` characters 
to cover positive balance (open parentheses).

This approach alone, however, will fail for ["))((", "0011"] test case. 
That is why we also need to do the same going right-to-left.

Example:
    string:     ))((
    locked:     0011
        i = 0, wild = 1
        i = 1, wild = 2
        i = 2, wild = 2, bal = 1
        i = 3, wild = 2, bal = 2
    reversed:   ))((
    locked:     1100
        i = 0, wild = 0, bal = -1 --> False    
"""


def two_scans(s: str, locked: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)

    def validate(s: str, locked: str, ref: str) -> bool:
        balance, wild = 0, 0
        for i in range(n):
            if locked[i] == "1":
                balance += 1 if s[i] == ref else -1
            else:
                wild += 1
            if wild + balance < 0:
                return False
        return balance <= wild

    n = len(s)
    return (
        n & 1 == 0 and validate(s, locked, "(") and validate(s[::-1], locked[::-1], ")")
    )


if __name__ == "__main__":
    print("-" * 60)
    print("Check if a parentheses string can be valid")
    print("-" * 60)

    test_cases = [
        # (string, locked, solution)
        (")", "0", False),
        (")()", "000", False),
        ("))", "11", False),
        ("))", "01", True),
        ("()", "01", True),
        ("()()", "0111", True),
        ("))((", "0010", True),
        ("))((", "0011", False),
        ("))()))", "010100", True),
    ]

    for s, locked, solution in test_cases:

        print("String:", s)
        print("Locked:", locked)

        result = two_scans(s, locked)
        output = f"     two_scans = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
