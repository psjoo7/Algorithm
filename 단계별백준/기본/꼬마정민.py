array = list(map(int, input().split()))
answer = 0
for i in range(3):
    answer += array[i]

print(answer)