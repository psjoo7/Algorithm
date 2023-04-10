from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())

graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i,j])

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m :
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

ans = 0
for line in graph:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()
    ans = max(ans, max(line))

print(ans - 1)