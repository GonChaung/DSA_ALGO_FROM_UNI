# name - Thant Si Thu Naing
# id - 6611720
# section - 541

from Heap_Decrease_Key import *

class Node:
    def __init__(self, vertex, key):
        self.vertex = vertex
        self.key = key
        self.a_index = None


def dijkstra(graph, vertices, start_vertex):
    inf = float('inf')
    distances = [inf] * (vertices + 1)
    predecessors = [None] * (vertices + 1)
    distances[start_vertex] = 0

    nodes = [Node(v, distances[v]) for v in range(vertices + 1)]
    priority_queue = heap(nodes[1:])

    while not priority_queue.empty():
        u_index = priority_queue.extract()
        u = priority_queue.items[u_index].vertex

        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u
                priority_queue.elevate_key(v - 1, distances[v])

    return distances[1:], predecessors[1:]


if __name__ == "__main__":
    graph_type = input().strip()
    vertices, edges = map(int, input().strip().split())

    graph = {i: [] for i in range(1, vertices + 1)}

    for _ in range(edges):
        u, v, weight = map(int, input().strip().split())
        graph[u].append((v, weight))
        if graph_type == "Undirected Graph":
            graph[v].append((u, weight))

    start_vertex = 1

    distances, predecessors = dijkstra(graph, vertices, start_vertex)

    for i in range(1, vertices + 1):
        print(f"{i} {distances[i - 1]} {predecessors[i - 1] or 'None'}")