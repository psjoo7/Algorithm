n, m, x, y, k = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

graph = [list(map(int, input().split())) for _ in range(n)]
com = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: # east
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 2 : # west
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 3 : # north
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]=  e, a, c, d, f, b
    else: #south
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

nx, ny = x, y

for i in com: # dx, dy의 인덱스는 0부터 시작함
    nx += dx[i-1]
    ny += dy[i-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위를 벗어난 경우
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    turn(i)
    if graph[nx][ny] == 0: # 바닥이 0인 경우
        graph[nx][ny] = dice[0]
    else : # 바닥이 0이 아닌 경우
        dice[0] = graph[nx][ny]
        graph[nx][ny] = 0
    # 맨위의 다이스의 인덱스는 5이다.
    print(dice[5])