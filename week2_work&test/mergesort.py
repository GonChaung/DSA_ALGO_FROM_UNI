
def merge(A, p, q, r):
  return A
    

def mergesort(A, p, r):
    return A


a = list(map(int, input().split()))

import time

st = time.process_time()

mergesort(a, 0, len(a)-1)

et = time.process_time()

print(a)
print(et-st)
