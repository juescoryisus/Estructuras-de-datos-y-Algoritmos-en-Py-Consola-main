class ShellSort:
    def __init__(self):
        pass

    def sort(self, arr):
        self.shell_sort(arr)

    def shell_sort(self, array):
        # Get the length of the array
        n = len(array)
        # Get the initial gap size
        gap = n // 2

        print("\nStart of Shell Sort algorithm:")

        # While the gap between elements is greater than 0
        while gap > 0:
            print(f"\nCurrent Gap: {gap}")

            # Apply the insertion sort algorithm for each subarray with the current gap size
            for i in range(gap, n):
                # Save the current element's value in a temporary variable
                temp = array[i]
                j = i

                print(f"\nComparing {temp} with elements in its subarray:")

                # Perform the insertion
                while j >= gap and array[j - gap] > temp:
                    # Shift elements to the right until finding the correct position
                    array[j] = array[j - gap]
                    j -= gap

                    self.print_array(array)

                # Place the temporary value in the correct position in the subarray
                array[j] = temp
                print(f"Insert {temp} at position {j} in the subarray:")
                self.print_array(array)

            # Reduce the gap between elements by half in each iteration
            gap //= 2

        print("\nEnd of Shell Sort algorithm:")

    @staticmethod
    def print_array(array):
        for num in array:
            print(num, end=" ")
        print()
