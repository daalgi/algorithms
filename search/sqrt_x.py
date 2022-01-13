"""
https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, compute and 
return the square root of x.

Since the return type is an integer, the decimal 
digits are truncated, and only the integer part 
of the result is returned.

Note: You are not allowed to use any built-in exponent 
function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and 
since the decimal part is truncated, 2 is returned.

Constraints:
0 <= x <= 2^31 - 1
"""


def binary_search(x: int) -> int:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    if x < 4:
        return min(x, 1)

    # Use two pointers to
    left, right = 0, x
    while left < right:
        # Middle point tilted to the right
        # `mid = (left + right + 1) // 2` can overflow,
        # to prevent it use this expanded relationship
        mid = left + (right - left + 1) // 2
        if mid <= x // mid:
            # Compare `mid <= x // mid` to avoid overflow,
            # instead of `mid * mid <= x`
            # In this case, we still have to increment the value,
            # so move the `left` pointer to the `mid` point
            left = mid
        else:
            # The current `mid` is too large,
            # we have to reduce it moving the `right` pointer.
            # Add a `-1` to ensure that when the
            # distance `right - left = 1`, the loop
            # doesn't get stuck (infinite loop)
            right = mid - 1

    return right


def newton(x: int) -> int:
    # Time complexity: O(log(logn))
    # Space complexity: O(1)
    # https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division
    r = x
    while r * r > x:
        r = (r + x // r) // 2
    return r


if __name__ == "__main__":
    print("-" * 60)
    print("Sqrt(x)")
    print("-" * 60)

    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 2),
        (8, 2),
        (9, 3),
        (13, 3),
        (25, 5),
        (144, 12),
        (145, 12),
        (16984963, 4121),
        (2147483647, 46340),  # MAX 32-bit number
    ]

    for x, solution in test_cases:

        print("x:", x)

        result = binary_search(x)
        output = f"     binary_search = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = newton(x)
        output = f"            newton = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
