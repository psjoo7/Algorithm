n, m = map(int, input().split())
n += 1

answer = []
for i in range(n):
    answer.append(i)

array = []
for i in range(m):
    array.append(list(map(int, input().split())))

for x in range(m):
    i, j = array[x][0], array[x][1]
    while(i < j):
        answer[i], answer[j] = answer[j], answer[i]
        i += 1
        j -= 1

for i in range(1,n):
    print(answer[i], end=" ")