from dataclasses import dataclass


@dataclass
class StackNode:
    data: any
    next = None


class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, data: any):
        node = StackNode(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            raise ValueError("The stack is empty, `pop()` failed")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None


if __name__ == "__main__":
    stack = Stack()
    print("\nPushing data into the Stack...")
    for i in range(5, 10):
        stack.push(i)
        print(f"stack.push({i})")
        print(f"stack.peek() = {stack.peek()}", stack.peek() == i)
        print()

    print("Popping data from the Stack...")
    for i in range(4):
        data = stack.pop()
        print(f"stack.pop() = {data}")
        print(f"stack.peek() = {stack.peek()}", stack.peek() == 9 - i - 1)
        print()
