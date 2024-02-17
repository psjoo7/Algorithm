n, k = map(int, input().split())
temp = k
array = [k]
add = 0
a = 1
while 1:
    if len(array) == n:
        break
    if temp not in array and add == k:
        array.append(temp)
        add = 0
    temp += 1
    if temp == n+1:
        temp = 1
    if temp not in array:
        add += 1

print('<',end='')
for i in range(n-1):
    print(array[i], end=', ')

print(array[n-1], end='')
print('>')