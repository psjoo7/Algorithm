from collections import deque
import sys

input = sys.stdin.readline()

A, B = map(int, input.split())

q = deque()
q.append((A, 1))

while(q):
    n, t = q.popleft()
    if n > B: # 숫자가 오바해버린 상황
        continue
    if n == B: # 숫자가 딱 맞는 상황, 가중치를 보여주면 됨
        print(t)
        break
    q.append((int(str(n) + "1"), t+1))
    q.append((n * 2, t+1))
else:
    print(-1)