# N*N 크기의 공간 / M마리의 물고기 / 아기 상어 1마리
# 한 칸에는 물고기 최대 1마리
# 아기 상어의 크기는 한 칸씩 움직이고, 처음 크기는 2
# 1. 물고기 < 상어 : 먹는다
# 2. 물고기 = 상어 : 지나갈 수 있다. 먹을순 없다
# 3. 물고기 > 상어 : 먹을수도 지나갈 수도 없다.
# 이동 결정 방법 :
# 1. 더이상 먹을 수 있는 물고기가 없다면 끝!
# 2. 먹을 수 있는 물고기가 1마리라면 거기로 이동
# 3. 1마리 이상이라면, 거리가 가장 가까운 쪽으로 간다. 하지만 거리가 같다면, 가장 위에있는 물고기
# 3. 그러한 물고기가 여러마리면, 가장 왼쪽에 있는 물고기를 먹는다.
# 크기가 늘어나는 방법:
# 크기와 같은 수의 물고기를 먹으면 됨!
from collections import deque

n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]
# 물고기와 상어의 위치 정보가 들어가야함
fish = []
sharkSize = 2
eat_count = 0
fish_count = 0
time = 0
shark_x, shark_y = 0 , 0
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            shark_x, shark_y = i, j
            sea[shark_x][shark_y] = 0 # 지나간 자리
        elif 0 < sea[i][j] <= 6:
            fish.append((i,j))
            fish_count += 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(shark_x, shark_y):
    q = deque([(shark_x,shark_y,0)])
    dist_list=[]
    visited = [[False] * n for _ in range(n)]
    visited[shark_x][shark_y] = True
    min_dist = int(1e9)

    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n or 0 <= ny < n and not visited[nx][ny]:
                if sea[nx][ny] <= sharkSize:
                    visited[nx][ny] = True
                    if 0 < sea[nx][ny] < sharkSize:
                        min_dist = dist
                        dist_list.append((dist+1, nx, ny))
                    if dist + 1 <= min_dist:
                        q.append((nx, ny, dist+1))

    if dist_list:
        dist_list.sort()
        return dist_list[0]
    else:
        return False

while fish_count:
    result = bfs(shark_x,shark_y)
    if not result:
        break
    shark_x, shark_y = result[1], result[2]
    time += result[0]
    eat_count += 1
    fish_count -= 1
    if sharkSize == eat_count:
        sharkSize += 1
        eat_count = 0
    sea[shark_x][shark_y] = 0

print(time)