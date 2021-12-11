"""
CRACKING THE CODING INTERVIEW
8.6 Towers of Hanoi:
In the classic problem of the Towers of Hanoi, you have 3
towers and N disks of different sizes which can slide onto 
any tower. The puzzle starts with disks sorted in ascending order
of size from top to bottom (i.e., each disk sits on top of an
even larger one). You have the following constraints:

1 - Only one disk can be moved at a time.
2 - A disk is slid off the top of one tower onto another tower.
3 - A disk cannot be placed on top of a smaller disk.

Write a program to move the disks from the first tower to the
last using Stacks.
"""


def recursion(disks: int) -> int:
    # Time complexity: O(2^n - 1) = O(2^n)

    # Towers:
    # A: origin, B: auxiliary, C: target
    A, B, C = [i for i in range(disks, 0, -1)], [], []

    def move(n: int, source, target, auxiliary) -> None:
        if n > 0:
            # Move n - 1 disks from source to auxiliary,
            # so they are out of the way
            move(n - 1, source, auxiliary, target)

            # Move the nth disk from source to target
            target.append(source.pop())

            # Display the current progress
            print(A, B, C, sep="\n")
            print()

            # Move the n - 1 disks that we left on auxiliary
            # onto target
            move(n - 1, auxiliary, target, source)

    print("Initial state:")
    print(A, B, C, sep="\n")
    print("\nIterations:")    
    move(disks, A, C, B)


if __name__ == "__main__":
    print("-" * 60)
    print("Towers of Hanoi")
    print("-" * 60)

    test_cases = [2, 3]

    for disks in test_cases:

        print(f">>> recursion({disks})")
        recursion(disks)
        print()
