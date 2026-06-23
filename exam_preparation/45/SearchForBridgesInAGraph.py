'''Поиск мостов и точек сочленения в графе'''
'''Алгоритм Тарьяна'''

def find_bridges_and_articulation_points(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    tin = [-1] * n
    fup = [-1] * n
    visited = [False] * n
    timer = 0
    bridges = []
    art_points = set()

    def dfs(v, parent):
        nonlocal timer
        visited[v] = True
        tin[v] = fup[v] = timer
        timer += 1
        children = 0
        for to in graph[v]:
            if to == parent:
                continue
            if visited[to]:
                fup[v] = min(fup[v], fup[to])
                if fup[to] > tin[v]:
                    bridges.append((v, to))
                if parent != -1 and fup[to] >= tin[v]:
                    art_points.add(v)
                children += 1
        if parent == -1 and children > 1:
            art_points.add(v)

    for i in range(n):
        if not visited[i]:
            dfs(i, -1)
    return bridges, art_points

edges = [(0,1),(1,2),(2,0),(1,3),(3,4)]
bridges, pts = find_bridges_and_articulation_points(5, edges)
print("Мосты:", bridges)
print("Точки сочленения:", pts)
