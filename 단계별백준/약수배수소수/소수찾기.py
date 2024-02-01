n = int(input())
answer = n
array = map(int, input().split())
for i in array:
    if i == 1:
        answer -= 1
        continue
    for j in range(2,i):
        if i % j == 0:
            answer -= 1
            break

print(answer)