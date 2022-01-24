"""
https://leetcode.com/problems/detect-capital/

We define the usage of capitals in a word to be 
right when one of the following cases holds:
- All letters in this word are capitals, like "USA".
- All letters in this word are not capitals, like "leetcode".
- Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of 
capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false

Constraints:
1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
"""


def count_capitals(word: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)
    num_capital_letters = sum(ord(c) < ord("a") for c in word)
    n = len(word)
    if num_capital_letters == n or num_capital_letters == 0:
        return True
    if num_capital_letters == 1:
        return ord(word[0]) < ord("a")
    return False


def count_capitals2(word: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)
    # Use python built-in methods (slower)
    num_capital_letters = sum(c.isupper() for c in word)
    n = len(word)
    if num_capital_letters == n or num_capital_letters == 0:
        return True
    if num_capital_letters == 1:
        return word[0].isupper()
    return False


def python_methods(word: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)
    # Use python built-in methods (even slower)
    return word.isupper() or word.islower() or word.istitle()


if __name__ == "__main__":
    print("-" * 60)
    print("Detect capital")
    print("-" * 60)

    test_cases = [
        ("USA", True),
        ("Google", True),
        ("GooGlE", False),
        ("leetcode", True),
        ("leetCode", False),
        ("ALGORITHm", False),
    ]

    for word, solution in test_cases:

        print("Word:", word)

        result = count_capitals(word)
        output = f"     count_capitals = "
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = count_capitals2(word)
        output = f"    count_capitals2 = "
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = python_methods(word)
        output = f"     python_methods = "
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
