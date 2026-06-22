'''Поиск цикла в графе'''

def search_cycle(graph):
    visited = set()

    for start in graph:
        if start not in visited:
            stack = [(start, None)]
            visited.add(start)
        while stack:
            node, parent = stack.pop()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, node))
                elif neighbor != parent:
                    return True
    return False

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3]
}

print(search_cycle(graph))

