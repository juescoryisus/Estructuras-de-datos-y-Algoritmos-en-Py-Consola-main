from Interfaces.Algorithms.ImethodAlgorithms import ImethodAlgorithms


class BucketSort(ImethodAlgorithms):
    def __init__(self):
        pass

    def sort(self, arr):
        return self.bucket_sort_double(arr)

    @staticmethod
    def print_bucket_state(buckets):
        print("Current state of buckets:")
        for i in range(len(buckets)):
            print(f"Bucket {i}: {' '.join(map(str, buckets[i]))}")
        print()

    @staticmethod
    def bucket_sort_double(array):
        # Create empty buckets
        buckets = [[] for _ in range(len(array))]

        # Insert elements into their respective buckets
        for element in array:
            buckets[int(element * len(array))].append(element)

        # Print the state of buckets after insertion
        BucketSort.print_bucket_state(buckets)

        # Sort the elements in each bucket
        for i in range(len(array)):
            buckets[i].sort()

        # Print the state of buckets after sorting
        BucketSort.print_bucket_state(buckets)

        # Get the sorted elements
        k = 0
        for i in range(len(array)):
            for item in buckets[i]:
                array[k] = item
                k += 1

        return array
