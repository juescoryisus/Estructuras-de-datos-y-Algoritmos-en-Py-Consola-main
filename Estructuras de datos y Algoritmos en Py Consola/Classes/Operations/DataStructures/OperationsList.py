from Classes.DataStructures.Lists.LinkedList import SimpleList
from Classes.DataStructures.Lists.Circle_LinkedList import CircleLinkedList
from Classes.DataStructures.Lists.Doubly_LinkedList import DoublyLinkedList
from Classes.DataStructures.Lists.DoublyCircle_LinkedList import DoublyCircleLinkedList
import random


class OptionLists:
    Add = 1
    Delete = 2
    Search = 3
    Show = 4
    ShowRevers = 5
    Clear = 6


class OperationsList:
    r = random.Random()

    def __int__(self):
        self.menu_list()

    @staticmethod
    def add_elements(elements_to_add, custom_list):
        for element in elements_to_add:
            custom_list.add(element)

    @staticmethod
    def data_numeric():
        cant = int(input("How many data do you want to add: "))
        minon = int(input("Enter the minimum value for selecting data (default is 0): ") or 0)
        print(f"Selected value: {minon}")

        length = int(input("Enter the maximum value for selecting data (default is 100): ") or 100)
        print(f"Selected value: {length}")

        if minon > length:
            print("Error: The minimum value cannot be greater than the maximum value. Using default values.")
            minon = 0
            length = 100

        if cant > (length - minon + 1):
            print("Error: The number of data requested exceeds the available range. Using the available range.")
            cant = length - minon + 1

        data = [random.randint(minon, length) for _ in range(cant)]
        return data

    @staticmethod
    def a_list_operation(custom_list):
        list_type_message = (
            "Simple" if isinstance(custom_list, SimpleList) else
            "Circular" if isinstance(custom_list, CircleLinkedList) else
            "Doubly" if isinstance(custom_list, DoublyLinkedList) else
            "Doubly circle"
        )

        while True:
            print(f"{list_type_message} list \n"
                  + "1. Add value \n"
                  + "2. Delete value \n"
                  + "3. Search value \n"
                  + "4. Show list \n"
                  + "5. Show reverse \n"
                  + "6. Clear \n"
                  + "0. Exit \n")

            opti = int(input() or 0)

            if opti == OptionLists.Add:
                print("Do you want to add data randomly? \n"
                    + "1. Yes \n"
                    + "2. No \n")
                optio_ = int(input() or 0)

                if optio_ == 1:
                    OperationsList.add_elements(OperationsList.data_numeric(), custom_list)
                    continue
                elif optio_ == 2:
                    print("Enter a value: ")
                    custom_list.add(input())
                    continue

            elif opti == OptionLists.Delete:
                print("Do you want to delete data randomly (only numbers)? \n"
                    + "1. Yes \n"
                    + "2. No \n")
                optio = int(input() or 0)

                if optio == 1:
                    custom_list.delete(OperationsList.data_numeric())
                    continue
                elif optio == 2:
                    print("Enter a value to delete: ")
                    custom_list.delete(input())
                    continue

            elif opti == OptionLists.Search:
                print("Enter a value to search: ")
                custom_list.search(input("Enter your choice: "))
                continue

            elif opti == OptionLists.Show:
                custom_list.show()
                continue

            elif opti == OptionLists.ShowRevers:
                custom_list.show_reverse()
                continue

            elif opti == OptionLists.Clear:
                custom_list.clear()
                continue

            elif opti == 0:
                return

    @staticmethod
    def menu_list():
        while True:
            print("Types of lists: \n"
                  + "1. Simple \n"
                  + "2. Circular \n"
                  + "3. Doubly linked \n"
                  + "4. Circular Doubly linked \n"
                  + "0. Exit \n")

            opt = int(input() or 0)

            if opt == 1:
                OperationsList.a_list_operation(SimpleList())
            elif opt == 2:
                OperationsList.a_list_operation(CircleLinkedList())
            elif opt == 3:
                OperationsList.a_list_operation(DoublyLinkedList())
            elif opt == 4:
                OperationsList.a_list_operation(DoublyCircleLinkedList())
            elif opt == 0:
                return
            else:
                OperationsList.deffault()

    @staticmethod
    def deffault():
        input("Invalid input. Please enter a valid number.")
