# name - Thant Si Thu Naing
# id - 6611720
# section - 541

V, E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

from disjointsets3 import DisjointSets

# Initialize disjoint set
s = DisjointSets(V)

for u, v, w in edgeList:
    s.union(u, v)

representative = s.findset(0)
condition = True
for i in range(1, V):
    if s.findset(i) != representative:
        condition = False
        break

if condition:
    print("The graph is connected.")
else:
    print("The graph is not connected.")