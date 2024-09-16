# name - Thant Si Thu Naing
# id - 6611720
# section - 541
from disjointsets3 import DisjointSets

def kruskal(V, edges):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSets(V)
    mst_weights = 0
    mst_edges = []
    for u, v, weight in edges:
        if ds.findset(u) != ds.findset(v):
            mst_weights += weight
            mst_edges.append((u, v, weight))
            ds.union(u, v)
    return mst_weights, mst_edges

V, E = map(int, input().split())

A = []
for _ in range(E):
    u, v, weight = map(int, input().split())
    A.append((u, v, weight))

mst_weights, mst_edges = kruskal(V, A)
print(mst_weights)
