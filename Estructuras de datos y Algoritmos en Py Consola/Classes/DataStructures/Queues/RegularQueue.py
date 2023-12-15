from collections import deque


class RegularQueue:
    def __init__(self):
        self.my_queue = deque()

    def enqueue(self, value):
        self.my_queue.append(value)
        print(f"Enqueued: {value}")

    def dequeue(self):
        if self.my_queue:
            value = self.my_queue.popleft()
            print(f"Dequeued: {value}")
        else:
            print("Queue is empty. Unable to dequeue.")

    def peek(self):
        if self.my_queue:
            front_value = self.my_queue[0]
            print(f"Front element: {front_value}")
        else:
            print("Queue is empty. No elements to peek.")

    def display(self):
        print("Queue elements:", end=" ")
        for item in self.my_queue:
            print(item, end=" ")
        print()

    def count(self):
        return len(self.my_queue)
