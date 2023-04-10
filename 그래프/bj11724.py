import sys
N, M = map(int, input().split()) # N : 정점의 개수, M : 간선의 개수

input = sys.stdin.readline

graph = [list() for _ in range(N+1)]
chk = [False] * (N+1) # 방문 처리
count = 0 # 컴포넌트 개수 저장

for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(start, depth):
    # 해당 노드 방문 체크를 한다.
    chk[start] = True

    # 해당 시작점을 기준으로 계속해서 dfs로 그래프를 탐색한다.
    for i in graph[start]:
        if not chk[i]:
            dfs(i, depth + 1)

for i in range(1, N+1):
    if not chk[i]: # 만약 i 번째 노드를 방문하지 않았다면
        if not graph[i] : # 만약 해당 정점이 연결된 그래프가 없다면
            count += 1
            chk[i] = True # 방문처리
        else: #연결된 그래프가 있다면
            dfs(i, 0)
            count += 1

print(count)