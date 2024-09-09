# Name: Thant Si Thu Naing
# ID: 6611720
# Sec: 541

import sys

def create_adjacency_list(edges, num_vertices):
    adjacency_list = {i: [] for i in range(num_vertices)}
    for edge in edges:
        u, v = edge
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    return adjacency_list


def print_adjacency_list(adjacency_list):
    for node in adjacency_list:
        print(f"{node}: {adjacency_list[node]}")


data = sys.stdin.readlines()
num_vertices = 0
num_edges = 0
edges = []
indexer = 0
while indexer < len(data) - 1:
    n, m = map(int, data[indexer].split(" "))
    if indexer == 0:
        num_vertices = n
        num_edges = m
    else:
        edges.append((n, m))
    indexer = indexer + 1

adjacency_list = create_adjacency_list(edges, num_vertices)
print_adjacency_list(adjacency_list)
