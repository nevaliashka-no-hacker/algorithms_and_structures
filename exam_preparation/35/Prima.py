'''Алгоритм Прима'''

import heapq

def prim(graph, start):
    if not graph:
        return [], 0

    mst_edges = []
    total_cost = 0
    visited = set()
    min_heap = []

    def add_edges_to_heap(vertex):
        visited.add(vertex)
        for neighbor, weight in graph[vertex].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, vertex, neighbor))

    add_edges_to_heap(start)

    while min_heap:
        weight, from_vertex, to_vertex = heapq.heappop(min_heap)
        if to_vertex in visited:
            continue
        mst_edges.append((from_vertex, to_vertex, weight))
        total_cost += weight
        add_edges_to_heap(to_vertex)
    if len(visited) != len(graph):
        print("ytcdzpysq")
    return mst_edges, total_cost
            
graph = {
        'A': {'B': 2, 'C': 3, 'D': 4},
        'B': {'A': 2, 'D': 1, 'E': 5},
        'C': {'A': 3, 'D': 6, 'F': 8},
        'D': {'A': 4, 'B': 1, 'C': 6, 'E': 7, 'F': 9},
        'E': {'B': 5, 'D': 7},
        'F': {'C': 8, 'D': 9},
    }    
print(prim(graph, 'A'))
