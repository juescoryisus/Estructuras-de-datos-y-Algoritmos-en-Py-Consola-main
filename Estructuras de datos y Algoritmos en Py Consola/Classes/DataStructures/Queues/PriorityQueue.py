from collections import defaultdict


class PriorityQueue:
    def __init__(self):
        self.my_priority_queue = defaultdict(list)

    def enqueue(self, value, priority):
        self.my_priority_queue[priority].append(value)
        print(f"Enqueued with priority {priority}: {value}")

    def dequeue(self):
        if self.my_priority_queue:
            highest_priority = min(self.my_priority_queue.keys())
            value = self.my_priority_queue[highest_priority].pop(0)

            if not self.my_priority_queue[highest_priority]:
                del self.my_priority_queue[highest_priority]

            print(f"Dequeued with priority {highest_priority}: {value}")
            return

        print("Priority Queue is empty. Unable to dequeue.")

    def peek(self):
        if self.my_priority_queue:
            highest_priority = min(self.my_priority_queue.keys())
            value = self.my_priority_queue[highest_priority][0]

            print(f"Front element with priority {highest_priority}: {value}")
            return

        print("Priority Queue is empty. No elements to peek.")

    def display(self):
        print("Priority Queue elements:", end=" ")
        for priority, items in self.my_priority_queue.items():
            for item in items:
                print(f"{item} (Priority {priority})", end=" ")
        print()

    def count(self):
        return sum(len(items) for items in self.my_priority_queue.values())
