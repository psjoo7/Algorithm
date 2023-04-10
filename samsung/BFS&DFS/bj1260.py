import queue

n, m, v = map(int, input().split()) #정점의 개수, 간선의 개수, 시작 번호

a = [list() for _ in range(n+1)]
#a = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    a[start].append(end)
    a[end].append(start)
# for _ in range(m):
#     start, end = map(int, input().split())
#     a[start][end] = 1
#     a[end][start] = 1

for x in a:
    x.sort()


def bfs(start):
    q = queue.Queue()
    q.put(start)
    chk[start] = True

    while not q.empty():
        now = q.get() # 큐에서 가장 앞의 노드를 꺼내온다.
        print(now, end=" ") # 방문한 노드를 알려준다.
        for next in a[now]: # 방문한 노드의 다음 노드들의 방문 여부를 체크한다.
            if not chk[next]: # 다음 노드가 방문되지 않았으면
                chk[next] = True # 다음 노드를 방문하고
                q.put(next) # 방문한 노드를 표시하기 위해 큐에 넣어준다.
    print()

def dfs(node):
    chk[node] = True
    print(node, end=" ")

    for next in a[node]: # 현재 노드가 갈 수 있는 모든 노드 알아보기
        if not chk[next]: # 방문하지 않은 노드라면,
            dfs(next)

chk = [False] * (n+1)
dfs(v)
print()

chk = [False] * (n+1)
bfs(v)

