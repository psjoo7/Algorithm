# 수평으로 2칸, 수직으로 한칸
# 수직으로 2칸, 수평으로 한칸
# 이동할 수 있는 경우의 수
n = str(input())
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
count = 0
x, y = row.index(n[0]) + 1, int(n[1])
ways = [(-2,-1), (-2,1), (2,1), (2,-1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

for way in ways:
    nx = x + way[0]
    ny = y + way[1]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        count += 1
print(count)
