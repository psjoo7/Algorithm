N, L = map(int, input().split())

road_row = [list(map(int, input().split())) for _ in range(N)]
road_col = [[road_row[i][j] for i in range(N)] for j in range(N)]
result = 0

# 경사로를 놓을 수 있는 조건
# 1. L개의 연속된 칸에 경사로의 바닥이 모두 접해야한다.
# 2. 낮은 간과 높은 칸의 높이 차이는 1이어야 한다.
# 3. 경사로를 놓을 낮은 칸의 높이는 모두 같아야하고, L개의 칸이 연속되어야한다.

# 경사로를 놓을 수 없는 조건
# 1. 경사로를 놓은 곳에 또 경사로를 놓는 경우
# 2. 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
# 3. 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
# 4. 경사로를 놓다가 범위를 벗어나는 경우

def pos(now):
    for j in range(1, N):
        if abs(now[j] - now[j-1]) > 1:
            return False
        if now[j] < now[j-1]: # 현재 < 이전 (경사로를 만들려면, 오른쪽으로 스캔해야함)
            for k in range(L): # L 만큼의 경사로 너비가 필요하므로 체크해야됨 변동이 있는지
                # 1. 범위를 넘어가거나, 2. 이미 사용됐거나, 3. 중간에 높이가 변화가 있거나
                if j + k >= N or used[j+k] or now[j] != now[j+k]:
                    return False
                if now[j] == now[j+k]: # 높이가 같다면 사용여부 체크
                    used[j+k] = True
        elif now[j] > now[j-1]: # 현재 > 이전 ( 경사로를 만들려면, 왼쪽으로 스캔이 필요함)
            for k in range(L):
                if j - k - 1 < 0 or now[j - 1] != now[j - k - 1] or used[j - k - 1]:
                    return False
                # 높이가 같은 경우 사용 여부 체크
                if now[j - 1] == now[j - k - 1]:
                    used[j - k - 1] = True
        return True # 아무 문제 없이 설치가 됐다면 가능함을 출력해줘야함

# 1. 가로의 경우
for i in range(N):
    used = [False] * N # 사용 여부
    if pos(road_row[i]): # 현재 확인할 길을 넣어줌
        result += 1

# 2. 세로의 경우
for i in range(N):
    used = [False] * N # 사용 여부
    if pos(road_col[i]):
        result += 1

print(result)

