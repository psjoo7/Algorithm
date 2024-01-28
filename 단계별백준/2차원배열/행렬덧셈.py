n, m = input().split()
n, m = int(n), int(m)

add1 = []
add2 = []
for i in range(n):
    add1.append(list(map(int, input().split())))
for i in range(n):
    add2.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        add1[i][j] = add1[i][j] + add2[i][j]

for i in range(n):
    for j in range(m):
        print(add1[i][j], end=' ')
    print()