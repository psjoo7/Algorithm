import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
dp = deque()

for _ in range(n):
    com, *num = input().split()
    if com == 'push_front':
        dp.appendleft(int(num[0]))
    elif com == 'push_back':
        dp.append(int(num[0]))
    elif com == 'pop_front':
        print(dp.popleft() if len(dp) > 0 else -1)
    elif com == 'pop_back':
        print(dp.pop() if len(dp) > 0 else -1)
    elif com == 'size':
        print(len(dp))
    elif com == 'empty':
        print(1 if len(dp) == 0 else 0)
    elif com == 'back' :
        print(dp[-1] if len(dp) > 0 else -1)
    else :
        print(dp[0] if len(dp) > 0 else -1)