import networkx as nx

graph = nx.Graph()
with open("t.txt", "r") as file:
    for line in file:
        node1, node2 = line.strip().split("-")

        graph.add_edge(node1, node2)

# a = sorted(nx.approximation.max_clique(graph))
# print(a)
triangle = [t for t in nx.enumerate_all_cliques(graph) if len(t) == 3]
filtered_triangles = [
    triangle for triangle in triangle if any(node.startswith("t") for node in triangle)
]
print("part1:-", len(filtered_triangles))
largest = max(nx.find_cliques(graph), key=len)

largest.sort()
print("part2:-")
for i in largest:
    print(i, end=",")
print("\n")
