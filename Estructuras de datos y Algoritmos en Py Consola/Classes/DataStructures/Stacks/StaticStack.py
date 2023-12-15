from Interfaces.DataStructures.ImethodStacks import ImethodStacks


class StaticStack(ImethodStacks):
    def __init__(self, capacity):
        self.capacity = capacity
        self.elements = [None] * capacity
        self.count = 0

    def push(self, element):
        if self.count < self.capacity:
            self.elements[self.count] = element
            self.count += 1
        else:
            print("The stack is full. Cannot add more elements.")

    def pop(self):
        if self.count > 0:
            self.count -= 1
            return self.elements[self.count]
        else:
            print("The stack is empty. Cannot pop more elements.")
            return None

    def peek(self):
        if self.count > 0:
            return self.elements[self.count - 1]
        else:
            print("The stack is empty. No elements to peek.")
            return None

    def count(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def show(self):
        if self.is_empty():
            print("The stack is empty.")
        else:
            print("\nElements in the stack:")
            for i in range(self.count - 1, -1, -1):
                print(self.elements[i])
