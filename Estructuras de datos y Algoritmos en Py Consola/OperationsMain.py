from Classes.Operations.DataStructures.OperationsList import OperationsList
from Classes.Operations.DataStructures.OperationsStack import OperationsStack
from Classes.Operations.DataStructures.OperationsQueue import OperationsQueue
from Classes.Operations.DataStructures.OperationsGraph import OperationsGraph
from Classes.Operations.DataStructures.OperationsTree import OperationsTree
from Classes.Operations.Algorithms.OperationsAlgorithm import OperationsAlgorithm


class OperationMain:

    @staticmethod
    def menu_DataStructures():
        while True:
            print("Select a data structure:")
            print("1. Lists \n"
                  + "2. Stacks \n"
                  + "3. Queue \n"
                  + "4. Trees \n"
                  + "5. Graphs \n"
                  + "0. Exit \n")

            try:
                option = int(input())
            except ValueError:
                OperationsList.deffault()
                continue

            if option == 1:
                OperationsList.menu_list()
            elif option == 2:
                OperationsStack.menu_stack()
            elif option == 3:
                OperationsQueue.menu_queue()
            elif option == 4:
                OperationsTree.tree_menu()
            elif option == 5:
                OperationsGraph.menu_graphs()
            elif option == 0:
                break
            else:
                OperationsList.deffault()

    @staticmethod
    def main_ds():
        while True:
            print("Select a data structure or algorithm:")
            print("1. Algorithms\n"
                  + "2. Data Structures\n"
                  + "0. Exit\n")

            num = input("Enter your choice: ")

            try:
                num = int(num)
            except ValueError:
                OperationsAlgorithm.deffault()
                continue

            if num == 1:
                OperationsAlgorithm.menu_algorithms()
            elif num == 2:
                OperationMain.menu_DataStructures()
            elif num == 0:
                return

    @staticmethod
    def deffault():
        input("Invalid input. Please enter a valid number.")
