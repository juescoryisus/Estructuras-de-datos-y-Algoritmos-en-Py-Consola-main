from Classes.DataStructures.Stacks.StaticStack import StaticStack
from Classes.DataStructures.Stacks.DynamicStack import DynamicStack


class OperationsStack:
    @staticmethod
    def all_stack_operations(stack):
        stack_type_message = "Dynamic stack" if isinstance(stack, DynamicStack) else "Static stack"

        while True:
            OperationsStack.clear_console()
            print(f"{stack_type_message} Menu \n"
                  + "1. Push \n"
                  + "2. Pop \n"
                  + "3. Peek \n"
                  + "4. Count \n"
                  + "5. Show Stack \n"
                  + "0. Exit \n")

            try:
                option = int(input())
            except ValueError:
                OperationsStack.default()
                continue

            if option == 1:
                value_input = input("\nEnter a value: ")
                stack.push(value_input)
            elif option == 2:
                try:
                    popped_element = stack.pop()
                    print(f"Element '{popped_element}' removed from the stack.")
                except IndexError:
                    print("The stack is empty. Cannot pop more elements.")
            elif option == 3:
                try:
                    top_element = stack.peek()
                    print(f"Element '{top_element}' is at the top of the stack.")
                except IndexError:
                    print("The stack is empty. No elements to peek.")
            elif option == 4:
                print(f"Number of elements in the stack: {stack.count}")
            elif option == 5:
                stack.show()
            elif option == 0:
                return
            else:
                OperationsStack.default()

            input("Press Enter to continue...")

    @staticmethod
    def menu_stack():
        while True:
            OperationsStack.clear_console()
            print("Types of stacks: \n"
                  + "1. Static stack \n"
                  + "2. Dynamic stack \n"
                  + "0. Exit \n")

            try:
                option = int(input())
            except ValueError:
                OperationsStack.default()
                continue

            if option == 1:
                try:
                    cant = int(input("How many data do you want to store in the static stack? "))
                except ValueError:
                    OperationsStack.default()
                    continue

                # Crea una pila estática sin especificar el tipo de datos
                OperationsStack.all_stack_operations(StaticStack(cant))
            elif option == 2:
                stack = DynamicStack()
                OperationsStack.all_stack_operations(stack)
            elif option == 0:
                return
            else:
                OperationsStack.default()

    @staticmethod
    def default():
        print("\nInvalid input. Please enter a valid number.")
        input()

    @staticmethod
    def clear_console():
        # Limpiar la consola en función del sistema operativo
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
