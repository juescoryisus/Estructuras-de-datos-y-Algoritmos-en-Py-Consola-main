from Interfaces.DataStructures.ImethodStacks import ImethodStacks


class DynamicStack(ImethodStacks):
    def __init__(self):
        self.stack_list = []

    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        if not self.stack_list:
            raise ValueError("The stack is empty.")

        return self.stack_list.pop()

    def peek(self):
        if not self.stack_list:
            raise ValueError("The stack is empty.")

        return self.stack_list[-1]

    def count(self):
        return len(self.stack_list)

    def show(self):
        print("\nElements in the stack:")
        for item in reversed(self.stack_list):
            print(item)
