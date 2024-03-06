import sys
input = sys.stdin.readline

n = int(input())
array1 = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))

for i in array2:
    if i in array1:
        print(1)
    else:
        print(0)