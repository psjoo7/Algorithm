n = int(input())

tile = [0 for _ in range(1000001)]
tile[1] = 1
tile[2] = 2


def zero_one_tile(n):
    if n <= 2:
        return tile[n]

    for i in range(3, n+1):
        tile[i] = (tile[i-1] + tile[i-2]) % 15746
    return tile[n]


result = zero_one_tile(n)
print(result)