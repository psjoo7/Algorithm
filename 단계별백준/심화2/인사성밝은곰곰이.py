import sys
input = sys.stdin.readline

n = int(input())

array = dict()
answer = 0
for _ in range(n):
    nickname = input().strip()
    if nickname == 'ENTER':
        array = dict()
        continue
    if nickname not in array:
        array[nickname] = 0
        answer += 1

print(answer)