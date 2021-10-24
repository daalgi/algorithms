"""
CRACKING THE CODING INTERVIEW
3.6. Animal Shelter:
An animal shelter, which holds only cats and dogs, operates on a strictly
"first in, first out" basis. People must adopt either the "oldest" (based
on arrival time) of all the animals at the shelter, or they can select
whether they would prefer a dog or a cat (and will receie the oldest
animal of that type). They cannot select whihch specific animal they
would like. Create the data structures to maintain this system and
implement operations such as `enqueue`, `dequeue_any`, `dequeue_dog`,
and `dequeue_cat`.
"""
from dataclasses import dataclass


class Animal:
    cat = "cat"
    dog = "dog"


@dataclass
class Node:
    data: str
    next = None


class AnimalShelterQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self, data: str):
        node = Node(data)

        # Add the new node at the tail
        # of the LinkedList or Queue
        if self.tail is None:
            # If it's the first node,
            # add it to the `tail`
            self.tail = node
        else:
            # If it's not the first node,
            # added after the `tail`
            self.tail.next = node
            self.tail = node

        # If it's the first node, it'll
        # be the `head` as well
        if self.head is None:
            self.head = self.tail

    def peek(self) -> str:
        if self.head is None:
            return None

        return self.head.data

    def dequeue_any(self):
        if self.head is None:
            raise ValueError("The shelter has no animals currently")

        animal = self.head.data
        self.head = self.head.next
        return animal

    def dequeue_animal(self, animal: str):
        # If the queue is empty, raise error
        if self.head is None:
            raise ValueError("The shelter has no animals currently")

        # If the head contains the searched `animal`,
        # update the `head` reference and return the animal
        if self.head.data == animal:
            self.head = self.head.next
            return animal

        # Loop over the queue to find the given `animal`
        # cur initialized as a dummy node
        cur = self.head
        while cur.next and cur.next.data != animal:
            cur = cur.next

        # If the loop ended because there's no more nodes
        if cur.next is None:
            raise ValueError(f"The shelter has no {animal}s currently")

        # Update node `next` references
        if cur.next.next:
            # If it's a middle node
            cur.next = cur.next.next
        else:
            # If it's the tail
            cur.next = None

        # Return the animal
        return animal

    def dequeue_dog(self):
        return self.dequeue_animal(animal=Animal.dog)

    def dequeue_cat(self):
        return self.dequeue_animal(animal=Animal.cat)

    def nodes_to_list(self):
        res = []
        cur = self.head
        while cur:
            res.append(cur.data)
            cur = cur.next

        return res


if __name__ == "__main__":
    print("-" * 60)
    print("ANIMAL SHELTER QUEUE")
    print("-" * 60)

    queue = AnimalShelterQueue()
    print("\nEnqueueing into AnimalShelterQueue...")
    for i in range(5):
        animal = Animal.dog if i & 1 else Animal.cat
        queue.enqueue(animal)
        print(f"queue.enqueue({animal})")
        print(f"stack.peek() = {queue.peek()}", queue.peek() == Animal.cat)
        print()

    print("Shelter queue:", " -> ".join(queue.nodes_to_list()))

    print("\nDequeueing any animals...")
    for i in range(5):
        expected = Animal.dog if i & 1 else Animal.cat
        animal = queue.dequeue_any()
        print(f"queue.dequeue_any() = {animal}", animal == expected)
        print()

    print("\nEnqueueing into AnimalShelterQueue...")
    for i in range(8):
        animal = Animal.dog if i & 1 else Animal.cat
        queue.enqueue(animal)
    print("Shelter queue:", " -> ".join(queue.nodes_to_list()))

    print("\nDequeueing only dogs...")
    for i in range(3):
        queue.dequeue_dog()
        print("Shelter queue:", " -> ".join(queue.nodes_to_list()))
        print()

    print("\nDequeueing only cats...")
    for i in range(4):
        queue.dequeue_cat()
        print("Shelter queue:", " -> ".join(queue.nodes_to_list()))
        print()
