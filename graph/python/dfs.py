
#     2
#    /  \
#  1      5
#        /  \
#       6    8
#      /
#     9

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insert_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)

    def dfs(self, starting_node):
        stack = [starting_node]
        visited = set()

        while stack:
            cur_node = stack.pop()
            if cur_node not in visited:
                visited.add(cur_node)
                print(cur_node, end=" ")
                for vertex in self.graph[cur_node]:
                    stack.append(vertex)


graph = Graph()

graph.insert_edge(2, 1)
graph.insert_edge(2, 5)
graph.insert_edge(5, 6)
graph.insert_edge(5, 8)
graph.insert_edge(6, 9)

graph.dfs(2)
