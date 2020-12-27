
from collections import defaultdict
import heapq


def shortest_path(times, start_node, total_nodes):
    graph = defaultdict(list)
    visited = set()

    for vertex1, vertex2, cost in times:
        graph[vertex1].append((cost, vertex2))

    min_heap = [(0, start_node)]

    distance_map = {i: float("inf") for i in range(1, total_nodes+1)}
    distance_map[start_node] = 0

    while min_heap:
        cur_distance, cur_vertex = heapq.heappop(min_heap)
        if cur_vertex in visited:
            continue
        visited.add(cur_vertex)

        if len(visited) == total_nodes:
            return cur_distance

        for next_distance, vertex in graph[cur_vertex]:
            if vertex not in visited and cur_distance + next_distance <= distance_map[vertex]:
                distance_map[vertex] = cur_distance + next_distance
                heapq.heappush(min_heap, (distance_map[vertex], vertex))

    return -1


print(shortest_path([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 2, 4))
