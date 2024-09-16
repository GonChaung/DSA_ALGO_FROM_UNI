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

connected = True
for i in range(1, V):
    if s.findset(i) != representative:
        connected = False
        break

if connected:
    print("The graph is connected.")
else:
    print("The graph is not connected.")