n = int(input())
m = int(input())

min = -1
sum = 0

for i in range(n, m+1):
    if i == 1:
        continue
    flag = 0
    for j in range(2,i//2+1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        if min == -1:
            min = i
        sum += i

if min == -1:
    print(min)
else:
    print(sum)
    print(min)