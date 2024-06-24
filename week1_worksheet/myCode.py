## id - 6611720
## name - Thant Si Thu Naing
## section - 541
import time

K = int(input())
a = list(map(int, input().split()))

st = time.process_time()

found = False
seen = set()

for x in a:
    if x != 0 and K % x == 0:
        y = K // x
        if y in seen:
            found = True
            break
        seen.add(x)

et = time.process_time()

if not found:
    print("No pair multiplies to K")
else:
    print(x, y)
print("Running time:", et - st)
