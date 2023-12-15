from Interfaces.DataStructures.ImethodLists import ImethodLists
from Classes.DataStructures.Nodes.DoubleNode import DoubleNode

class DoublyCircleLinkedList(ImethodLists):

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = DoubleNode(data)

        # Case 1: The list is empty
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.head.back = self.tail
            self.tail.next = self.head
            return

        # Case 2: The data already exists
        if self.exist(data):
            print(f"- [{data}] already exists in the list")
            return

        # Case 3: Head has data less than that of the new node.
        if self.head.data > new_node.data:
            new_node.next = self.head
            new_node.back = self.tail
            self.head.back = new_node
            self.tail.next = new_node
            self.head = new_node
            return

        # Case 4: The node to add goes after the Tail
        if new_node.data > self.tail.data:
            new_node.next = self.head
            new_node.back = self.tail
            self.tail.next = new_node
            self.head.back = new_node
            self.tail = new_node
            return

        # Case 5: The data is less than one of the nodes in the list
        current_node = self.head
        while current_node.next is not self.tail and current_node.next.data < new_node.data:
            current_node = current_node.next

        new_node.back = current_node
        new_node.next = current_node.next
        current_node.next.back = new_node
        current_node.next = new_node

    def remove(self, data):
        # Case 1: List is empty
        if self.is_empty():
            print("// The list is empty")
            return

        # Case 2: The head has the courage to remove
        if self.head.data == data:
            self.head = self.head.next
            self.head.back = self.tail
            self.tail.next = self.head
            print(f"- Data[{data}] has been removed from the list")
            return

        # Case 3: When the data to be removed is the tail of the list
        if self.tail.data == data:
            self.tail = self.tail.back
            self.tail.next = self.head
            self.head.back = self.tail
            print(f"- Data[{data}] has been removed from the list")
            return

        # Case 4: Any of the following nodes has the data to be removed
        current_node = self.head
        while current_node.next is not self.head and current_node.data < data:
            current_node = current_node.next

        # Case 5: When the data to be removed is not the tail of the list
        if current_node.data == data:
            current_node.next.back = current_node.back
            current_node.back.next = current_node.next
            print(f"- Data[{data}] has been removed from the list")
            return

        # Case 6: When we reached the end of the list and it was not found
        print(f"- Data[{data}] does not exist in the list")

    def exist(self, data):
        # Case 1: List is empty
        if self.is_empty():
            print("// The list is empty")
            return False

        # Case 2: The 'head' node contains the data
        if self.head.data == data:
            return True

        # Case 3: The 'tail' node contains the data
        if self.tail.data == data:
            return True

        # Case 4: Any node in the list can have the data
        current_node = self.head
        while current_node.next is not self.head and current_node.next.data <= data:
            current_node = current_node.next

        # Case 5: The data already exists in the list
        if current_node.data == data:
            return True

        # Case 6: We reached the end and found nothing
        return False

    def search(self, data):
        # Case 1: List is empty
        if self.is_empty():
            print("// The list is empty")
            return

        # Case 2: The 'head' node contains the data
        if self.head.data == data:
            print(f"- Data[{data}] exists in the list")
            return

        # Case 3: The 'tail' node contains the data
        if self.tail.data == data:
            print(f"- Data[{data}] exists in the list")
            return

        # Case 4: Any node in the list can have the data
        current_node = self.head
        while current_node.next is not self.head and current_node.next.data <= data:
            current_node = current_node.next

        # Case 5: The data already exists in the list
        if current_node.data == data:
            print(f"- Data[{data}] exists in the list")
            return

        # Case 6: We reached the end and found nothing
        print(f"- Data[{data}] does not exist in the list")

    def show(self):
        # Case 1: List is empty
        if self.is_empty():
            print("// The list is empty")
            return

        # Case 2: List is not empty or is not None
        print("=== My Doubly Circular Linked List ===")
        i = 0
        current_node = self.head
        while True:
            print(f"- Node[{i}] and data: {current_node.data}")
            current_node = current_node.next
            i += 1
            if current_node is self.head:
                break

    def show_reverse(self):
        # Case 1: List is empty
        if self.is_empty():
            print("// The list is empty")
            return

        # Case 2: List is not empty or is not None
        print("=== My Reversed Doubly Circular Linked List ===")
        i = 0
        current_node = self.tail
        while True:
            print(f"- Node[{i}] and data: {current_node.data}")
            current_node = current_node.back
            i += 1
            if current_node is self.tail:
                break

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None
        self.tail = None
