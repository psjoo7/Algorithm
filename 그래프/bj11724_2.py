from collections import deque
import sys

input = sys.stdin.readline
def bfs(start):
    queue = deque([start])
    chk[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not chk[i]:
                chk[i] = True
                queue.append(i)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# 방문 처리
chk = [False] * (N+1)
count = 0

for i in range(1, N+1):
    if not chk[i]: # 방문하지 않았다면
        if not graph[i]: #연결된 간선이 없다면
            count += 1
            chk[i] = 1
        else: #연결된 간선이 있다면
            bfs(i)
            count += 1

print(count)