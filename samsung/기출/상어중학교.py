from collections import deque
''' 
N * N 격자
1 <= M <= 5
초기 상태 : 모든 칸에는 블록 하나
블록의 종류 : 검은색( -1 ) , 무지개 ( 0 ), M가지 색상의 일반 블록
블록 그룹 :
    블록의 개수 2 이상,
    일반 블록의 색은 모두 같아야함
    검은 블록은 X,
    무지개는 상관 노,
    인접한 칸을 통해 모두 이동할 수 있어야함
    기준 블록은 무지개 블록이 아닌 블록 중 행의 번호 ( 겹치면 열 )가 가장 작은 블록
'''

'''
필요 함수 : 
    중력을 적용하는 함수
    가장 큰 그룹을 구하는 함수 - 가장 큰 그룹을 그래프에서 지우기도 해야함.
'''
# 북, 동, 남, 서
# x 가 위 아래, y 가 좌 우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
graph = []
# group = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


def turn_graph(): # 그래프를 돌리는 함수 ( 반시계 90도 )
    temp = []
    for i in range(N-1, -1, -1):
        array = []
        for j in range(N):
            array.append(graph[j][i])
        temp.append(array)
    return temp

# bfs
def block_group(i, j, color):
    queue = deque()
    queue.append([i,j])
    group = [[i,j]]
    rainbow = [] # 무지개블록은 방문을 다시 할 수 있도록 해야함
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 일반 블록
                if graph[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append([nx,ny])
                    group.append([nx,ny])
                # 무지개블록
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    group.append([nx, ny])
                    rainbow.append([nx, ny])

    for x, y in rainbow:
        visited[x][y] = False
    return [len(group), len(rainbow), group+rainbow]


def use_gravity(graph):
    for i in range(N-2, -1, -1):
        for j in range(N):
            if graph[i][j] > -1: # 일반블록, 무지개 블록이라면
                k = i
                while True:
                    if 0 <= k+1 < N and graph[k+1][j] == -2:
                        graph[k+1][j] = graph[k][j]
                        graph[k][j] = -2
                        k += 1
                    else:
                        break

answer = 0
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]  # 2. 방문을 했는지 확인하기 위한 배열
    # 3. 만들어지는 그룹들을 저장
    groups = []  # 그룹들을 저장할 배열
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                color = graph[i][j]
                group = block_group(i, j, color)
                if group[0] >= 2:
                    groups.append(group)
    # 4. 그중 제일 큰 그룹을 고르고, 그 그룹을 answer에 더해주고 graph에서 -2로 제헤준다.
    groups.sort(reverse=True)
    if not groups:
        break
    answer += groups[0][0] ** 2
    for i in groups[0][2]:
        x, y = i[0], i[1]
        graph[x][y] = -2
    # 5. 중력을 적용한다.
    use_gravity(graph)
    # 5. 그래프를 돌린다.
    graph = turn_graph()
    # 6. 중력을 적용한다.
    use_gravity(graph)

print(answer)