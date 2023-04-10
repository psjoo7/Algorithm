# N * N 의 정사각 보드
# 뱀의 시작 위치 맨위 맨좌 ( 0, 0 ) / 뱀의 길이 1
# 뱀은 처음 오른쪽을 향한다. (dx, dy) = (0, 1)
# 벽 또는 자기자신의 몸과 부딪히면 게임이 끝남
# 3가지 규칙 ( 뱀은 매초 이동함)
# 1. 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다. 몸길이가 변한다 (+1)
# 3. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이가 변하지 않는다.
from collections import deque

N = int(input()) # 보드의 크기
board = [[0] * (N+1) for _ in range(N+1)]
K = int(input()) # 사과의 개수
for i in range(K): # 사과의 위치
    # 첫 번째 정수는 행, 두 번째 위치는 열 위치를 의미한다.
    y, x = map(int, input().split())
    board[y-1][x-1] = 2
L = int(input()) # 방향 변환 횟수
# L : 왼쪽 방향으로 방향 전환 90도 ( 반 시계 )
# D : 오른쪽 방향으로 방향 전환 90도 ( 시계 )
dx = [0, 1, 0, -1] # 동 부터 시계 방향
dy = [1, 0, -1, 0] # 동 부터 시계 방향
# 0: 오른쪽으로 1: 아래쪽 2: 왼쪽 3: 위쪽
# 0: 오른쪽으로 -1: 위쪽 -2: 왼쪽 -3: 아래쪽
direct = dict()
for _ in range(L):
    # X초가 끝난 뒤 ( 그니까 그초는 이동을 한거임, 이후 이동을 하는 거지 )
    second, direction = input().split()
    direct[int(second)] = direction
def turn(alpha):
    global d
    if alpha == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4

# L : 반시계이므로 d -= 1, D : 시계이므로 d += 1
d = 0 # 현재 움직이는 방향을 의미함
s = 0 # 타이머
x, y = 0,0
# 사과를 먹지 못한 경우는 길이가 그대로니까, 지나간 자리를 다시 0 으로 바꿔줘야함.
# 사과를 먹은 경우는 길이가 변하므로, 지나간 자리를 신경쓰지 않는다.
snake = deque()
snake.append((x, y))
board[x][y] = 1
# 시작 : 뱀의 머리 ( x , y )
while True:
    x += dx[d]
    y += dy[d]
    # 종료 지점 : 몸통과 충돌 or 벽에 충돌
    if x < 0 or x >= N or y >= N or y < 0 or board[x][y] == 1:
        print(s+1)
        break
    s += 1 # 1초 지난 시점임
    snake.append((x, y))
    if board[x][y] == 0: # 아무것도 없는 경우 : 몸 길이가 그대로다
        board[x][y] = 1
        bx, by = snake.popleft()
        board[bx][by] = 0
        if s in direct:
            turn(direct[s])
    elif board[x][y] == 2: # 사과가 있는 경우 : 몸 길이가 늘어난다.
        board[x][y] = 1
        if s in direct:
            turn(direct[s])
