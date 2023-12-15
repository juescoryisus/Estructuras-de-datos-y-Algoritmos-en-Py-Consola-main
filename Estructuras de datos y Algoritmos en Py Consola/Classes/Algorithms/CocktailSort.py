from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms

class CocktailSort(ImethodAlgorithms):
    def __init__(self):
        pass

    def sort(self, arr):
        self.cocktail_sort(arr)

    def cocktail_sort(self, arr):
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1
        swaps = 0
        iterations = 0

        while swapped:
            # Move from left to right
            swapped = False
            for i in range(start, end):
                iterations += 1
                if arr[i] > arr[i + 1]:
                    # Multiple assignment in Python
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
                    swaps += 1
                    print(arr)

            if not swapped:
                break

            end -= 1

            # Move from right to left
            swapped = False
            for i in range(end - 1, start - 1, -1):
                iterations += 1
                if arr[i] > arr[i + 1]:
                    # Multiple assignment in Python
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
                    swaps += 1
                    print(arr)

            start += 1

        print(f"\nSorting complete. Total iterations: {iterations}, Total swaps: {swaps}")
