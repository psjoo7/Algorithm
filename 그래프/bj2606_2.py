n = int(input())
connection = int(input())
graph = [[] * n for _ in range(n+1)]
for _ in range(connection):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

count = 0
visited = [0] * (n+1)
def dfs(start):
    global count
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            count += 1

dfs(1)
print(count)