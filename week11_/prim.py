# name - Thant Si Thu Naing
# id - 6611720
# section - 541

import heapq

def prim(V, edges):
    adj_list = [[] for _ in range(V)]
    for u, v, weight in edges:
        adj_list[u].append((weight, v))
        adj_list[v].append((weight, u))

    in_mst = [False] * V

    pq = []

    in_mst[0] = True
    for weight, v in adj_list[0]:
        heapq.heappush(pq, (weight, v, 0))

    mst_weight = 0
    mst_edges = []

    while pq:
        weight, u, parent = heapq.heappop(pq)
        if not in_mst[u]:
            in_mst[u] = True
            mst_weight += weight
            mst_edges.append((parent, u, weight))

            for next_weight, v in adj_list[u]:
                if not in_mst[v]:
                    heapq.heappush(pq, (next_weight, v, u))

    return mst_weight, mst_edges

V, E = map(int, input().split())

edges = []
for _ in range(E):
    u, v, weight = map(int, input().split())
    edges.append((u, v, weight))
mst_weight, mst_edges = prim(V, edges)

print(mst_weight)
# print("Edges in the minimum spanning tree:")
# for u, v, weight in mst_edges:
#     print(f"{u} - {v} (weight: {weight})")
