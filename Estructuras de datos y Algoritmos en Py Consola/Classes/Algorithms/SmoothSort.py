from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class SmoothSort(ImethodAlgorithms):
    def __init__(self):
        self.heap = []
        self.iterations = 0

    def sort(self, arr):
        self.heap = arr
        n = len(arr)

        for i in range((n-1)//2, -1, -1):
            self.sift_down(i, n - 1)
            self.iterations += 1

        for i in range(n - 1, 0, -1):
            self.swap(0, i)
            self.sift_down(0, i - 1)
            self.iterations += 1

    def sift_down(self, root, end):
        left_child = 2 * root + 1
        while left_child <= end:
            right_child = left_child + 1
            swap_index = root

            if self.heap[swap_index] < self.heap[left_child]:
                swap_index = left_child

            if right_child <= end and self.heap[swap_index] < self.heap[right_child]:
                swap_index = right_child

            if swap_index == root:
                return
            else:
                self.swap(root, swap_index)
                root = swap_index
                left_child = 2 * root + 1

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
