from collections import deque

testcase = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = 0


for i in range(testcase):
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    count = 0

    for j in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1:
                bfs(a, b)
                count += 1

    print(count)