# Name: Hein Oke Soe
# ID: 6611717
# Sec: 543

from Heap import *

def prim(vertices, edges):
    graph = {i: [] for i in range(vertices)}

    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = [False] * vertices

    pq = heap()

    pq.insert((0, 0))

    mst_cost = 0
    mst_edges = []

    while not pq.empty():
        weight, u = pq.extract()

        if visited[u]:
            continue

        visited[u] = True

        mst_cost += weight
        mst_edges.append(u)

        for w, v in graph[u]:
            if not visited[v]:
                pq.insert((w, v))

    return mst_cost, mst_edges


if __name__ == "__main__":
    V,E = map(int, input().split())
    edges = []

    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    mst_cost, mst_edges = prim(V, edges)

    print(mst_cost)