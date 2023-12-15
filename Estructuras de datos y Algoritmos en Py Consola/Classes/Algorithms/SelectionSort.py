from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class SelectionSort(ImethodAlgorithms):
    def __init__(self):
        self.iterations = 0
        self.swaps = 0
        pass

    def sort(self, arr):
        n = len(arr)

        for i in range(n - 1):
            self.iterations += 1
            # Encontrar el índice del elemento mínimo en el subarreglo no ordenado
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            # Intercambiar el elemento mínimo encontrado con el primer elemento del subarreglo no ordenado
            arr[i], arr[min_index] = arr[min_index], arr[i]
            self.swaps += 1
            print(arr)

        print(f'Number of iterations: {self.iterations}')
        print(f'Number of swaps: {self.swaps}')
