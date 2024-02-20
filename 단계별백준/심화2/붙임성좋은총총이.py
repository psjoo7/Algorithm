import sys
input = sys.stdin.readline

n = int(input())

array = set()
start = False
for _ in range(n):
    i, j = input().split()
    if not start:
        if i == 'ChongChong' or j == 'ChongChong':
            array.add(i)
            array.add(j)
            start = True
    if start:
        if i in array:
            array.add(j)
        if j in array:
            array.add(i)

print(len(array))