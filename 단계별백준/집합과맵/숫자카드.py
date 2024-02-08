n = int(input())
standard = set(map(int, input().split()))
m = int(input())
array = list(map(int, input().split()))

for i in array:
    if i in standard:
        print(1, end=" ")
    else:
        print(0, end=" ")