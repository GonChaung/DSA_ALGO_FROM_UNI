import time
a = list(map(int, input().split()))
n = len(a)
st = time.process_time()

# write the insertion sort code into this segment
for i in range(1, n):
    key = a[i]
    j = i - 1
    while j >= 0 and key < a[j]:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key
et = time.process_time()
print(a)
print(et-st)
