from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class RadixSort(ImethodAlgorithms):
    def __init__(self):
        self.iterations = 0
        pass

    def sort(self, arr):
        max_value = self.find_max(arr)

        # Apply Radix Sort for each digit position
        exp = 1
        while max_value // exp > 0:
            self.iterations += 1
            self.counting_sort(arr, exp)
            exp *= 10
            print(arr)

        print(f'Number of iterations: {self.iterations}')

    def counting_sort(self, arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        # Initialize the count array
        for i in range(10):
            self.iterations += 1
            count[i] = 0

        # Count the frequency of each element at the current digit position
        for i in range(n):
            self.iterations += 1
            count[(arr[i] // exp) % 10] += 1

        # Update the count array to contain the actual positions
        for i in range(1, 10):
            self.iterations += 1
            count[i] += count[i - 1]

        # Build the output array
        i = n - 1
        while i >= 0:
            self.iterations += 1
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1
            print(arr)

        # Copy the output array back to the original array
        for i in range(n):
            arr[i] = output[i]

    def find_max(self, arr):
        max_value = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max_value:
                max_value = arr[i]
        return max_value
