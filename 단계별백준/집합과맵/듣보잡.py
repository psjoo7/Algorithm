import sys

input = sys.stdin.readline

n, m = map(int, input().split())
listen = set()
seen = set()

for _ in range(n):
    listen.add(input().strip())
for _ in range(m):
    seen.add(input().strip())
answer = list(listen & seen)
answer.sort()
print(len(answer))
print(*answer, sep='\n')