from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insert_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def display_graph(self):
        for node in self.graph:
            for vertex in self.graph[node]:
                print(node, "==>", vertex)


graph = Graph()
graph.insert_edge(1, 2)
graph.insert_edge(1, 3)
graph.insert_edge(1, 4)
graph.insert_edge(3, 4)

graph.display_graph()
