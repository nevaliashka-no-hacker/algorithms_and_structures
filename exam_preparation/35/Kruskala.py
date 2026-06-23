'''Алгоритм Крускала'''

'''easy version'''
def has_path(graph, start, end, visited = None):
    if visited is None:
        visited = set()
    if start == end:
        return True

    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            if has_path(graph, neighbor, end, visited):
                return True
    return False

def kruskal(vertices, edges):
    sorted_edges = sorted(edges, key=lambda x: x[0])
    mst_graph = {v: [] for v in vertices}
    mst_edges = []
    total_weight = 0

    for weight, u, v in sorted_edges:
        if has_path(mst_graph, u, v):
            continue
        else:
            mst_graph[u].append(v)
            mst_graph[v].append(u)
            mst_edges.append((u, v, weight))
            total_weight += weight
            if len(mst_edges) == len(vertices) - 1:
                break
    return mst_edges, total_weight

vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    (1, 'A', 'B'),
    (2, 'B', 'C'),
    (3, 'A', 'C'),
    (4, 'C', 'D'),
    (5, 'B', 'D'),
    (6, 'D', 'E'),
]

print(kruskal(vertices, edges))
