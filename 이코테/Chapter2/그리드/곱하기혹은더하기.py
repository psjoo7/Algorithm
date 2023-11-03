n = list(map(int, input()))

answer = 1
for i in n:
    if i != 0:
        answer *= i

print(answer)