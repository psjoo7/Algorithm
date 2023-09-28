from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b):
    dq = deque()
    dq.append((a,b))
    matrix[a][b] = 0

    while dq:
        a, b = dq.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if matrix[nx][ny] == 1:
                dq.append((nx, ny))
                matrix[nx][ny] = 0


T = int(input())
for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split()) # M : 가로, N : 세로, K : 배추 위치 개수
    matrix = [[0] * N for _ in range(M)]

    for i in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    for a in range(N):
        for b in range(M):
            if matrix[a][b] == 1:
                bfs(a,b)
                cnt += 1

    print(cnt)