from Classes.Algorithms.BinaryTreeSort import BinaryTreeSort
from Classes.Algorithms.BubbleSort import BubbleSort
from Classes.Algorithms.BucketSort import BucketSort
from Classes.Algorithms.CocktailSort import CocktailSort
from Classes.Algorithms.CombSort import CombSort
from Classes.Algorithms.CountingSort import CountingSort
from Classes.Algorithms.GnomeSort import GnomeSort
from Classes.Algorithms.HeapSort import HeapSort
from Classes.Algorithms.InsertionSort import InsertionSort
from Classes.Algorithms.MargeSort import MergeSort
from Classes.Algorithms.PigeonholeSort import PigeonholeSort
from Classes.Algorithms.QuickSort import QuickSort
from Classes.Algorithms.RadixSort import RadixSort
from Classes.Algorithms.SelectionSort import SelectionSort
from Classes.Algorithms.ShellSort import ShellSort
from Classes.Algorithms.SmoothSort import SmoothSort
from datetime import datetime
import random


class OperationsAlgorithm:
    _rand = random.Random()

    @staticmethod
    def generar_vector_double(minon=0, length=10, values=5):
        arr = [OperationsAlgorithm._rand.random() for _ in range(minon, minon + min(values, length))]
        return arr

    @staticmethod
    def generar_vector(minon=0, length=10, values=5):
        arr = random.sample(range(minon, minon + length), min(values, length))
        return arr

    @staticmethod
    def algorithm(algorithm):
        while True:
            try:
                minon = int(input("Enter the minimum range from which you want to generate your unordered array: "))
                length = int(input("\nEnter the maximum range or limit where you want to generate your unordered array: "))
                values = int(input("\nEnter the number of values you want in your array: "))
            except ValueError:
                OperationsAlgorithm.deffault()
                continue
            if isinstance(algorithm, CountingSort) or isinstance(algorithm, RadixSort) and minon < 0:
                input("Only values greater than or equal to zero are accepted.")
                continue
            if isinstance(algorithm, BucketSort):
                arr = OperationsAlgorithm.generar_vector_double(minon, length, values)
            else:
                arr = OperationsAlgorithm.generar_vector(minon, length, values)

            print("\nUnordered array: ")
            print("[ " + ", ".join(map(str, arr)) + " ]")

            start_time = datetime.now()
            algorithm.sort(arr)
            print("\nSorted array: ")
            print("[ " + ", ".join(map(str, arr)) + " ]")
            print("Time: " + str(datetime.now() - start_time))

            input()
            return

    @staticmethod
    def menu_algorithms():
        while True:
            try:
                print("Select an algorithm:")
                print("1. Binary Tree Sort\n"
                      + "2. Bubble Sort\n"
                      + "3. Bucket Sort\n"
                      + "4. Cocktail Sort\n"
                      + "5. Comb Sort\n"
                      + "6. Counting Sort\n"
                      + "7. Gnome Sort\n"
                      + "8. Heap Sort\n"
                      + "9. Insertion Sort\n"
                      + "10. Merge Sort\n"
                      + "11. Pigeonhole Sort\n"
                      + "12. Quick Sort\n"
                      + "13. Radix Sort\n"
                      + "14. Selection Sort\n"
                      + "15. Shell Sort\n"
                      + "16. Smooth Sort\n"
                      + "0. Exit\n")

                option = int(input())

                if option == 1:
                    OperationsAlgorithm.algorithm(BinaryTreeSort())
                elif option == 2:
                    OperationsAlgorithm.algorithm(BubbleSort())
                elif option == 3:
                    OperationsAlgorithm.algorithm(BucketSort())
                elif option == 4:
                    OperationsAlgorithm.algorithm(CocktailSort())
                elif option == 5:
                    OperationsAlgorithm.algorithm(CombSort())
                elif option == 6:
                    OperationsAlgorithm.algorithm(CountingSort())
                elif option == 7:
                    OperationsAlgorithm.algorithm(GnomeSort())
                elif option == 8:
                    OperationsAlgorithm.algorithm(HeapSort())
                elif option == 9:
                    OperationsAlgorithm.algorithm(InsertionSort())
                elif option == 10:
                    OperationsAlgorithm.algorithm(MergeSort())
                elif option == 11:
                    OperationsAlgorithm.algorithm(PigeonholeSort())
                elif option == 12:
                    OperationsAlgorithm.algorithm(QuickSort())
                elif option == 13:
                    OperationsAlgorithm.algorithm(RadixSort())
                elif option == 14:
                    OperationsAlgorithm.algorithm(SelectionSort())
                elif option == 15:
                    OperationsAlgorithm.algorithm(ShellSort())
                elif option == 16:
                    OperationsAlgorithm.algorithm(SmoothSort())
                elif option == 0:
                    return
                else:
                    OperationsAlgorithm.deffault()
            except ValueError:
                OperationsAlgorithm.deffault()

    @staticmethod
    def deffault():
        print("Invalid input. Please enter a valid number.")
        input()
