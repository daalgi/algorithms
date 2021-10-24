"""
CRACKING THE CODING INTERVIEW
3.5. Sort Stack:
Write a program to sort a stack such that the smallest items
are on the top. You can use an additional temporary stack,
but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations:
push, pop, peek, and is_empty.
"""
from dataclasses import dataclass


@dataclass
class StackNode:
    data: int
    next = None


class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, data: int):
        node = StackNode(data)
        node.next = self.top
        self.top = node

    def peek(self) -> int:
        if self.top is None:
            return None
        return self.top.data

    def pop(self) -> int:
        if self.top is None:
            raise ValueError("The stack is empty, `pop()` failed")
        data = self.top.data
        self.top = self.top.next
        return data

    def is_empty(self) -> bool:
        return self.top is None


class SortStack:
    def __init__(self):
        self.stack = Stack()

    def push(self, data: int):
        if self.stack.is_empty() or data >= self.stack.peek():
            self.stack.push(data)
            return

        # If after pushing the new data the stack
        # is not sorted, use an additional stack
        # to store temporarily the values greater than `data`.
        temp = Stack()
        while not self.stack.is_empty() and data < self.stack.peek():
            temp.push(self.stack.pop())

        # Add the new `data` to the stack in the correct location
        self.stack.push(data)

        # Move back the values in the temperary stack
        while not temp.is_empty():
            self.stack.push(temp.pop())

    def peek(self) -> int:
        return self.stack.peek()

    def pop(self) -> int:
        return self.stack.pop()

    def is_empty(self) -> int:
        return self.stack.is_emtpy()


if __name__ == "__main__":
    print('-' * 60)
    print("SORT STACK")
    print('-' * 60)

    print("\nPushing data into the SortStack...")
    stack = SortStack()
    for i in range(10, 5, -1):
        stack.push(i)
        print(f"stack.push({i})")
        print(f"stack.peek() = {stack.peek()}", stack.peek() == 10)
        print()

    print("\nPushing and popping data...")
    stack = SortStack()
    stack.push(2)
    print(f"stack.push({2})")
    print(f"stack.peek() = {stack.peek()}", stack.peek() == 2)
    
    stack.push(1)
    print(f"\nstack.push({1})")
    print(f"stack.peek() = {stack.peek()}", stack.peek() == 2)
    
    stack.push(3)
    print(f"\nstack.push({3})")
    print(f"stack.peek() = {stack.peek()}", stack.peek() == 3)
    
    stack.push(0)
    print(f"\nstack.push({0})")
    print(f"stack.peek() = {stack.peek()}", stack.peek() == 3)

    print(f"\nstack.pop() = {stack.pop()}")
    print(f"stack.peek() = {stack.peek()}", stack.peek() == 2)

    print(f"\nstack.pop() = {stack.pop()}")
    print(f"stack.peek() = {stack.peek()}", stack.peek() == 1)
    
    print(f"\nstack.pop() = {stack.pop()}")
    print(f"stack.peek() = {stack.peek()}", stack.peek() == 0)
    
    print(f"\nstack.pop() = {stack.pop()}")
    print(f"stack.peek() = {stack.peek()}", stack.peek() is None)
    print()