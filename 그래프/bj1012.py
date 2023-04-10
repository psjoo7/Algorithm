#DFS는 런타임 에러가 남

testcase = int(input())

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx,ny)

for _ in range(testcase):
    count = 0
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                dfs(i,j)
                count += 1
    print(count)