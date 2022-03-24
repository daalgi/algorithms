"""
https://leetcode.com/problems/time-based-key-value-store/

Design a time-based key-value data structure that can store 
multiple values for the same key at different time stamps and 
retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the 
key key with the value value at the given time timestamp.
- String get(String key, int timestamp) Returns a value such that 
set was called previously, with timestamp_prev <= timestamp. 
If there are multiple such values, it returns the value associated 
with the largest timestamp_prev. If there are no values, it returns "".
 
Example 1:
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], 
["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
 
Constraints:
1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 10^7
All the timestamps timestamp of set are strictly increasing.
At most 2 * 10^5 calls will be made to set and get.
"""
from collections import defaultdict


class BinarySearch:
    def __init__(self):
        # Time complexity: O(1)
        # Space complexity: O(n) as the store increases

        # Map { key: [(timestamp1, value1), ...], }
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Time complexity: O(1)
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Time complexity: O(logn)
        # Space complexity: O(1)

        # Array of values for `key`
        arr = self.hashmap[key]

        # Edge case: no values or not yet created at `timestamp`
        if not arr or timestamp < arr[0][0]:
            return ""

        # Edge case: last value
        if timestamp >= arr[-1][0]:
            return arr[-1][1]

        # Binary search to find the `value` at a given `timestamp`
        # (search `timestamp` or the nearest smallest time)
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if timestamp < arr[mid][0]:
                right = mid
            elif timestamp > arr[mid][0]:
                left = mid + 1
            else:
                # If `timestamp` found in the list,
                # return the associated `value`
                return arr[mid][1]

        # If `timestamp` not found (but we know it's a value within
        # `arr`), return the previous value to the one where
        # the two pointers `left` and `right` crossed
        return arr[left - 1][1]


if __name__ == "__main__":
    print("-" * 60)
    print("Time based key value store")
    print("-" * 60)

    set_values = [
        # (key, value, timestamp)
        (["reinf", "br", 3]),
        (["reinf", "bt", 5]),
        (["reinf", "tr", 10]),
        (["reinf", "tt", 13]),
    ]

    test_cases = [
        # (key, timestamp, solution)
        ("reinf", 1, ""),
        ("reinf", 3, "br"),
        ("reinf", 4, "br"),
        ("reinf", 5, "bt"),
        ("reinf", 6, "bt"),
        ("reinf", 8, "bt"),
        ("reinf", 10, "tr"),
        ("reinf", 11, "tr"),
        ("reinf", 12, "tr"),
        ("reinf", 13, "tt"),
        ("reinf", 25, "tt"),
    ]

    time = BinarySearch()
    for key, value, timestamp in set_values:
        time.set(key, value, timestamp)

    print("Timestamps for 'reinf':")
    for timestamp, value in time.hashmap["reinf"]:
        print("   ", timestamp, "-->", value)

    for key, timestamp, solution in test_cases:

        print(f"get({key}, {timestamp})")

        result = time.get(key, timestamp)
        output = f"      binary_search = "
        output += str(result)
        test_ok = result == solution
        output += " " * (50 - len(output))
        output += f"Test {'OK' if test_ok else 'NOT OK'}"
        print(output)

        print()
