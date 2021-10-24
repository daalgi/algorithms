"""
CRACKING THE CODING INTERVIEW
3.4. Queue via stacks:
Implement a `MyQueue` class which implements aqueue using two stacks.
"""
from dataclasses import dataclass


@dataclass
class StackNode:
    data: int
    next = None


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self, data: int):
        node = StackNode(data)
        node.next = self.top
        self.top = node
        self.size += 1

    def peek(self) -> int:
        if self.top is None:
            return None
        return self.top.data

    def pop(self) -> int:
        if self.top is None:
            raise ValueError("The stack is empty, `pop()` failed")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def is_empty(self):
        return self.size == 0


class MyQueue:
    def __init__(self) -> None:
        self.newest_stack = Stack()
        self.oldest_stack = Stack()

    def push(self, data: int):
        self.newest_stack.push(data)

    def peek(self) -> int:
        # In a queue, peek() returns the oldest element

        # Shift the elements from the `newest_stack`
        # to the `oldest_stack`
        self._shift_to_oldest()

        # Peek the newest node in the `oldest_stack`,
        # which was the oldest node in the `newest_stack`
        return self.oldest_stack.peek()

    def _shift_to_oldest(self):
        # Shifts the elements from `newest_stack`
        # to `oldest_stack` only if
        # `oldest_stack` is empty
        if self.oldest_stack.is_empty():
            while self.newest_stack.size:
                elem = self.newest_stack.pop()
                self.oldest_stack.push(elem)

    def pop(self):
        # Ensure `oldest_stack` has the current elements
        self._shift_to_oldest()

        return self.oldest_stack.pop()


if __name__ == "__main__":
    print("-" * 60)
    print("QUEUE VIA TWO STACKS")
    print("-" * 60)

    stack = MyQueue()
    print("\nPushing data into MyQueue...")
    for i in range(5, 10):
        stack.push(i)
        print(f"stack.push({i})")
        print(f"stack.peek() = {stack.peek()}", stack.peek() == 5)
        print()

    stack = MyQueue()
    print("Pushing data into MyQueue...")
    for i in range(5, 10):
        stack.push(i)
        print(f"stack.push({i})")
    print(f"stack.peek() = {stack.peek()}", stack.peek() == 5)

    print("\nPopping data from MyQueue...")
    for i in range(5, 9):
        print(f"stack.pop() = {stack.pop()}")
        print(f"stack.peek() = {stack.peek()}", stack.peek() == i + 1)
        print()
    print(f"stack.pop() = {stack.pop()}")
    print(f"stack.peek() = {stack.peek()}", stack.peek() is None)
