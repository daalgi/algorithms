"""
https://leetcode.com/problems/number-of-1-bits/

Write a function that takes an unsigned integer and returns 
the number of '1' bits it has (also known as the Hamming weight).

Note:
Note that in some languages, such as Java, there is no 
unsigned integer type. In this case, the input will be 
given as a signed integer type. It should not affect your 
implementation, as the integer's internal binary 
representation is the same, whether it is signed or unsigned.

In Java, the compiler represents the signed integers 
using 2's complement notation. Therefore, in Example 3, 
the input represents the signed integer. -3.

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Constraints:
The input must be a binary string of length 32.

Follow up: If this function is called many times, how would you optimize it?
"""


def brute_force(num: int) -> int:
    # Check bit by bit, and if it's a `1`, 
    # add it to the count
    count = 0
    while num > 0:
        if num & 1 == 1:
            count += 1
        num >>= 1
    return count

def optimal(num: int) -> int:
    # Remove the rightmost set bit
    # Example: n & (n - 1) = 11110 & 11101 = 11100
    # This way, the number of iterations is exactly equal
    # to the number of 1s in the binary representation of `num`
    count = 0
    while num:
        num &= num - 1
        count += 1
    return count

if __name__ == "__main__":
    print("-" * 60)
    print("Number of 1 bits")
    print("-" * 60)

    test_cases = [
        (1, 1),  # 1
        (2, 1),  # 10
        (3, 2),  # 11
        (4, 1),  # 100
        (5, 2),  # 101
        (6, 2),  # 110
        (7, 3),  # 111
    ]

    for num, solution in test_cases:

        string = f"brute_force({num}) = "
        string += " " * (35 - len(string))
        result = brute_force(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
        
        string = f"    optimal({num}) = "
        string += " " * (35 - len(string))
        result = optimal(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
