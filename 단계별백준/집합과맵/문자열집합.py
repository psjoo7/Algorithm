n, m = map(int, input().split())
s = []

for i in range(n):
    temp = str(input())
    s.append(temp)

answer = 0
for i in range(m):
    temp = str(input())
    if temp in s:
        answer += 1

print(answer)