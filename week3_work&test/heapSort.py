# name - Thant Si Thu Naing
# ID - 6611720
# section - 541

from Heap import heap
import time

def compare(x,y):
    return x<y

arr = list(map(int, input().split()))
start = time.process_time()
h = heap(arr , cmp = compare)
sorted_list = []
while not h.empty():
    sorted_list.append(h.extract())
print(sorted_list[::-1])
et = time.process_time()
print(et-start)