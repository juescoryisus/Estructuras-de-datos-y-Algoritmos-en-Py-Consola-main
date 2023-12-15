from Classes.DataStructures.Tree.BinaryTree import BinaryTree


class OperationsTree:
    @staticmethod
    def tree_menu():
        tree = BinaryTree()

        while True:
            print("Binary Tree \n"
                  + "1. Add node\n"
                  + "2. Search node\n"
                  + "3. Delete node\n"
                  + "4. Display tree\n"
                  + "5. PreOrder Traversal\n"
                  + "6. PostOrder Traversal\n"
                  + "7. InOrder Traversal\n"
                  + "0. Exit\n")

            try:
                choice = int(input())
            except ValueError:
                OperationsTree.default()
                continue

            if choice == 0:
                return

            if choice == 1:
                try:
                    value = int(input("Enter a value: "))
                    tree.add(value)
                except ValueError:
                    OperationsTree.default()
                    continue
            elif choice == 2:
                try:
                    value_to_search = int(input("Enter the value of the node to search: "))
                    tree.search(value_to_search)
                except ValueError:
                    OperationsTree.default()
                    continue
            elif choice == 3:
                try:
                    value_to_delete = int(input("Enter the value of the node to delete: "))
                    tree.delete(value_to_delete)
                except ValueError:
                    OperationsTree.default()
                    continue
            elif choice == 4:
                print("\nDisplay tree:")
                tree.print_tree()
                input("Press Enter to exit")
            elif choice == 5:
                print("\nPreOrder Traversal:", " ".join(map(str, tree.get_pre_order())))
            elif choice == 6:
                print("\nPostOrder Traversal:", " ".join(map(str, tree.get_post_order())))
            elif choice == 7:
                print("\nInOrder Traversal:", " ".join(map(str, tree.get_in_order())))
            else:
                OperationsTree.default()

    @staticmethod
    def default():
        print("\nInvalid input. Please enter a valid number.")
        input("Press Enter to continue")
