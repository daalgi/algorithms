"""
CRACKING THE CODING INTERVIEW
8.9 Parens:
Implement an algorithm to print all valid (i.e., properly opened
and closed) combinations of n pairs of parentheses.

Example:
Input: 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]


https://leetcode.com/problems/generate-parentheses/
"""
from typing import List


def brute_force(n: int) -> List[str]:
    # Brute force: create all possible sequences and validate them.

    # Time complexity: O(n * 2^(2*n))
    # Create 2^(2n) possibilities.
    # Create and validate the sequence takes O(n)
    # Space complexity: O(n * 2^(2*n))

    str_len = 2 * n
    res = []

    def is_valid(comb: list):
        balance = 0
        for c in comb:
            if c == "(":
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    def generate(comb: list):
        if len(comb) == str_len:
            if is_valid(comb):
                res.append("".join(comb))
        else:
            comb.append("(")
            generate(comb)
            comb.pop()

            comb.append(")")
            generate(comb)
            comb.pop()

    generate([])
    return res


def backtrack(n: int) -> List[str]:
    # Time complexity: O(4^n / sqrt(n))
    # Space complexity: O(4^n / sqrt(n))
    res = []
    str_len = 2 * n

    def _backtrack(comb: list, open: int, closed: int) -> None:
        # Recursive function - Backtrack
        # `comb` is the current combination
        # `open` represents the remaining open parentheses
        # `closed` represents the remaining closed parentheses

        # Base case
        if len(comb) == str_len:
            # Make a string copy of the current combination
            res.append("".join(comb))
            return

        # New candidate:
        if open > 0:
            # If there're open parentheses remaining,
            # add an open parenthesis to the current combination
            comb.append("(")
            # Given the candidate, explore further
            _backtrack(comb, open - 1, closed)
            # Backtrack: revert the last choice
            comb.pop()

        if closed > open:
            # If there're more closed parentheses than open,
            # add a closed parenthesis to the current combination
            comb.append(")")
            # Given the candidate, explore further
            _backtrack(comb, open, closed - 1)
            # Backtrack: revert the last choice
            comb.pop()

    _backtrack([], n, n)
    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Parens")
    print("-" * 60)

    test_cases = [
        (0, [""]),
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    ]

    for n, solution in test_cases:

        solution = sorted(solution)

        print(f">>> brute_force({n})")
        result = brute_force(n)
        result = sorted(result)
        string = str(result)
        if len(string) > 60:
            string = string[:60] + "...]"
        print(string)
        test_ok = solution == result
        print(" " * 60, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')

        print(f">>> backtrack({n})")
        result = backtrack(n)
        result = sorted(result)
        string = str(result)
        if len(string) > 60:
            string = string[:60] + "...]"
        print(string)
        test_ok = solution == result
        print(" " * 60, f'\t\tTest: {"OK" if test_ok else "NOT OK"}')
