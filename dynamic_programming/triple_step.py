"""
CRACKING THE CODING INTERVIEW
8.1 Triple step:
A child is running up a staircase with n steps and can hop
either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the
child can run up the stairs.
"""


def brute_force(steps: int) -> int:
    # Time complexity: O(3^n)
    # Space complexity: O(n)
    # where n is the number of steps
    if steps == 0:
        return 1
    if steps < 0:
        return 0

    return brute_force(steps - 1) + brute_force(steps - 2) + brute_force(steps - 3)


def dp_recursion(steps: int) -> int:
    # Initialize an array to save the computed solutions
    # memo[ith_step] = num_paths_to_get_there
    memo = [None] * (steps + 1)

    # Recursive function
    def r(steps: int) -> int:
        # Base cases
        if steps == 0:
            return 1
        if steps < 0:
            return 0

        # If the result has been already computed
        if memo[steps] is not None:
            # return the computed result
            return memo[steps]

        # Recursive call and store the result in `memo`
        memo[steps] = r(steps - 1) + r(steps - 2) + r(steps - 3)
        # Return the number of ways to get to the current `step`
        return memo[steps]

    # Return the result of the recursive function
    return r(steps)


def dp_iterative(steps: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Base cases
    if steps <= 0:
        return 0
    if 0 < steps < 3:
        return steps

    # Initialize an array to save the computed solutions
    # memo[ith_step] = num_paths_to_get_there
    memo = [None] * (steps + 1)
    # Initialize with the first 3 steps with their solutions
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2

    # Loop over the steps
    for i in range(3, steps + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

    # Return the number of possible ways to run up the stairs
    return memo[steps]


if __name__ == "__main__":
    print("-" * 60)
    print("Triple step")
    print("-" * 60)

    test_cases = [
        (1, 1),
        (2, 2),
        (3, 4),
        (4, 7),
        (13, 1705),
        (25, 2555757),
    ]

    for num, solution in test_cases:

        string = f" brute_force({num}) = "
        string += " " * (25 - len(string))
        result = brute_force(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f"dp_recursion({num}) = "
        string += " " * (25 - len(string))
        result = dp_recursion(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f"dp_iterative({num}) = "
        string += " " * (25 - len(string))
        result = dp_iterative(num)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
