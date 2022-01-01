from typing import List
from dataclasses import dataclass


@dataclass
class ListNode:
    data: int = 0
    next = None


def list_to_linked_list(nums: List[int]) -> ListNode:
    # Time complexity: O(n)
    # Space complexity: O(1)
    head = ListNode()
    curr = head
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next

    return head.next


def linked_list_to_list(head: ListNode) -> List[int]:
    curr = head
    res = []
    while curr:
        res.append(curr.data)
        curr = curr.next

    return res


def print_linked_list(head: ListNode) -> None:
    print("Linked list: ", end="")
    if not head:
        return print("<empty>")

    print(f"{head.data}", end="")
    curr = head.next

    while curr:
        print(f" -> {curr.data}", end="")
        curr = curr.next
    print()


if __name__ == "__main__":
    print("-" * 60)
    print("Linked list utils")
    print("-" * 60)
