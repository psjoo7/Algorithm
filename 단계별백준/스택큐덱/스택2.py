import sys
input = sys.stdin.readline

n = int(input())

def stack(order, answer):
    if order[0] == 1:
        answer.append(order[1])
    elif order[0] == 2:
        if len(answer) != 0:
            print(answer.pop())
        else:
            print(-1)
    elif order[0] == 3:
        print(len(answer))
    elif order[0] == 4:
        if len(answer) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(answer) == 0:
            print(-1)
        else:
            print(answer[-1])
    return answer

answer = list()

for _ in range(n):
    order = list(map(int, input().split()))
    answer = stack(order,answer)