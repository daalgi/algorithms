"""
https://leetcode.com/problems/optimal-account-balancing/

You are given an array of transactions transactions where 
transactions[i] = [fromi, toi, amounti] indicates that the 
person with ID = fromi gave amounti $ to the person 
with ID = toi.

Return the minimum number of transactions required 
to settle the debt.

Example 1:
Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt 
is person #1 pays person #0 and #2 $5 each.

Example 2:
Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
Output: 1
Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, 
and all debt is settled.

Constraints:
1 <= transactions.length <= 8
transactions[i].length == 3
0 <= fromi, toi <= 20
fromi != toi
1 <= amounti <= 100
"""
from typing import List


def sorting_incorrect(transactions: List[List[int]]) -> int:
    # INCORRECT! This solution doesn't assure that the
    # number of transactions is minimum

    max_persons = 21
    balance = [0] * max_persons
    for sender, receiver, amount in transactions:
        balance[sender] -= amount
        balance[receiver] += amount

    balance.sort()
    count, left, right = 0, 0, max_persons - 1
    while balance[left] < 0 and balance[right] > 0:
        if balance[right] >= -balance[left]:
            balance[right] -= -balance[left]
            balance[left] = 0
            left += 1
        else:
            balance[left] += balance[right]
            balance[right] = 0
            right -= 1

        if balance[right] == 0:
            right -= 1

        count += 1

    return count


def backtracking(transactions: List[List[int]]) -> int:
    # Time complexity: O(n!)
    # Space complexity: O(n)

    def backtrack(person: int, balances: List[int]) -> int:
        # Skip already settled balances
        while person < max_persons and balances[person] == 0:
            person += 1

        # Base case: reached the end of the `balances` list
        if person == max_persons:
            return 0

        # Recursevely loop over the next persons
        min_transactions = float("inf")
        for next_person in range(person + 1, max_persons):
            if balances[next_person] * balances[person] < 0:
                # Perform a transaction
                balances[next_person] += balances[person]
                min_transactions = min(
                    # Current transactions
                    min_transactions,
                    # Further explore
                    backtrack(person + 1, balances) + 1,
                )
                # Undo and continue exploring
                balances[next_person] -= balances[person]

        return min_transactions

    # Build the `balances` list
    max_persons = 21
    balances = [0] * max_persons
    for sender, receiver, amount in transactions:
        balances[sender] -= amount
        balances[receiver] += amount

    return backtrack(0, balances)


def backtracking2(transactions: List[List[int]]) -> int:
    # Time complexity: O(n!)
    # Space complexity: O(n)

    def backtrack(person: int, balances: List[int]) -> int:
        # Skip already settled balances
        while person < max_persons and balances[person] == 0:
            person += 1

        # Base case: reached the end of the `balances` list
        if person == max_persons:
            return 0

        # Recursevely loop over the next persons
        min_transactions = float("inf")
        for next_person in range(person + 1, max_persons):
            if balances[next_person] * balances[person] < 0:
                # Perform a transaction
                balances[next_person] += balances[person]
                min_transactions = min(
                    # Current transactions
                    min_transactions,
                    # Further explore
                    backtrack(person + 1, balances) + 1,
                )
                # Undo and continue exploring
                balances[next_person] -= balances[person]

        return min_transactions

    # Build the `balances` list
    max_persons = 21
    balances = [0] * max_persons
    for sender, receiver, amount in transactions:
        balances[sender] -= amount
        balances[receiver] += amount

    # Remove already settled balances
    balances = [b for b in balances if b != 0]
    max_persons = len(balances)

    return backtrack(0, balances)


if __name__ == "__main__":
    print("-" * 60)
    print("Optimal account balancing")
    print("-" * 60)

    test_cases = [
        # (transactions, solution)
        ([[0, 1, 10], [2, 0, 5]], 2),
        (
            [
                [0, 1, 10],
                [2, 0, 5],
                [1, 3, 13],
                [3, 2, 5],
                [2, 4, 10],
                [4, 0, 3],
                [1, 5, 9],
                [3, 4, 9],
            ],
            5,
        ),
        ([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]], 1),
        (
            [
                [0, 1, 2],
                [1, 2, 2],
                [2, 3, 2],
                [3, 4, 2],
                [4, 5, 99],
                [5, 6, 20],
                [6, 7, 10],
                [7, 8, 3],
            ],
            5,
        ),
        ([[1, 5, 8], [8, 9, 8], [2, 3, 9], [4, 3, 1]], 4),
    ]

    for transactions, solution in test_cases:

        print("Transactions:")
        print(transactions)

        result = sorting_incorrect(transactions)
        output = f"   sorting_incorrect = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = backtracking(transactions)
        output = f"        backtracking = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = backtracking2(transactions)
        output = f"       backtracking2 = "
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
