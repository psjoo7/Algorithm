n = int(input())

answer = []

array = []
for i in range(n):
    array.append(list(map(str, input())))

answer.append(array[0])
for i in range(1,n):
    for j in range(len(array[i])):
        if answer[0][j] != array[i][j]:
            answer[0][j] = '?'
for i in range(len(answer[0])):
    print(answer[0][i], end='')