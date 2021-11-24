"""
https://leetcode.com/problems/reverse-bits/

Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no 
unsigned integer type. In this case, both input and output 
will be given as a signed integer type. They should not 
affect your implementation, as the integer's internal 
binary representation is the same, whether it is signed or 
unsigned.
In Java, the compiler represents the signed integers 
using 2's complement notation. Therefore, in Example 2 above, 
the input represents the signed integer -3 and the output 
represents the signed integer -1073741825.

Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

Constraints:
The input must be a binary string of length 32
"""


def reverse(num: int) -> int:
    # Time complexity is O(32)
    # Space complexity is O(1)
    res = 0
    bits = 0
    while num:
        res = (res << 1) | (num & 1)
        num >>= 1
        bits += 1

    while bits < 32:
        res <<= 1
        bits += 1

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Reverse bits")
    print("-" * 60)

    test_cases = [
        # (00000000000000000000000000000010,
        #  01000000000000000000000000000000)
        (2, 1073741824),
        # (00000000000000000000000000000101,
        #  10100000000000000000000000000000)
        (5, 2684354560),
        # (00000000000000000000000000001100,
        #  00110000000000000000000000000000)
        (12, 805306368),
        # (00000010100101000001111010011100,
        #  00111001011110000010100101000000)
        (43261596, 964176192),
        # (11111111111111111111111111111101,
        # 10111111111111111111111111111111)
        (4294967293, 3221225471),
    ]

    for num, solution in test_cases:

        string = f"reverse({num}) = "
        string += " " * (35 - len(string))
        result = reverse(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
        # print(bin(result))
