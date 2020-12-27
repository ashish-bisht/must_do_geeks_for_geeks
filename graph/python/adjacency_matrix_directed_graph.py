
# Directed graph


from collections import defaultdict

# Default dict is just like an dict , only major thing is it dosent give key error.


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insert_edge(self, v1, v2):
        self.graph[v1].append(v2)  # it means [1,2] , 1 => 2

    def print_graph(self):
        for node in self.graph:
            for vertex in self.graph[node]:
                print(node, " ", "==>", " ", vertex)


graph = Graph()

graph.insert_edge(1, 2)
graph.insert_edge(1, 3)
graph.insert_edge(2, 3)
graph.insert_edge(3, 4)

graph.print_graph()
