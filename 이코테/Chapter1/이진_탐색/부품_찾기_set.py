n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for i in b:
    if i in a:
        print("Yes", end=" ")
    else:
        print("No", end=" ")