n = int(input())
array = [['*'] * n for _ in range(n)]
def star(x, y, n, array):
    if n == 1:
        return array
    n //= 3
    for i in range(x + n, x + n*2):
        for j in range(y + n, y + n*2):
            array[i][j] = ' '

    for i in range(0, 3):
        for j in range(0, 3):
            if i == 1 and j == 1:
                continue
            star(x + n * i, y + n * j, n, array)
    return array


star(0, 0, n, array)
for row in array:
    print(''.join(row))