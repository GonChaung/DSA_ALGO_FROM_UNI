from topological_sort import *
first_line = [int(x) for x in input().split()]
n_nodes = first_line[0]
n_edges = first_line[1]
#print(first_line)
adj_list = [[] for _ in range(n_nodes)]
#print(adj_list)
for each in range(n_edges):
    e_line = [int(x) for x in input().split()]
    adj_list[e_line[0]].append(e_line[1])
#print(adj_list)
print(topological_sort(n_nodes, adj_list))
