m = -1
x, y = -1, -1

for i in range(9):
    array = list(map(int, input().split()))
    if m < max(array):
        m = max(array)
        x, y = i, array.index(max(array))

print(m)
print(x+1, y+1)