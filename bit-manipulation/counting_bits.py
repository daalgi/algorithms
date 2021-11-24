"""
https://leetcode.com/problems/counting-bits/

Given an integer n, return an array ans of length n + 1 
such that for each i (0 <= i <= n), ans[i] is the number 
of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
0 <= n <= 105

Follow up:
It is very easy to come up with a solution with a runtime 
of O(n log n). 
Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function 
(i.e., like __builtin_popcount in C++)?
"""


def count(num: int) -> list:
    # Keep track of the current integer, from 0 to `num`
    cur = 0
    # Store the count of 1s in each integer
    res = list()
    # Loop over all the integers between 0 and `num`
    while cur <= num:
        # Start the counter of ones in `cur`
        count = 0
        # Assign a temporary value for `cur`
        temp = cur
        # While `temp` is greater than 0
        while temp:
            # n & (n - 1) removes the rightmost set bit
            temp &= temp - 1
            # increment the count
            count += 1

        # Append the count to the result list
        res.append(count)
        # Update `cur` for next iteration
        cur += 1

    return res


def patterns(num: int) -> list:
    res = [0] * (num + 1)
    offset = 1
    for i in range(1, num + 1):
        if offset * 2 == i:
            offset *= 2
        res[i] = res[i - offset] + 1
    return res


def dp(num: int) -> list:
    res = [0]
    for i in range(1, num + 1):
        if i & 1 == 0:
            # If it's even, we can shift the last bit (a 0),
            # and the resulting integer corresponds with
            # a previously computed integer,
            # so the number of set bits will be the same
            # i.e. 110010 >> 1 = 11001 (3 1s)
            res.append(res[i >> 1])
        else:
            # If it's odd, we can shift the last bit (a 1),
            # and the resulting integer corresponds with a
            # previously computed integer,
            # so the number of set bits will differ by 1
            # i.e. 110011 - 1 = 110010 (3 + 1 = 4 1s)
            res.append(res[i - 1] + 1)

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Counting bits")
    print("-" * 60)

    test_cases = [
        (0, [0]),
        (1, [0, 1]),
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
        (13, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3]),
    ]

    for num, solution in test_cases:

        string = f"   count({num}) = "
        string += " " * (15 - len(string))
        result = count(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f"patterns({num}) = "
        string += " " * (15 - len(string))
        result = patterns(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f"      dp({num}) = "
        string += " " * (15 - len(string))
        result = dp(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
