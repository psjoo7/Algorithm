import sys
input = sys.stdin.readline

n = int(input())
tri = []

for _ in range(n):
    numbers = list(map(int, input().split()))
    tri.append(numbers)

for i in range(n-1, 0, -1):
    for j in range(len(tri[i])-1):
        tri[i-1][j] = max(tri[i][j], tri[i][j+1]) + tri[i-1][j]

print(tri[0][0])