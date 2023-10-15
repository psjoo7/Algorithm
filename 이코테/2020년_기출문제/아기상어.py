# 상어 크기 2, 1초에 상하좌우 1칸
from collections import deque
n = int(input())
INF = 1e9
graph = []
for i in range(n):
    graph.append(map(int, input().split()))

size = 2
x, y = 0, 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j
            graph[x][y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    dist = [[-1] * n for _ in range(n)]
    q = deque((x, y))
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if dist[nx][ny] == -1 and graph[nx][ny] <= size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    return dist

def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= graph[i][j] and graph[i][j] < size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist

result = 0
ate = 0

while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        x, y = value[0], value[1]
        result += value[2]
        graph[x][y] = 0
        ate += 1
        if ate >= size:
            size += 1
            ate = 0