import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

array = deque()
for _ in range(n):
    order = input().split()
    if order[0] == 'push':
        array.append(order[1])
    if order[0] == 'pop':
        if len(array) == 0:
            print(-1)
        else:
            print(array.popleft())
    if order[0] == 'size':
        print(len(array))
    if order[0] == 'empty':
        if len(array) == 0 :
            print(1)
        else:
            print(0)
    if order[0] == 'front':
        if len(array) == 0:
            print(-1)
        else:
            print(array[0])
    if order[0] == 'back':
        if len(array) == 0:
            print(-1)
        else:
            print(array[-1])