from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
deq = deque()

for _ in range(n):
    array = input().split()
    if array[0] == '1':
        deq.appendleft(array[1])
    elif array[0] == '2':
        deq.append(array[1])
    elif array[0] == '3':
        if len(deq) != 0:
            print(deq.popleft())
        else:
            print(-1)
    elif array[0] == '4':
        if len(deq) != 0:
            print(deq.pop())
        else:
            print(-1)
    elif array[0] == '5':
        print(len(deq))
    elif array[0] == '6':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif array[0] == '7':
        if len(deq) != 0:
            print(deq[0])
        else:
            print(-1)
    elif array[0] == '8':
        if len(deq) != 0:
            print(deq[-1])
        else:
            print(-1)