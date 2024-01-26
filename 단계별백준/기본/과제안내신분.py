array = []

for i in range(31):
    array.append(i)

for i in range(28):
    n = int(input())
    array[n] = 0

answer = []

for i in range(31):
    if array[i] != 0:
        answer.append(i)

print(answer[0])
print(answer[1])