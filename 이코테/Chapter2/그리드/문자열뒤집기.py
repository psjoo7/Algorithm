array = list(map(int, input()))
count = 1
isZero = array[0]
for i in array:
    if isZero != i:
        isZero = i
        count += 1

print(int(count / 2))