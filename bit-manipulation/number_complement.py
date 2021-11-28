"""
https://leetcode.com/problems/number-complement/

The complement of an integer is the integer you get when 
you flip all the 0's to 1's and all the 1's to 0's in its 
binary representation.

For example, The integer 5 is "101" in binary and its 
complement is "010" which is the integer 2.
Given an integer num, return its complement.

Example 1:
Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 
(no leading zero bits), and its complement is 010. 
So you need to output 2.

Example 2:
Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 
(no leading zero bits), and its complement is 0. 
So you need to output 0.

Constraints:
1 <= num < 2^31
"""


def complement(n: int) -> int:
    # XOR with a mask with 1s only at the set bits of `n`.
    # You can find the length of the magnitude of the binary
    # representation of an integer with (len(n) - 2)
    mask = (1 << (len(bin(n)) - 2)) - 1
    return n ^ mask


if __name__ == "__main__":
    print("-" * 60)
    print("Number complement")
    print("-" * 60)

    test_cases = [
        (1, 0),
        (2, 1),
        (3, 0),
        (4, 3),
        (5, 2),
        (6, 1),
        (7, 0),
        (50, 13),
        (88498498, 45719229),
    ]

    for n, solution in test_cases:
        string = f"complement({n}) = "
        string += " " * (25 - len(string))
        result = complement(n)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
