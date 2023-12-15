from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class PigeonholeSort(ImethodAlgorithms):
    def __init__(self):
        self.iterations = 0
        pass

    def sort(self, arr):
        self.pigeonhole_sort(arr)
        print(f'Number of iterations: {self.iterations}')

    def pigeonhole_sort(self, arr):
        _min = min(arr)
        _max = max(arr)
        _range = _max - _min + 1
        pigeonholes = [0] * _range

        for element in arr:
            self.iterations += 1
            print(arr)
            pigeonholes[element - _min] += 1

        index = 0

        for j in range(_range):
            self.iterations += 1
            print(arr)
            while pigeonholes[j] > 0:
                arr[index] = j + _min
                index += 1
                pigeonholes[j] -= 1
