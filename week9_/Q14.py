# Name: Thant Si Thu Naing
# ID: 6611720
# Sec: 541

import sys

def create_adjacency_matrix(edges, num_vertices):
    adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    for edge in edges:
        u, v = edge
        adjacency_matrix[u][v] = 1
        adjacency_matrix[v][u] = 1
    return adjacency_matrix


def print_adjacency_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


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

adjacency_matrix = create_adjacency_matrix(edges, num_vertices)
print_adjacency_matrix(adjacency_matrix)
