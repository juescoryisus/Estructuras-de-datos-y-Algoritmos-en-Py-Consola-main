from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class HeapSort(ImethodAlgorithms):
    def __init__(self):
        self.iterations = 0
        self.swaps = 0

    def sort(self, arr):
        n = len(arr)

        # Build a max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Extract elements one by one from the heap
        for i in range(n - 1, 0, -1):
            # Swap the root (max element) with the last element
            arr[0], arr[i] = arr[i], arr[0]
            self.swaps += 1
            self.iterations += 1
            print(arr)

            # Call heapify on the reduced heap
            self.heapify(arr, i, 0)

        # Print the number of iterations and swaps
        print(f'Number of iterations: {self.iterations}')
        print(f'Number of swaps: {self.swaps}')

    @staticmethod
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Compare with the left child
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Compare with the right child
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If the largest is not the root
        if largest != i:
            # Python's multiple assignment for swapping
            arr[i], arr[largest] = arr[largest], arr[i]

            # Recursively heapify the affected subtree
            HeapSort.heapify(arr, n, largest)
