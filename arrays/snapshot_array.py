"""
https://leetcode.com/problems/snapshot-array/

Implement a SnapshotArray that supports the 
following interface:
- SnapshotArray(int length) initializes an array-like 
data structure with the given length.  
Initially, each element equals 0.
- void set(index, val) sets the element at the given 
index to be equal to val.
- int snap() takes a snapshot of the array and returns 
the snap_id: the total number of times we called 
snap() minus 1.
- int get(index, snap_id) returns the value at the given 
index, at the time we took the snapshot with 
the given snap_id

Example 1:
Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 
Constraints:
1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9
"""
from bisect import bisect_left


class SnapshotArray:
    def __init__(self, length: int):
        # Time complexity: O(n)
        # Space complexity: O(ns)
        self.snaps = [[0] * length]
        self.length = length

    def set(self, index: int, val: int) -> None:
        # Time complexity: O(1)
        if 0 <= index < self.length:
            self.snaps[-1][index] = val

    def snap(self) -> int:
        # Time complexity: O(n)
        self.snaps.append(self.snaps[-1][:])
        return len(self.snaps) - 2

    def get(self, index: int, snap_id: int) -> int:
        # Time complexity: O(1)
        if 0 <= snap_id < len(self.snaps) and 0 <= index < self.length:
            return self.snaps[snap_id][index]


class SnapshotArrayBinarySearch:
    def __init__(self, length: int):
        # Time complexity: O(n)
        # Space complexity: O(s)
        self.snaps = [{0: 0} for _ in range(length)]
        self.last_snap_id = 0
        self.length = length

    def set(self, index: int, val: int) -> None:
        # Time complexity: O(1)
        if 0 <= index < self.length:
            self.snaps[index][self.last_snap_id] = val

    def snap(self) -> int:
        # Time complexity: O(1)
        self.last_snap_id += 1
        return self.last_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # Time complexity: O(n + logn)
        # --> better to avoid calling `list()`
        if 0 <= snap_id <= self.last_snap_id and 0 <= index < self.length:
            if snap_id in self.snaps[index]:
                return self.snaps[index][snap_id]
            # Time complexity of converting dictionary keys to list:
            # O(n)
            snaps = list(self.snaps[index].keys())
            # Time complexity of finding the next smaller `snap_id`: O(logn)
            prev_snap_id = snaps[bisect_left(snaps, snap_id) - 1]
            return self.snaps[index][prev_snap_id]


class SnapshotArrayBinarySearch2:
    def __init__(self, length: int):
        # Time complexity: O(n)
        # Space complexity: O(s)
        self.arr = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int):
        # Time complexity: O(1)
        if self.arr[index][-1][0] == self.snap_id:
            self.arr[index][self.snap_id][1] = val
        else:
            self.arr[index].append([self.snap_id, val])

    def snap(self) -> int:
        # Time complexity: O(1)
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # Time complexity: O(logn)
        id = bisect_left(self.arr[index], [snap_id + 1]) - 1
        return self.arr[index][id][1]


if __name__ == "__main__":
    print("-" * 60)
    print("Snapshot array")
    print("-" * 60)

    length = 10
    test_cases = [
        # (method, arg1, arg2, return_value)
        ["set", 0, 32, None],
        ["set", 1, 86, None],
        ["snap", None, None, 0],
        ["set", 1, 93, None],
        ["get", 0, 0, 32],
        ["get", 1, 0, 86],
        ["get", 1, 1, 93],
        ["snap", None, None, 1],
        ["set", 0, 1986, None],
        ["set", 1, 1993, None],
        ["get", 0, 0, 32],
        ["get", 0, 1, 32],
        ["get", 0, 2, 1986],
        ["get", 1, 0, 86],
        ["get", 1, 1, 93],
        ["get", 1, 2, 1993],
    ]

    bforce = SnapshotArray(length=length)
    bs1 = SnapshotArrayBinarySearch(length=length)
    bs2 = SnapshotArrayBinarySearch2(length=length)

    for method, arg1, arg2, solution in test_cases:

        output = f">>{method}()"

        if method == "set":
            output += f": index={arg1}, val={arg2}"
            bforce.set(arg1, arg2)
            bs1.set(arg1, arg2)
            bs2.set(arg1, arg2)
            print(output)

        elif method == "snap":
            bforce.snap()
            bs1.snap()
            bs2.snap()
            print(output)

        else:
            output += f": index={arg1}, snap_id={arg2}"
            print(output)

            result = bforce.get(arg1, arg2)
            output = f"       brute_force = "
            output += str(result)
            output += " " * (50 - len(output))
            test_ok = result == solution
            output += f'Test: {"OK" if test_ok else "NOT OK"}'
            print(output)

            result = bs1.get(arg1, arg2)
            output = f"     binary_search = "
            output += str(result)
            output += " " * (50 - len(output))
            test_ok = result == solution
            output += f'Test: {"OK" if test_ok else "NOT OK"}'
            print(output)

            result = bs2.get(arg1, arg2)
            output = f"    binary_search2 = "
            output += str(result)
            output += " " * (50 - len(output))
            test_ok = result == solution
            output += f'Test: {"OK" if test_ok else "NOT OK"}'
            print(output)

        print()
