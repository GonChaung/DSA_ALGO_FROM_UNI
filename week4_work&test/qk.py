import sys
import time

# Set recursion limit
sys.setrecursionlimit(10000)

# Global counter variable
counter = 0

# Partition function
def partition(A, p, r):  # Lomuto's partition scheme
    global counter
    x = A[r]
    i = p - 1
    for j in range(p, r):
        counter += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1

# QuickSort function
def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q - 1)
        quickSort(arr, q + 1, r)

# Read input array from stdin (own_test_case.txt)
input_data = sys.stdin.read().strip()

# Split input by spaces and convert to integers
arr = list(map(int, input_data.split()))

# Measure time
st = time.process_time()
quickSort(arr, 0, len(arr) - 1)
et = time.process_time()

# Print sorted list, time taken, and counter value
print("Sorted array:", arr)
print("Time taken for sorting:", et - st)
print("Counter value (number of steps):", counter)
