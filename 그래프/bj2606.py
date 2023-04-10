from collections import deque

computer = int(input()) # 컴퓨터의 개수
comp = [list() for _ in range(computer + 1)] # 컴퓨터의 연결 정보를 담을 배열
line = int(input()) # 컴퓨터의 연결 정보의 수

for _ in range(line): # 컴퓨터의 연결 정보를 담는데,
    start, end = map(int,input().split())
    comp[start].append(end)
    comp[end].append(start)

# bfs로 탐색할 것이므로, deque() 활용
q = deque()
# 컴퓨터 1에서 출발하므로
q.append(1)
# 컴퓨터가 방문할 기록을 담기 위해
chk = [0] * (computer + 1)
# 컴퓨터 1은 이미 방문했으므로
chk[1] = 1
# 결과를 담을 변수. -1인 이유는 처음에 더할 것이기 때문
res = 0

#bfs 시작
while(q):
    n = q.popleft()
    for i in comp[n]:
        # 아직 방문하지 않은 곳만 들르기
        if chk[i] == 0:
            res += 1
            chk[i] = 1
            q.append(i)


print(res)