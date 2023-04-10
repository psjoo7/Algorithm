import queue

n, m = map(int, input().split())

a = [list(map(int, input())) for _ in range(n)]

chk = [[0] * m for _ in range(n)]

q = queue.Queue()
q.put([0,0])
chk[0][0] = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while not q.empty():
    x, y = q.get()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n : continue # 1. nx 가 배열의 범위를 넘었는가
        if ny < 0 or ny >= m : continue # 2. ny 가 배열의 범위를 넘었는가
        if a[nx][ny] == 0 : continue # 3. 벽이 있는가
        if chk[nx][ny] != 0 : continue # 4. 이미 방문하였는가

        chk[nx][ny] = chk[x][y] + 1
        q.put([nx,ny])

print(chk[n-1][m-1])