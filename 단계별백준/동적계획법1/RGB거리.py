import sys
input = sys.stdin.readline

n = int(input())
houses = []

for i in range(n):
    r, g, b = map(int, input().split())
    houses.append([r,g,b])

