from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms

class CountingSort(ImethodAlgorithms):
    def __init__(self):
        self.iterations = 0
        self.exchanges = 0

    def sort(self, arr):
        n = len(arr)

        # Encontrar el rango del arreglo
        max_value = self.find_max(arr)

        # Crear un arreglo de conteo y un arreglo resultado
        count = [0] * (max_value + 1)
        output = [0] * n

        # Contar la frecuencia de cada elemento
        for i in range(n):
            count[arr[i]] += 1

        # Actualizar el arreglo de conteo para contener las posiciones reales
        for i in range(1, max_value + 1):
            count[i] += count[i - 1]

        # Construir el arreglo de salida
        for i in range(n - 1, -1, -1):
            output[count[arr[i]] - 1] = arr[i]
            count[arr[i]] -= 1
            self.iterations += 1
            self.exchanges += 1

            # Print the array after each exchange
            print(output)

        # Copiar el arreglo de salida de vuelta al arreglo original
        for i in range(n):
            arr[i] = output[i]

        # Print the number of iterations and exchanges
        print(f'Number of iterations: {self.iterations}')
        print(f'Number of swaps: {self.exchanges}')

    @staticmethod
    def find_max(arr):
        max_value = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max_value:
                max_value = arr[i]
        return max_value
