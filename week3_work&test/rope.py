from Heap import heap
import time
arr = list(map(int, input().split()))
st = time.process_time()
h = heap(arr)
total_cost = 0
while h.heapsize > 1:
    first = h.extract()
    second = h.extract()
    combined = first + second
    total_cost += combined
    h.insert(combined)
print(total_cost)
et = time.process_time()
print(et-st)