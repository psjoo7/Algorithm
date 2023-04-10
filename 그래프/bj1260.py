#DFS -> stack
#BFS -> queue
from sys import stdin
from collections import deque

def bfs(start):
    queue = deque([start])
    check1[start] = 1
    while queue:
        v= queue.popleft()
        print(v, end= " ")
        for i in adj[v]:
            if not check1[i]:
                check1[i] = 1
                queue.append(i)

def dfs(start):
    check2[start] = 1
    print(start, end=" ")
    for i in adj[start]:
        if not check2[i]:
            dfs(i)

node, edge, start = map(int, stdin.readline().split())

check1 = [0 for i in range(node+1)]
check2 = [0 for i in range(node+1)]
answerDFS = []
answerBFS = []
#인접 리스트 구현
adj = [[] for _ in range(node+1)]
for _ in range(edge):
    src, dest = map(int, stdin.readline().split())
    adj[src].append(dest)
    adj[dest].append(src)

for i in adj:
    i.sort()

dfs(start)
print()
bfs(start)