import sys
input = sys.stdin.readline


array = [[[-1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
for i in range(20):
    for j in range(20):
        for k in range(20):
            if i == 0 or j == 0 or k == 0:
                array[i][j][k] = 1


def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    if array[a][b][c] != -1:
        return array[a][b][c]
    if a < b < c:
        result = w(a,b,c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        result = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    array[a][b][c] = result
    return result

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w({}, {}, {}) =".format(a,b,c),end=" ")
    print(w(a,b,c))
