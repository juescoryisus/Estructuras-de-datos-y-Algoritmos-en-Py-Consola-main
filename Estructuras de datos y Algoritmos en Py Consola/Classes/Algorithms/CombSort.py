from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class CombSort(ImethodAlgorithms):
    def __init__(self):
        pass

    def sort(self, arr):
        n = len(arr)

        # Initialize the gap size
        gap = n

        # Reduction factor
        shrink = 1.3

        swapped = False
        iterations = 0
        swaps = 0

        while gap > 1 or swapped:
            # Apply a minimum gap of 1
            if gap > 1:
                gap = int(gap / shrink)

            swapped = False

            # Perform comparisons and swaps
            for i in range(n - gap):
                iterations += 1
                if arr[i] > arr[i + gap]:
                    # Multiple assignment in Python
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    swapped = True
                    swaps += 1
                    print(arr)

        print(f"\nSorting complete. Total iterations: {iterations}, Total swaps: {swaps}")
