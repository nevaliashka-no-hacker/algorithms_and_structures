'''Алгоритм Дейкстры'''

import heapq

#самостоятельно - O(2n^2)
#неоптимально реализовала?
'''Так это жадное решение задачи коммивояжера...'''
def comm(graph, start, way = [], result = 0):
    if len(way) == 0:
        way.append(start)
    if len(way) >= len(graph):
        return result, way
    mnres = 10 ** 10
    for neighbor in graph[start]:
        if neighbor in way:
            continue
        mnres = min(mnres, result + graph[start][neighbor])

    for neighbor in graph[start]:
        if mnres == result + graph[start][neighbor] and neighbor not in way:
            result += graph[start][neighbor]
            way.append(neighbor)
    return comm(graph, way[-1], way, result)
            

#Здесь мне понадобится бинарная куча(это что вообще? ахаха)
def deikstra(graph, start):
    distances = {vertex: 10**10 for vertex in graph}
    distances[start] = 0

    parents = {start: None}

    pq = [(0, start)]
    while pq:
        cur_dist, u = heapq.heappop(pq)
        if cur_dist > distances[u]:
            continue
        for v, weight in graph[u].items():
            distance = cur_dist + weight
            if distance < distances[v]:
                distances[v] = distance
                parents[v] = u
                heapq.heappush(pq, (distance, v))
    return distances, parents

def reconstruct_path(parents, start, end):
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = parents.get(cur)
    path.reverse()
    if path and path[0] == start:
        return path
    else:
        return None

graph = {
    'A': {'B': 1, 'C': 4, 'E': 7, 'F': 3},
    'B': {'A': 1, 'C': 2, 'D': 5, 'F': 1},
    'C': {'A': 4, 'B': 2, 'D': 1, 'F': 4},
    'D': {'B': 5, 'C': 1, 'E': 2},
    'E': {'D': 2, 'A': 7, 'F': 8},
    'F': {'A': 3, 'B': 1, 'E': 8, 'C': 4}
    }
print(*comm(graph, 'C'))

dist, par = deikstra(graph, 'A')

print("min paths:")
for vertex, d in dist.items():
    print(f" A -> {vertex}: {d}")

print("paths:")
for target in graph:
    path = reconstruct_path(par, 'A', target)
    if path:
        print(f" {' -> '.join(path)} (lenght: {dist[target]})")
    else:
        print(f" {start_vertex} -> {target}: no path")
