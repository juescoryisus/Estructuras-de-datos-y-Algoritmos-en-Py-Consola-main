from typing import Optional, Generator
from itertools import cycle


class CircularQueue:
    def __init__(self, size):
        self.capacity = size
        self.my_circular_queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value: Optional):
        if self.is_empty():
            self.front = self.rear = 0
            self.my_circular_queue[self.rear] = value
            print(f"Enqueued: {value}")
            return

        if (self.rear + 1) % self.capacity == self.front:
            print("Circular Queue is full. Unable to enqueue.")
            return

        self.rear = (self.rear + 1) % self.capacity
        self.my_circular_queue[self.rear] = value
        print(f"Enqueued: {value}")

    def dequeue(self):
        if self.is_empty():
            print("Circular Queue is empty. Unable to dequeue.")
            return

        if self.front == self.rear:
            print(f"Dequeued: {self.my_circular_queue[self.front]}")
            self.front = self.rear = -1
            return

        print(f"Dequeued: {self.my_circular_queue[self.front]}")
        self.front = (self.front + 1) % self.capacity

    def peek(self):
        if self.is_empty():
            print("Circular Queue is empty. No elements to peek.")
            return

        print(f"Front element: {self.my_circular_queue[self.front]}")

    def display(self) -> Generator[str, None, None]:
        if self.is_empty():
            print("Circular Queue is empty.")
            return

        print("Circular Queue elements:", end=" ")
        for i in cycle(range(self.front, self.rear + 1)):
            yield str(self.my_circular_queue[i])
            print(f"{self.my_circular_queue[i]} ", end="")
            if i == self.rear:
                break
        print()

    def count(self):
        if self.is_empty():
            return 0

        if self.front <= self.rear:
            return self.rear - self.front + 1

        return self.capacity - self.front + self.rear + 1

    def is_empty(self):
        return self.front == -1 and self.rear == -1
