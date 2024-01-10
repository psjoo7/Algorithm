array = []

for i in range(19):
    array.append(list(map(int, input().split())))
#북, 북동, 동, 남동, 남, 서남, 서, 북서
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

visited = [[0]*19 for _ in range(19)]
x, y = 0, 0

def dfs(x, y):
    if array[x][y] != 0:
        visited[x][y] = True
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            while nx <= -1 or nx > 19 or ny <= -1 or ny > 19:
                continue
                