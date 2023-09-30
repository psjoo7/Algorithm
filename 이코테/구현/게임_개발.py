# N * M 크기 / 육지 or 바다
# 1. 현재 방향 기준으로 왼쪽 방향부터 차례대로 간다.
# 2. 바로 왼쪽 방향에 가보지 못한 칸이 존재하면 왼쪽으로 회전 후 한 칸 전진, 없다면 왼쪽 방향으로 회전만
# 3. 네 방향 모두 가본 칸 or 바다 인 경우, 바라보는 방향은 유지한 채로 한 칸 뒤로 이동, BUT 뒤쪽이 바다인 경우 움직임 멈추기

# 0 : 육지 / 1 : 바다
# 0 : 북 / 1 : 동 / 2 : 남 / 3 : 서

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
d = [[0] * m for _ in range(n)]
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if array[nx][ny] == 0 and d[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn = 0
        continue
    else:
        turn += 1
    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn = 0

print(count)
