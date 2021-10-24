"""
CRACKING THE CODING INTERVIEW
3.2. Stack min:
How would you design a stack which, in addition to push and pop, has
a function min which returns the minimum element?
Push, pip and min should all operate in O(1) time.

Strategy:
In order to achieve O(1) for the push, pop and min methods,
we need to keep track of the minimum of the stack in each state
by means of a list.
- If we push a new value, we compare it the last minimum.
- If we pop the top, we remove the current minimum state 
(remove the last value of the minimum list)
"""
from dataclasses import dataclass


@dataclass
class StackNode:
    data: int
    next = None


class StackMin:
    def __init__(self):
        self.top = None
        self.mins = []

    def push(self, data: int):
        # Store the minimum value for the current state
        if self.top is None:
            self.mins.append(data)
        else:
            self.mins.append(min(self.mins[-1], data))

        # Push the new node to the top
        node = StackNode(data)
        node.next = self.top
        self.top = node

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def pop(self):
        if self.top is None:
            raise ValueError("Stack is empty")

        # Remove the minimum of the current state
        self.mins.pop()

        # Remove the top node of the stack
        data = self.top.data
        self.top = self.top.next

        return data

    def min(self):
        if self.top is None:
            return None
        return self.mins[-1]


if __name__ == "__main__":
    stack = StackMin()

    print("\nPushing values into the stack...")
    for i in range(5, 10):
        stack.push(i)
        print(f"stack.push({i})")
        print(f"stack.min() = {stack.min()}", stack.min() == 5)
        print()

    num = 3
    mini = num
    stack.push(num)
    print(f"stack.push({num})")
    print("stack.min() =", stack.min(), stack.min() == mini)

    num = 2
    mini = num
    stack.push(num)
    print(f"\nstack.push({num})")
    print("stack.min() =", stack.min(), stack.min() == mini)

    num = 4
    stack.push(num)
    print(f"\nstack.push({num})")
    print("stack.min() =", stack.min(), stack.min() == mini)

    print("\nPopping values from the stack...")
    print("stack.pop() =", stack.pop())
    print("stack.min() =", stack.min(), stack.min() == 2)

    print("\nstack.pop() =", stack.pop())
    print("stack.min() =", stack.min(), stack.min() == 3)
    print("\nstack.pop() =", stack.pop())
    print("stack.min() =", stack.min(), stack.min() == 5)
    for i in range(4):
        print("\nstack.pop() =", stack.pop())
        print("stack.min() =", stack.min(), stack.min() == 5)

    print("\nstack.pop() =", stack.pop())
    print("stack.min() =", stack.min(), stack.min() is None)
    print()
