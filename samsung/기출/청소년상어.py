'''
4 * 4
1 <= 번호 <= 16, 같은 번호는 없음
방향은 8가지 방향 ( 대각선까지 )
상어는 (0,0)에서 물고기를 먹고 시작, 방향도 흡수

1. 물고기는 번호가 작은 물고기부터 순서대로 이동한다.
    이동할 수 있는 칸 : 빈칸, 다른 물고기가 있는 칸
    이동할 수 없는 칸 : 상어가 있는 칸, 경계를 넘는 칸
2. 각 물고기가 이동할 수 없을 경우, 이동할 수 있는 칸을 향할 때까지 45도 반시계 회전시킨다.
    못찾으면, 이동은 하지 않는다.
3. 상어의 이동
    3-1. 가지고 있는 방향으로 이동 ( 여러칸 가능 )
    3-2. 물고기를 먹으면 그 방향을 가지게 됨.
    3-3. 물고기가 없는 칸에는 이동 불가, 이동 못하면 집으로 감
'''
'''
필요한 함수.
1. 회전
2. 이동

'''

# 북부터 반시계
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

space = []
for _ in range(4):
    row = list(map(int, input().split()))
    space.append([row[i:i+2] for i in range(0, 8, 2)])

numbers = [i for i in range(16,0,-1)]


def rotate_45(dir):
    dir = (dir+1) % 8
    return dir


def move():
    
