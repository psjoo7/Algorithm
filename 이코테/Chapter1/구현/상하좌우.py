# 지도 크기와 방향을 알려주면 위치를 출력해주는 문제

N = int(input())
order = input().split()
x, y = 1, 1
move_types = [ 'L', 'R', 'U', 'D' ]
dx = [ -1, 1, 0, 0 ]
dy = [ 0, 0, -1, 1 ]

for d in order:
    if d == move_types[0]:
        nx = x + dx[0]
        ny = y + dy[0]
    if d == move_types[1]:
        nx = x + dx[1]
        ny = y + dy[1]
    if d == move_types[2]:
        nx = x + dx[2]
        ny = y + dy[2]
    if d == move_types[3]:
        nx = x + dx[3]
        ny = y + dy[3]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x , y = nx, ny

print(x, y)