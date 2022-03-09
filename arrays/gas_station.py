"""
https://leetcode.com/problems/gas-station/

There are n gas stations along a circular route, 
where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it 
costs cost[i] of gas to travel from the ith station 
to its next (i + 1)th station. You begin the journey 
with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the 
starting gas station's index if you can travel around 
the circuit once in the clockwise direction, otherwise 
return -1. If there exists a solution, it is guaranteed 
to be unique

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. 
Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough 
to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough 
gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. 
Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit 
of gas but you only have 3.
Therefore, you can't travel around the circuit once no 
matter where you start.

Constraints:
n == gas.length == cost.length
1 <= n <= 10^5
0 <= gas[i], cost[i] <= 10^4
"""
from typing import List


def brute_force(gas: List[int], cost: List[int]) -> int:
    # Time complexity: O(n²)
    # Space complexity: O(1)
    pass


def greedy(gas: List[int], cost: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)

    # We can only travel to all the stations if
    # there's in total enough gas to cover all the cost,
    # that's the sum of all diff_i = gas_i - cost_i is
    # greater or equal than zero.
    # If there's a solution, it's guaranteed to be unique,
    # so we can find it checking at every step if the
    # current gas is non-negative.

    n = len(gas)
    start = current_gas = total_gas = 0
    for i in range(n):
        diff = gas[i] - cost[i]
        current_gas += diff
        total_gas += diff
        if current_gas < 0:
            # Currently not enough gas, so the start
            # can't be at any point before `i`
            start = i + 1
            # Restart `current_gas` as if starting
            # from `i+1`
            current_gas = 0

    # If there was enough gas, return the starting point
    if total_gas >= 0:
        return start
    # If there was not enough gas, return -1
    return -1


if __name__ == "__main__":
    print("-" * 60)
    print("Gas station")
    print("-" * 60)

    test_cases = [
        # (gas, cost, solution)
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 9], -1),
        ([2, 3, 4], [3, 4, 3], -1),
    ]

    for gas, cost, solution in test_cases:

        print("Gas: ", gas)
        print("Cost:", cost)

        result = greedy(gas, cost)
        output = "     greedy = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
