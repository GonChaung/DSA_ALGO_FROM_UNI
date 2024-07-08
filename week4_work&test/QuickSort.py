import sys
import time

sys.setrecursionlimit(10000)
counter = 0
def partition(A, p, r): ## p is start_index and r is pivot
    global counter
    x = A[r]
    i = p-1
    for j in range(p, r):
        counter += 1
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[r],A[i+1] = A[i+1],A[r]
    return i+1

def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q-1)
        quickSort(arr, q+1, r)

arr = list(map(int, input().split()))
st = time.process_time()
quickSort(arr, 0, len(arr)-1)
et = time.process_time()
print("Sorted list: ",arr)
print("Taking time: ", et-st)
print("Counter value (number of steps): ", counter)