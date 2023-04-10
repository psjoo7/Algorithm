N = int(input()) # 총단지수
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

answer = [] # 단지별 주택 수

dx = [-1, 0, 1, 0] # 북, 동, 남, 서
dy = [0, 1, 0, -1] # 북, 동, 남, 서


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N: # 범위를 벗어나는 경우
        return False

    if graph[x][y] == 1:
        global count # 단지 내 주택 수
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

count = 0 # 단지 내 주택 수
num = 0 # 단지의 수

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            answer.append(count)
            num += 1 # 단지의 수는 늘고
            count = 0 # 단지 내 주택 수는 초기화

answer.sort()
print(num)
for i in answer:
    print(i)