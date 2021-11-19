"""
CRACKING THE CODING INTERVIEW
10.5 Sparse search.

Given a sorted array of strings that is interspersed with empty strings,
write a method to find the location of a given string.

Example:
Input: ball, ["at", "", "", "","ball", "", "", "car", "", "", "dad", "", "",]
Output: 4
"""


def sparse_search(array: list, target: str) -> int:

    def search(array: list, target: str, first: int, last: int) -> int:
        # Middle index
        mid = (first + last) // 2

        # If the middle element is an empty string, find the closest
        # non-empty string
        if array[mid] == "":
            left = mid - 1
            right = mid + 1
            while True:
                if first <= left and array[left] != "":
                    mid = left
                    break
                elif right <= last and array[right] != "":
                    mid = right
                    break
                elif left < first and right > last:
                    return -1
                left -= 1
                right += 1

        # If is a non-empty string
        if array[mid] == target:
            # Found it
            return mid
        if array[mid] < target:
            # Search in the right half
            return search(array, target, mid + 1, last)
        # Search in the left half
        return search(array, target, first, mid - 1)

    if target == "" or len(array) == 0:
        return -1
    return search(array, target, 0, len(array) - 1)


if __name__ == "__main__":
    print("-" * 60)
    print("Sparse search")
    print("-" * 60)

    strings = ["at", "", "", "","ball", "", "", "car", "", "", "dad", "", ""]
    test_cases = [
        (strings, "at", 0),
        (strings, "ball", 4),
        (strings, "car", 7),
        (strings, "dad", 10),
        (strings, "pen", -1),
        (strings, "", -1),
    ]

    for array, target, solution in test_cases:
        array_string = str(array)
        if len(array_string) > 20:
            array_string = array_string[:20] + "...]"

        result = sparse_search(array, target)
        string = f"search{array_string, target} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

    # case = 0
    # array = test_cases[case][0]
    # target = "at"
    # print(array)
    # print(target, sparse_search(array, target))