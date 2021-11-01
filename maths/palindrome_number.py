"""
https://leetcode.com/problems/palindrome-number/solution/
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward 
as forward. For example, 121 is palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false

Constraints:
-231 <= x <= 231 - 1
 
Follow up: Could you solve it without converting the integer to a string?
"""


def converting_to_string(num: int) -> bool:
    # Base case
    if num < 0:
        return False
    if num < 10:
        return True
    if num % 10 == 0:
        return False

    # Convert integer to a string
    s = str(num)
    # Two pointers
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def not_converting_to_string(num: int) -> bool:
    # Time complexity: O(log10(n))
    # Space complexity: O(1)
    # Base cases
    if num < 0 or (num % 10 == 0 and num != 0):
        return False
    if num < 10:
        return True

    # Loop over the digits of the integer.
    # To avoid possible integer overflow, we compare only half
    # of the digits.
    # The iterative process should stop when we reach the half
    # of the number, that is, num <= reversed_num
    # i.e. in "1221"
    #   reverted last half digits = "12"
    #           first half digits = "12"
    reversed_num = 0
    while num > reversed_num:
        # Add the last digit of `num` (212 % 10 = 2)
        # to the end of the `reversed_num`
        # i.e. num = 212
        # iter 1: reversed_num = 0 * 10 + 212 % 10 =  0 + 2 =  2
        # iter 2: reversed_num = 2 * 10 +  21 % 10 = 20 + 1 = 21
        reversed_num = reversed_num * 10 + num % 10
        # Remove the last digit of `num`
        num //= 10

    return reversed_num == num or reversed_num // 10 == num


if __name__ == "__main__":
    print("-" * 60)
    print("Is number Palindrome?")
    print("-" * 60)

    test_cases = [
        (0, True),
        (1, True),
        (-1, False),
        (10, False),
        (20, False),
        (80, False),
        (101, True),
        (10101, True),
        (101102, False),
    ]

    for num, solution in test_cases:

        result = converting_to_string(num)
        string = f"    converting_to_string({num}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = not_converting_to_string(num)
        string = f"not_converting_to_string({num}) = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
