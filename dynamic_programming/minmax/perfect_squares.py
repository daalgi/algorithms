"""
https://leetcode.com/problems/perfect-squares/

Given an integer n, return the least number of perfect square 
numbers that sum to n.

A perfect square is an integer that is the square of an integer; 
in other words, it is the product of some integer with itself. 
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:
1 <= n <= 10^4
"""


def dp_tabulation(n: int) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(n sqrt(n))
    # Space complexity: O(n)

    # Table to store the least number of perfect square numbers (LNPSN)
    # that add up to `i`.
    # Since we're looking for the minimum value,
    # initialize the table with large values.
    dp = [float("inf")] * (n + 1)
    # Base case
    dp[0] = 0

    # Loop over the targets `i`
    for i in range(1, n + 1):
        # For each target `i`, check all the numbers whose square
        # is at most `i`
        j = 1
        while j * j <= i:
            # If the square of `j` is less or equal to the target `i`,
            # check the LNPSN
            dp[i] = min(
                # Current LNPSN
                dp[i],
                # LNPSN for `i - j * j` plus 1 (counting the current `j`)
                dp[i - j * j] + 1,
            )
            # Try next `j`
            j += 1

    return dp[-1]


if __name__ == "__main__":
    print("-" * 60)
    print("Perfect squares")
    print("-" * 60)

    test_cases = [
        (1, 1),  # 1 = 1
        (2, 2),  # 2 = 1 + 1
        (3, 3),  # 3 = 1 + 1 + 1
        (4, 1),  # 4 = 4
        (5, 2),  # 5 = 4 + 1
        (6, 3),  # 6 = 4 + 1 + 1
        (7, 4),  # 7 = 4 + 1 + 1 + 1
        (9, 1),  # 9 = 9
        (10, 2),  # 10 = 9 + 1
        (12, 3),  # 12 = 4 + 4 + 4 (NOT 12 = 9 + 1 + 1 + 1)
        (13, 2),  # 13 = 4 + 9
        (25, 1),  # 25 = 25 (5 * 5)
        (1986, 3),
        (1993, 2),
    ]

    for n, solution in test_cases:

        print("Number:", n)

        result = dp_tabulation(n)
        output = f"\t       dp_tabulation = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
