import sys
input = sys.stdin.readline
n = int(input())

max_x = -sys.maxsize
max_y = -sys.maxsize
min_x = sys.maxsize
min_y = sys.maxsize

for i in range(n):
    x, y = map(int, input().split())
    if max_x < x:
        max_x = x
    if max_y < y:
        max_y = y
    if min_x > x:
        min_x = x
    if min_y > y:
        min_y = y

if n == 1 :
    print(0)
else:
    x = max_x - min_x
    y = max_y - min_y

    print(x*y)