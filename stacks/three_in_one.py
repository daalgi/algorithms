"""
CRACKING THE CODING INTERVIEW
3.1. Three in One:
Describe how you could use a single array to
implement three stacks.
"""
from dataclasses import dataclass


@dataclass
class FixedMultiStacks:
    num_stacks: int = 3
    stack_size: int = 10

    def __post_init__(self):
        self.values = [None] * self.stack_size * self.num_stacks
        self.lengths = [0, 0, 0]

    def _check_stack_id(self, stack_id: int):
        if stack_id < 0 or stack_id >= self.num_stacks:
            raise ValueError("Invalid stack id")
        return True

    def push(self, stack_id: int, data: any) -> None:
        self._check_stack_id(stack_id)

        index = self.lengths[stack_id] + self.stack_size * stack_id

        if self.lengths[stack_id] >= self.stack_size:
            raise ValueError(f"The stack {stack_id} is full")

        self.values[index] = data
        self.lengths[stack_id] += 1

    def peek(self, stack_id: int):
        self._check_stack_id(stack_id)

        index = self.stack_size * stack_id + self.lengths[stack_id] - 1
        return self.values[index]

    def pop(self, stack_id: int) -> any:
        self._check_stack_id(stack_id)

        if self.lengths[stack_id] == 0:
            raise ValueError(f"The stack {stack_id} is empty")

        index = self.stack_size * stack_id + self.lengths[stack_id] - 1
        data = self.values[index]
        self.values[index] = None
        self.lengths[stack_id] -= 1
        return data

    def is_empty(self, stack_id: int) -> bool:
        self._check_stack_id(stack_id)

        return self.lengths[stack_id] == 0


if __name__ == "__main__":
    stack = FixedMultiStacks(num_stacks=3, stack_size=3)
    print("\nPushing data into the three stacks...")
    stack.push(stack_id=0, data=5)
    print(f"stack.push{0, 5}")
    print("stack.peek(0) =", stack.peek(0), stack.peek(0) == 5)
    stack.push(stack_id=1, data=10)
    print(f"\nstack.push{1, 10}")
    print("stack.peek(1) =", stack.peek(1), stack.peek(1) == 10)
    stack.push(stack_id=2, data=13)
    print(f"\nstack.push{2, 13}")
    print("stack.peek(2) =", stack.peek(2), stack.peek(2) == 13)

    print("\nPushing more data into the three stacks...")
    stack.push(stack_id=0, data=6)
    print(f"stack.push{0, 6}")
    print("stack.peek(0) =", stack.peek(0), stack.peek(0) == 6)
    stack.push(stack_id=0, data=8)
    print(f"\nstack.push{0, 8}")
    print("stack.peek(0) =", stack.peek(0), stack.peek(0) == 8)
    stack.push(stack_id=1, data=11)
    print(f"\nstack.push{1, 11}")
    print("stack.peek(1) =", stack.peek(1), stack.peek(1) == 11)
    stack.push(stack_id=2, data=14)
    print(f"\nstack.push{2, 14}")
    print("stack.peek(2) =", stack.peek(2), stack.peek(2) == 14)

    print("\nPopping data from the three stacks...")
    print("stack.pop(0) =", stack.pop(stack_id=0))
    print("stack.peek(0) =", stack.peek(0), stack.peek(0) == 6)
    print("\nstack.pop(0) =", stack.pop(stack_id=0))
    print("stack.peek(0) =", stack.peek(0), stack.peek(0) == 5)
    print("\nstack.pop(0) =", stack.pop(stack_id=1))
    print("stack.peek(1) =", stack.peek(1), stack.peek(1) == 10)
    print("\nstack.pop(0) =", stack.pop(stack_id=2))
    print("stack.peek(2) =", stack.peek(2), stack.peek(2) == 13)
    print("\nstack.is_empty(0) =", stack.is_empty(0), stack.is_empty(0) is False)
    print("stack.is_empty(1) =", stack.is_empty(1), stack.is_empty(1) is False)
    print("stack.is_empty(2) =", stack.is_empty(2), stack.is_empty(2) is False)

    print("\nPopping data from the three stacks...")
    print("stack.pop(0) =", stack.pop(stack_id=0))
    print("stack.pop(0) =", stack.pop(stack_id=1))
    print("stack.pop(0) =", stack.pop(stack_id=2))
    print("\nstack.is_empty(0) =", stack.is_empty(0), stack.is_empty(0) is True)
    print("stack.is_empty(1) =", stack.is_empty(1), stack.is_empty(1) is True)
    print("stack.is_empty(2) =", stack.is_empty(2), stack.is_empty(2) is True)
    print("\nstack.peek(0) =", stack.peek(0), stack.peek(0) is None)
    print("stack.peek(1) =", stack.peek(1), stack.peek(1) is None)
    print("stack.peek(2) =", stack.peek(2), stack.peek(2) is None)
    print()
