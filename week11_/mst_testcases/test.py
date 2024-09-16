V, E = map(int, input().split())

A = []
for _ in range(E):
    u, v, weight = map(int, input().split())
    A.append((u, v, weight))
A.sort(key=lambda x: x[2])
print(A)