'''Задача с лабиринтом'''

import heapq

def shortest_path_in_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    dist = [[10**10] * cols for _ in range(rows)]
    sr, sc = start
    gr, gc = goal
    dist[sr][sc] = maze[sr][sc]
    heap = [(dist[sr][sc], sr, sc)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while heap:
        cur_cost, r, c = heapq.heappop(heap)
        if cur_cost != dist[r][c]:
            continue
        if (r, c) == goal:
            return cur_cost
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_cost = cur_cost + maze[nr][nc]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))
    return -1

maze = [[1,2,3],[4,5,6],[7,8,9]]
print(shortest_path_in_maze(maze, (0,0), (2,2)))
