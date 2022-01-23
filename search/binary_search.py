from typing import List


def search(nums: List[int], target: int) -> int:
    # Time complexity: O(logn)
    # Space complexity: O(1)

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    return right if nums[right] == target else None


def search_equal_or_next_smaller(nums: List[int], target: int) -> int:
    # Time complexity: O(logn)
    # Space complexity: O(1)

    # Returns the index of the `target`, or if not found,
    # the next smaller value.

    # Base case, target less than the smallest value
    if nums[0] > target:
        return None

    left, right = 0, len(nums) - 1

    # Base case, target greater than the largest value
    if nums[-1] < target:
        return right

    # Binary search
    last_valid = left
    while left < right:
        mid = (left + right) // 2
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
            # Keep track of the last `mid` pointer, so we have
            # the last index before left > right, which is
            # effectively the next smaller value to `target`
            # if `target` is not in `nums`
            last_valid = mid

    # If `target` was found, return its index;
    # otherwise, return the last valid index before left > right
    return right if nums[right] == target else last_valid


def search_equal_or_next_greater(nums: List[int], target: int) -> int:
    # Time complexity: O(logn)
    # Space complexity: O(1)

    # Returns the index of the `target`, or if not found,
    # the next greater value.

    if nums[0] > target:
        return 0

    left, right = 0, len(nums) - 1

    if nums[right] < target:
        return None

    # Binary search
    while left < right:
        mid = (left + right) // 2
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1

    # If `target` was found return `right`;
    # if not, return `right` as well, since in this case
    # it's the index of the next greater value
    return right


if __name__ == "__main__":
    print("-" * 60)
    print("Binary search")
    print("-" * 60)

    test_cases = [
        # (nums, target, search_solution, search_eq_sm_solution, search_eq_gt_solution)
        ([0], 0, 0, 0, 0),
        ([1, 3, 5, 7, 13, 20], 0, None, None, 0),
        ([1, 3, 5, 7, 13, 20], 3, 1, 1, 1),
        ([1, 3, 5, 7, 13, 20], 5, 2, 2, 2),
        ([1, 3, 5, 7, 13, 20], 6, None, 2, 3),
        ([1, 3, 5, 7, 13, 20], 7, 3, 3, 3),
        ([1, 3, 5, 7, 13, 20], 8, None, 3, 4),
        ([1, 3, 5, 7, 13, 20], 12, None, 3, 4),
        ([1, 3, 5, 7, 13, 20], 18, None, 4, 5),
        ([1, 3, 5, 7, 13, 20], 20, 5, 5, 5),
        ([1, 3, 5, 7, 13, 20], 21, None, 5, None),
    ]

    for (
        nums,
        target,
        search_solution,
        search_eq_sm_solution,
        search_eq_gt_solution,
    ) in test_cases:

        print("Array:", nums)
        print("Target:", target)

        result = search(nums, target)
        output = f"                        search = "
        output += f"{result}"
        if result is not None:
            output += f" ({nums[result]})"
        test_ok = search_solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = search_equal_or_next_smaller(nums, target)
        output = f"  search_equal_or_next_smaller = "
        output += f"{result}"
        if result is not None:
            output += f" ({nums[result]})"
        test_ok = search_eq_sm_solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = search_equal_or_next_greater(nums, target)
        output = f"  search_equal_or_next_greater = "
        output += f"{result}"
        if result is not None:
            output += f" ({nums[result]})"
        test_ok = search_eq_gt_solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
