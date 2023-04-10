from collections import deque

N = int(input())
graph = [list(map(int,input())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    count = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    return count

number = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            number.append(bfs(i, j))

number.sort()
print(len(number))
for i in number:
    print(i)