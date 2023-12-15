from collections import deque
from typing import Optional, Generator


class DoubleQueue:
    def __init__(self):
        self.my_deque = deque()

    def enqueue(self, value: Optional):
        self.my_deque.appendleft(value)
        print(f"Enqueued at the front: {value}")

    def enqueue_rear(self, value: Optional):
        self.my_deque.append(value)
        print(f"Enqueued at the rear: {value}")

    def dequeue(self):
        if self.my_deque:
            value = self.my_deque.popleft()
            print(f"Dequeued from the front: {value}")
            return
        print("Deque is empty. Unable to dequeue from the front.")

    def dequeue_rear(self):
        if self.my_deque:
            value = self.my_deque.pop()
            print(f"Dequeued from the rear: {value}")
            return
        print("Deque is empty. Unable to dequeue from the rear.")

    def peek(self):
        if self.my_deque:
            front_value = self.my_deque[0]
            print(f"Front element: {front_value}")
            return
        print("Deque is empty. No elements at the front to peek.")

    def peek_rear(self):
        if self.my_deque:
            rear_value = self.my_deque[-1]
            print(f"Rear element: {rear_value}")
            return
        print("Deque is empty. No elements at the rear to peek.")

    def display(self) -> Generator[str, None, None]:
        print("Deque elements: ", end="")
        for item in self.my_deque:
            yield str(item)
            print(f"{item} ", end="")
        print()

    def count(self):
        return len(self.my_deque)
