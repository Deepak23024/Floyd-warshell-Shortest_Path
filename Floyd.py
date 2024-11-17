import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

INF = float('inf')


def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph]
    for k in range(V):
        for i in range(V):
            for j in range(V):

                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


graph = [
    [0, 3, INF, 5],
    [3, 0, 2, INF],
    [INF, 2, 0, 4],
    [5, INF, 4, 0]
]


shortest_paths = floyd_warshall(graph)


print("Shortest path matrix (in terms of cost/time):")
for row in shortest_paths:
    print(row)
G = nx.DiGraph()
airports = ['A', 'B', 'C', 'D']

for i in range(len(shortest_paths)):
    for j in range(len(shortest_paths)):
        if shortest_paths[i][j] != INF and i != j:
            G.add_edge(airports[i], airports[j], weight=shortest_paths[i][j])


pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue")
nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")
nx.draw_networkx_edges(G, pos, edgelist=G.edges(data=True), arrowstyle="->", arrowsize=20, edge_color="black")

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")

plt.title("Optimized Airline Route Network with Costs/Times")
plt.axis("off")
plt.show()
