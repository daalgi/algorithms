"""
CRACKING THE CODING INTERVIEW
3.3. Stacks of plates:
Imagine a (literal) stack of plates. If the stack gets too high,
it might topple. Therefore, in real life, we would likely start
a new stack when the previous stack exceeds some threshold.
Implement a data structure `SetOfStacks` that mimics this.
`SetOfStacks` should be composed of several stacks and should create
a new stack once the previous one exceeds capacity.
`SetOfStacks.push()` and `SetOfStacks.pop()` should behave identically
to a single stack (that is, pop() should return the same values
as it would if there were just a single stack).
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


@dataclass
class SetOfStacks:
    capacity: int

    def __post_init__(self) -> None:
        self.stacks = []

    def push(self, data: int):
        if len(self.stacks) == 0 or self.stacks[-1].size >= self.capacity:
            self.stacks.append(Stack())

        self.stacks[-1].push(data)

    def peek(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[-1].peek()

    def pop(self) -> int:
        if len(self.stacks) == 0:
            raise ValueError("The stacks are empty")

        data = self.stacks[-1].pop()

        if self.stacks[-1].size == 0:
            self.stacks.pop()

        return data


if __name__ == "__main__":
    stack = SetOfStacks(capacity=2)
    print("\nPushing data into the SetOfStacks...")
    for i in range(5, 10):
        print(f"Current number of stacks: {len(stack.stacks)}")
        stack.push(i)
        print(f"stack.push({i})")
        print(f"Current number of stacks: {len(stack.stacks)}")
        print(f"stack.peek() = {stack.peek()}", stack.peek() == i)
        print()

    print("\nPopping data from the SetOfStacks...")
    for i in range(4):
        print(f"Current number of stacks: {len(stack.stacks)}")
        data = stack.pop()
        print(f"stack.pop() = {data}")
        print(f"Current number of stacks: {len(stack.stacks)}")
        print(f"stack.peek() = {stack.peek()}", stack.peek() == 8 - i)
        print()

    print(f"Current number of stacks: {len(stack.stacks)}")
    data = stack.pop()
    print(f"stack.pop() = {data}")
    print(f"stack.peek() = {stack.peek()}", stack.peek() is None)
    print(f"Current number of stacks: {len(stack.stacks)}")
