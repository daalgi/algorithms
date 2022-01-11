"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number 
could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone 
buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List
from collections import Counter


def digit_letters_dict():
    # Build a hashtable with the letters assigned to each key:
    # { "2": ["a", "b", "c"], "3": [...], ... }
    keys = {}
    curr_letter = ord("a")
    for digit in range(2, 10):
        num_letters = 4 if digit == 7 or digit == 9 else 3
        keys[str(digit)] = []
        for _ in range(num_letters):
            keys[str(digit)].append(chr(curr_letter))
            curr_letter += 1
    return keys


def backtracking_iterative(digits: str) -> List[str]:
    # Time complexity: O(3^n)
    # Space complexity: O(3^n)
    # Backtracking iterative algorithm to find all
    # possible combinations

    if not digits:
        return []

    # No need to use a dictionary, we can simply use a list
    # keys = digit_letters_dict()
    keys = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    res = [""]
    for digit in digits:
        res = [r + l for r in res for l in keys[int(digit)]]
    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Letter combinations of a phone number")
    print("-" * 60)

    test_cases = [
        # (digits, solution)
        ("", []),
        ("2", ["a", "b", "c"]),
        ("9", ["w", "x", "y", "z"]),
        (
            "29",
            ["aw", "ax", "ay", "az", "bw", "bx", "by", "bz", "cw", "cx", "cy", "cz"],
        ),
        ("3838", None),
    ]

    for digits, solution in test_cases:

        print("Digits:", digits)

        result = backtracking_iterative(digits)
        output = f"     iterative = "
        output += " " * (10 - len(output))
        output += str(result)
        if solution:
            test_ok = solution == result
            output += "\n" + " " * 55
            output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
