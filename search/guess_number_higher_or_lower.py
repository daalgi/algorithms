"""
https://leetcode.com/problems/guess-number-higher-or-lower/

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which 
number I picked.

Every time you guess wrong, I will tell you whether 
the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which r
eturns three possible results:
    -1: Your guess is higher than the number I 
    picked (i.e. num > pick).
    1: Your guess is lower than the number I 
    picked (i.e. num < pick).
    0: your guess is equal to the number I 
    picked (i.e. num == pick).

Return the number that I picked.

Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1

Constraints:
1 <= n <= 2^31 - 1
1 <= pick <= n
"""


class API:
    def __init__(self, number: int) -> None:
        self.number = number

    def guess(self, pick: int) -> int:
        if pick < self.number:
            return 1
        if pick > self.number:
            return -1
        return 0


def binary_search(n: int, api: API) -> int:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    """
    1 2 3 4 5 6 7 8 9 10  num=9
    L       M         R   pick=5 < num --> g = +1
              L   M   R   pick=8 < num --> g = +1
                    L R   pick=9 ok

    1 2 3 4 5 6 7 8 9 10  num=4
    L       M         R   pick=5 > num --> g = -1
    L M   R               pick=2 < num --> g = +1
        L R               pick=3 < num --> g = +1
         LMR              pick=4 ok
    """
    left, right = 1, n
    while left <= right:
        #mid = left + (right - left) // 2
        mid = (left + right) // 2
        guess = api.guess(pick=mid)
        if guess < 0:
            right = mid - 1
        elif guess > 0:
            left = mid + 1
        else:
            return mid


if __name__ == "__main__":
    print("-" * 60)
    print("Guess number higher or lower")
    print("-" * 60)

    test_cases = [
        # (n, solution)
        (1, 1),
        (13, 8),
        (25, 13),
        (86, 25),
        (93, 86),
        (987654321, 987654),
        (2147483647, 46340),  # MAX 32-bit number
    ]

    for n, solution in test_cases:

        print("Numbers:", n)

        api = API(number=solution)
        result = binary_search(n, api)
        output = f"     binary_search = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (40 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
