"""
https://leetcode.com/problems/design-hashset/

Design a HashSet without using any built-in hash
table libraries.

Implement MyHashSet class:
- void add(key) Inserts the value key into the HashSet.
- bool contains(key) Returns whether the value key exists 
in the HashSet or not.
- void remove(key) Removes the value key in the HashSet. 
If key does not exist in the HashSet, do nothing.

Example 1:
Input
["MyHashSet", "add", "add", "contains", "contains", 
"add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
 
Constraints:
0 <= key <= 10^6
At most 10^4 calls will be made to add, remove, and contains.
"""
from typing import List


class HashSet:
    def __init__(self):
        self.MAX = 10000
        self.buckets = [[] for _ in range(self.MAX)]

    def _hash(self, key: int) -> int:
        return key % self.MAX

    def _get_bucket(self, key: int) -> List[int]:
        return self.buckets[self._hash(key)]

    def add(self, key: int):
        bucket = self._get_bucket(key)
        # Loop over the elements of the bucket where `key`
        # should be stored to check if it already exists
        for element in bucket:
            if element == key:
                # If the element already is in the `HashSet`,
                # don't add it again
                return
        # If `key` is not yet in the `HashSet`, add it
        # to the corresponding `bucket`
        bucket.append(key)

    def remove(self, key: int) -> int:
        bucket = self._get_bucket(key)
        # Loop over the elements of the `bucket`
        for i in range(len(bucket)):
            if bucket[i] == key:
                # If the element is found, remove it
                # from the `bucket`
                bucket.pop(i)
                return key
        # If not found, return `None`
        return None

    def contains(self, key: int) -> bool:
        return key in self._get_bucket(key)


if __name__ == "__main__":
    print("-" * 60)
    print("Design Hashset")
    print("-" * 60)

    hset = HashSet()
    max_val = 9

    for e in range(max_val + 1):
        hset.add(e)
        print(f"HashSet.add({e})")
    print()

    # Contains
    for e in range(max_val - 3, max_val + 3):
        result = hset.contains(e)
        test_ok = result == (True if e <= max_val else False)
        output = f"HashSet.contains({e}) = {result}"
        output += " " * (45 - len(output))
        output += f"Test: {'OK' if test_ok else 'NOT OK'}"
        print(output)
    print()

    for num in [18, 4, 5]:
        print(f"Hashset.contains({num}) = {hset.contains(num)}")
        hset.remove(num)
        print(f"Hashset.remove({num})")
        print(f"Hashset.contains({num}) = {hset.contains(num)}")
        print()

    num = 86
    print(f"Hashset.contains({num}) = {hset.contains(num)}")
    hset.add(num)
    print(f"Hashset.add({num})")
    print(f"Hashset.contains({num}) = {hset.contains(num)}")
    print()
