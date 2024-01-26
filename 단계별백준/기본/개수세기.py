n = int(input())
array = list(map(int, input().split()))
num = int(input())
answer = 0

for i in range(n):
    if num == array[i]:
        answer += 1

print(answer)