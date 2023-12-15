from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class InsertionSort(ImethodAlgorithms):
    def __init__(self):
        self.iterations = 0
        self.swaps = 0

    def sort(self, arr):
        self.insertion_sort_algorithm(arr)

    def insertion_sort_algorithm(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1

            # Move elements of arr[0.i-1] that are greater than key
            # to one position ahead of their current position
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j = j - 1
                self.swaps += 1
                self.iterations += 1
                print(arr)

            arr[j + 1] = key

        # Print the number of iterations and swaps
        print(f'Number of iterations: {self.iterations}')
        print(f'Number of swaps: {self.swaps}')
