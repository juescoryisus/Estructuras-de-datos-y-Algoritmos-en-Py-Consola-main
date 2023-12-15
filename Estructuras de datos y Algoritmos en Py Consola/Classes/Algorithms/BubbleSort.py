from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class BubbleSort(ImethodAlgorithms):
    def __init__(self):
        pass

    def sort(self, arr):
        self.bubble_sort(arr)

    def bubble_sort(self, array):
        n = len(array)
        swaps = 0
        iterations = 0

        for i in range(n - 1):
            for j in range(n - i - 1):
                iterations += 1
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swaps += 1
                    print(array)

        print(f"Total iterations: {iterations}\nTotal swaps: {swaps}")
