n, m = map(int, input().split())
n += 1

answer = [0] * n
array = []
for i in range(m):
    array.append(list(map(int, input().split())))

for x in range(m):
    i, j, k = array[x][0], array[x][1], array[x][2]
    for y in range(i, j+1):
        answer[y] = k

for i in range(1,n):
    print(answer[i], end=" ")