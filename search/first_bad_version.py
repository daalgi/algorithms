"""
https://leetcode.com/problems/first-bad-version/

You are a product manager and currently leading a 
team to develop a new product. Unfortunately, the 
latest version of your product fails the quality check. 
Since each version is developed based on the previous 
version, all the versions after a bad version are 
also bad.

Suppose you have n versions [1, 2, ..., n] and you 
want to find out the first bad one, which causes all 
the following ones to be bad.

You are given an API bool isBadVersion(version) which 
returns whether version is bad. Implement a function 
to find the first bad version. You should minimize the 
number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
1 <= bad <= n <= 2^31 - 1
"""


def is_bad_version(x: int, b: int) -> bool:
    return x >= b


def binary_search(n: int, b: int) -> int:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    left, right = 1, n
    while left < right:
        # To avoid overflow, use the following relationship
        # to find `mid`
        mid = left + (right - left) // 2
        if is_bad_version(mid, b):
            right = mid
        else:
            left = mid + 1
    return right


if __name__ == "__main__":
    print("-" * 60)
    print("First bad version")
    print("-" * 60)

    test_cases = [
        # (n_versions, b_first_bad_version (solution))
        (1, 1),
        (13, 8),
        (25, 13),
        (86, 25),
        (93, 86),
        (987654321, 987654),
        (2147483647, 46340),  # MAX 32-bit number
    ]

    for n, first_bad_version in test_cases:

        print("Versions:", n)

        result = binary_search(n, first_bad_version)
        output = f"     binary_search = "
        output += " " * (10 - len(output))
        test_ok = first_bad_version == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
