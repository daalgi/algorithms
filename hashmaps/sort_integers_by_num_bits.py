"""
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

You are given an integer array arr. Sort the integers in the array 
in ascending order by the number of 1's in their binary representation 
and in case of two or more integers have the same number of 1's you 
have to sort them in ascending order.

Return the array after sorting it.

Example 1:
Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]

Example 2:
Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explantion: All integers have 1 bit in the binary representation, 
you should just sort them in ascending order.

Constraints:
1 <= arr.length <= 500
0 <= arr[i] <= 10^4
"""
from typing import List


def solution1(arr: List[int]) -> List[int]:
    # Time complexity: O(n)
    # Space complexity: O(n)

    def count_bits(x: int) -> int:
        count = 0
        while x:
            x &= x - 1
            count += 1
        return count

    bits = list()
    for x in arr:
        bits.append((count_bits(x), x))

    return [x[1] for x in sorted(bits)]


def solution2(arr: List[int]) -> List[int]:
    return [x for x in sorted(arr, key=lambda n: (bin(n).count("1"), n))]


if __name__ == "__main__":
    print("-" * 60)
    print("Sort integers by the number of 1 bits")
    print("-" * 60)

    test_cases = [
        ([7, 1, 5], [1, 5, 7]),
        ([25, 13, 86, 93], [13, 25, 86, 93]),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 4, 8, 3, 5, 6, 7]),
        (
            [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],
            [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
        ),
    ]

    for arr, solution in test_cases:

        output = f"Array: {arr}"
        if len(output) > 60:
            output = output[:60] + "...]"
        print(output)

        result = solution1(arr)
        output = f"\tsolution1 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (60 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = solution2(arr)
        output = f"\tsolution2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (60 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
