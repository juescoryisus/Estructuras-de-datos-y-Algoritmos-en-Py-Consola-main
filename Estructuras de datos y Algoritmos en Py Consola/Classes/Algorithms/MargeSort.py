from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class MergeSort(ImethodAlgorithms):
    def __init__(self):
        self.iterations = 0
        self.recursions = 0

    def sort(self, arr):
        self.iterations = 0  # Reset iterations count
        self.merge_sort(arr, 0)
        print(f'Number of iterations: {self.iterations}')
        print(f'Number of recursions: {self.recursions}')

    def merge_sort(self, arr, depth):
        if len(arr) < 2:
            return

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        self.merge_sort(left, depth + 1)
        self.merge_sort(right, depth + 1)
        self.merge(arr, left, right, depth)

    def merge(self, arr, left, right, depth):
        i = j = k = 0
        self.recursions += 1

        while i < len(left) and j < len(right):
            self.iterations += 1
            print(arr)
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            self.iterations += 1
            print(arr)
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            self.iterations += 1
            print(arr)
            arr[k] = right[j]
            j += 1
            k += 1


