from Classes.DataStructures.Queues.RegularQueue import RegularQueue
from Classes.DataStructures.Queues.DoubleQueue import DoubleQueue
from Classes.DataStructures.Queues.PriorityQueue import PriorityQueue
from Classes.DataStructures.Queues.CircularQueue import CircularQueue


class OperationsQueue:
    @staticmethod
    def all_queue_operations(queue):
        queue_type_message = (
            "Regular" if isinstance(queue, RegularQueue)
            else "Double" if isinstance(queue, DoubleQueue)
            else "Priority" if isinstance(queue, PriorityQueue)
            else "Circle"
        )
        operation_circular_queue = isinstance(queue, CircularQueue)

        while True:
            OperationsQueue.clear_console()
            print(f"{queue_type_message} queue \n"
                  + "1. Enqueue value \n"
                  + "2. Dequeue value \n"
                  + "3. Peek value\n"
                  + "4. Display \n"
                  + "0. Exit \n")

            try:
                choice = int(input())
            except ValueError:
                OperationsQueue.default()
                continue

            if choice == 1:
                if operation_circular_queue:
                    print("What type of enqueue do you want to perform?"
                          + "\n1. Enqueue simple"
                          + "\n2. Enqueue rear")

                    try:
                        option = int(input())
                    except ValueError:
                        OperationsQueue.default()
                        continue

                    if option == 2:
                        try:
                            queue.enqueue_rear(input("Enter a value to enqueue at the rear:"))
                        except ValueError:
                            OperationsQueue.default()
                        continue

                    if option != 1:
                        OperationsQueue.default()
                        continue

                try:
                    queue.enqueue(input("Enter a value to enqueue:"))
                except ValueError:
                    OperationsQueue.default()

            elif choice == 2:
                if operation_circular_queue:
                    print("What type of 'Dequeue' do you want to perform?"
                          + "\n1. Dequeue simple"
                          + "\n2. Dequeue rear")

                    try:
                        option = int(input())
                    except ValueError:
                        OperationsQueue.default()
                        continue

                    if option == 2:
                        queue.dequeue_rear()
                        continue

                    if option != 1:
                        OperationsQueue.default()
                        continue

                queue.dequeue()

            elif choice == 3:
                if operation_circular_queue:
                    print("What type of 'Peek' do you want to perform?"
                          + "\n1. Peek simple"
                          + "\n2. Peek rear")

                    try:
                        option = int(input())
                    except ValueError:
                        OperationsQueue.default()
                        continue

                    if option == 2:
                        queue.peek_rear()
                        continue

                    if option != 1:
                        OperationsQueue.default()
                        continue

                queue.peek()

            elif choice == 4:
                queue.display()

            elif choice == 0:
                return

            else:
                OperationsQueue.default()

            input("Press Enter to continue...")

    @staticmethod
    def menu_queue():
        while True:
            OperationsQueue.clear_console()
            print("Types of queues: \n"
                  + "1. Regular queue \n"
                  + "2. Doubly queue \n"
                  + "3. Priority queue \n"
                  + "4. Circular queue \n"
                  + "0. Exit \n")

            try:
                opt = int(input())
            except ValueError:
                OperationsQueue.default()
                continue

            if opt == 1:
                OperationsQueue.all_queue_operations(RegularQueue())
            elif opt == 2:
                OperationsQueue.all_queue_operations(DoubleQueue())
            elif opt == 3:
                OperationsQueue.all_queue_operations(PriorityQueue())
            elif opt == 4:
                try:
                    print("How large do you want your Queue to be?")
                    length = int(input())
                except ValueError:
                    OperationsQueue.default()
                    continue

                OperationsQueue.all_queue_operations(CircularQueue(length))
            elif opt == 0:
                return
            else:
                OperationsQueue.default()

    @staticmethod
    def default():
        print("Invalid input. Please enter a valid number.")
        input("Press Enter to continue...")

    @staticmethod
    def clear_console():
        # Implementar esto según tu plataforma, por ejemplo:
        # import os
        # os.system('cls' if os.name == 'nt' else 'clear')
        pass

    @staticmethod
    def convert_input_to_type(input_value, queue):
        try:
            return queue.convert_input_to_type(input_value)
        except ValueError:
            raise ValueError("Could not convert input to the required type.")
