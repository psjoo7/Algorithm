#인접리스트 구현하기
# 인접 리스트란?
# 각각의 노드에 연결된 노드들을 원소로 갖는 리스트들의 배열
# 장점: 실제로 연결된 노드에 대한 정보만 저장한다.
#      따라서 모든 벡터들의 원소의 개수의 합과 간선의 개수가 동일
# 단점: 노드 i 와 노드 j 의 연결 여부를 알고 싶을 경우에는 어떻게 해야할까?
#      adj[i]의 리스트를 모두 순회해서 찾아야하기 때문에 O(V)의 시간 복잡도를 갖는다
#      (인접 행렬의 경우 O(1))
from sys import stdin

node, edge = map(int, stdin.readline().split())

adj = [ [] for _ in range(node)]

for _ in range(edge):
    src, dest = map(int, stdin.readline().split())
    adj[src].append(dest)
    adj[dest].append(src)

print(adj)