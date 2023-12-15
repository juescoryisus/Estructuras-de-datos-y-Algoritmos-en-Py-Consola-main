from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class GnomeSort(ImethodAlgorithms):
    def __init__(self):
        self.iterations = 0
        self.swaps = 0

    def sort(self, arr):
        n = len(arr)
        index = 0

        while index < n:
            if index == 0:
                index += 1
            if arr[index] >= arr[index - 1]:
                index += 1
            else:
                # Python's multiple assignment for swapping
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                index -= 1
                self.iterations += 1
                self.swaps += 1
                print(arr)

        # Print the number of iterations and swaps
        print(f'Number of iterations: {self.iterations}')
        print(f'Number of swaps: {self.swaps}')
