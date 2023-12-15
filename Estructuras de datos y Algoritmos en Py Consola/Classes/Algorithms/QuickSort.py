from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms
import random


class QuickSort(ImethodAlgorithms):
    def __init__(self):
        self._random = random.Random()
        self._option = 0
        self._contain_exchange = 0
        self._contain_partition = 0
        self._contain_recursive = 0

    def sort(self, arr):
        self.quicksort(arr, 0, len(arr) - 1)

    def swap(self, arr, index_one, index_two):
        arr[index_one], arr[index_two] = arr[index_two], arr[index_one]

    def partition(self, array, first_index, last_index):
        self._contain_partition += 1
        index_pivot = 0
        if self._option == 1:
            index_pivot = first_index
        elif self._option == 2:
            index_pivot = (last_index + first_index) // 2
        elif self._option == 3:
            index_pivot = last_index
        else:
            index_pivot = self._random.randint(first_index, last_index)

        self.swap(array, first_index, index_pivot)

        self.print_swap(array, first_index, index_pivot)
        self._contain_exchange += 1

        pivot = array[first_index]
        left = first_index + 1
        right = last_index

        while True:
            while left <= right and array[left] <= pivot:
                left += 1
            while left <= right and array[right] >= pivot:
                right -= 1
            if right < left:
                break
            self.swap(array, left, right)
            self.print_swap(array, left, right)
            self._contain_exchange += 1
            left += 1
            right -= 1

        self.swap(array, first_index, right)
        self.print_swap(array, first_index, right)
        self._contain_exchange += 1
        return right

    def quicksort(self, array, first_index, last_index):
        if first_index < last_index:
            self._contain_recursive += 1
            index_pivot = self.partition(array, first_index, last_index)
            self.quicksort(array, first_index, index_pivot - 1)
            self.quicksort(array, index_pivot + 1, last_index)

    def print_result(self, arr):
        self.quicksort(arr, 0, len(arr) - 1)
        print("\nResult: [ " + ", ".join(map(str, arr)) + " ]")
        print("Swaps: " + str(self._contain_exchange) + "\nPartitions: " + str(self._contain_partition) +
              "\nRecursion: " + str(self._contain_recursive))
        self._contain_exchange = 0
        self._contain_partition = 0
        self._contain_recursive = 0

    def print_swap(self, array, left, right):
        print("[ ", end="")
        for i in range(len(array)):
            if right == i == left:
                print(f"\033[93m{array[i]}\033[0m", end="")
            elif i == left or i == right:
                print(f"\033[91m{array[i]}\033[0m", end="")
            else:
                print(array[i], end="")
            if i < len(array) - 1:
                print(", ", end="")
        print(" ]")
