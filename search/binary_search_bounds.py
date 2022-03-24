"""
Assume search intervals in "closed ends", [left, right),
so the while loop condition will be `left <= right`,
so the loop will finish when `left` exceeds `right`
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    # Time complexity: O(logn)
    # Space complexity: O(1)

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            # An index with `target` found
            # (there might be more valid indices)
            return mid
    return None


def search_left_bound(nums: List[int], target: int) -> int:
    # Time complexity: O(logn)
    # Space complexity: O(1)

    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        elif target == nums[mid]:
            # Lock the left border, so we can find the first
            # appearance of `target`
            right = mid - 1

    # Check boundaries
    if left >= n or nums[left] != target:
        return None

    return left


def search_right_bound(nums: List[int], target: int) -> int:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        elif target == nums[mid]:
            # Lock the right border, so we can find the last
            # appearance of `target`
            left = mid + 1

    # Check boundaries
    if right < 0 or nums[right] != target:
        return None

    return right


if __name__ == "__main__":
    print("-" * 60)
    print("Binary search bounds (open ends)")
    print("-" * 60)

    test_cases = [
        # (
        #   nums, target, search_solution,
        #   search_left_bound_solution, search_right_bound_solution,
        # )
        ([0], 0, 0, 0, 0),
        ([1, 3, 8, 9], 8, 2, 2, 2),
        ([1, 3, 8, 8, 8, 8, 8, 9], 3, 1, 1, 1),
        ([1, 3, 8, 8, 8, 8, 8, 9], 8, False, 2, 6),
        ([1, 3, 8, 8, 8, 8, 8, 13], 10, None, None, None),
    ]

    for (
        nums,
        target,
        search_solution,
        search_left_bound_solution,
        search_right_bound_solution,
    ) in test_cases:

        print("Array:", nums)
        print("Target:", target)

        if search_solution is not False:
            result = search(nums, target)
            output = f"                  search = "
            output += f"{result}"
            if result is not None:
                output += f" ({nums[result]})"
            test_ok = search_solution == result
            output += " " * (55 - len(output))
            output += f'Test: {"OK" if test_ok else "NOT OK"}'
            print(output)

        result = search_left_bound(nums, target)
        output = f"       search_left_bound = "
        output += f"{result}"
        if result is not None:
            output += f" ({nums[result]})"
        test_ok = search_left_bound_solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = search_right_bound(nums, target)
        output = f"      search_right_bound = "
        output += f"{result}"
        if result is not None:
            output += f" ({nums[result]})"
        test_ok = search_right_bound_solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
