"""
https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots 
are planted, and some are not. However, flowers 
cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an 
integer n, return if n new flowers can be planted 
in the flowerbed without violating the 
no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:
1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
from typing import List


def one_scan(flowerbed: List[int], n: int) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)

    size = len(flowerbed)

    # From the start to the first 1
    index = 0
    while index < size and flowerbed[index] == 0:
        index += 1

    # 0 0 0 1 --> count = 3 // 2
    n -= index // 2

    # If reached the end of the array without 1s
    if index == size:
        if index & 1:
            # Handle the case of even number of elements
            # (odd index)
            n -= 1
        return n < 1

    # From the first 1 to the last one
    zeros_count = 0
    for i in range(index, size):
        if flowerbed[i]:
            if zeros_count:
                n -= (zeros_count - 1) // 2
            zeros_count = 0
        else:
            zeros_count += 1

    # From the last 1 to the end of the array
    n -= zeros_count // 2

    return n < 1


def one_scan2(flowerbed: List[int], n: int) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Note: this algorithm takes into account that
    # by default the array must be valid, that is,
    # it can have two adjacent flowers: [0, 1, 1, 0] -> invalid!

    count = prev = 0
    for curr in flowerbed:
        if curr:
            if prev == 1:
                # Last added flower was invalid,
                # cause it's adjacent to a flower
                # (the current one)
                count -= 1
            prev = 1
        else:
            if prev:
                # Flower in the previous spot,
                # can't place one here
                prev = 0
            else:
                count += 1
                prev = 1

    return count >= n


def one_scan3(flowerbed: List[int], n: int) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)

    if n == 0:
        return True

    size = len(flowerbed)
    for i in range(size):
        if (
            flowerbed[i] == 0
            and (i == 0 or flowerbed[i - 1] == 0)
            and (i == size - 1 or flowerbed[i + 1] == 0)
        ):
            n -= 1
            if n == 0:
                return True

            # Place a flower
            flowerbed[i] = 1

    return False


if __name__ == "__main__":
    print("-" * 60)
    print("Can place flowers")
    print("-" * 60)

    test_cases = [
        # (flowerbed, n, solution)
        ([0], 0, True),
        ([0], 1, True),
        ([0, 0], 2, False),
        ([0, 0, 0], 2, True),
        ([0, 1, 0], 1, False),
        ([1, 0, 1], 0, True),
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 0, 1], 2, False),
        ([1, 0, 0, 0, 0, 1, 0, 0], 2, True),
        ([0, 0, 1, 0, 0, 0, 0, 1, 0, 0], 3, True),
        ([0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], 4, False),
    ]

    for flowerbed, n, solution in test_cases:

        print("Flowerbed:", flowerbed)
        print("n:", n)

        result = one_scan(flowerbed, n)
        output = f"     one_scan = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = one_scan2(flowerbed, n)
        output = f"    one_scan2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = one_scan3(flowerbed, n)
        output = f"    one_scan3 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
