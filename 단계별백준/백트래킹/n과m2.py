n, m = map(int, input().split())


def able(array, num):
    return num not in array


def is_m(array, m, n):
    if len(array) == m and sorted(array) == array:
        print(' '.join(map(str, array)))
        return
    for i in range(1, n+1):
        if able(array, i):
            array.append(i)
            is_m(array, m, n)
            array.pop()


is_m([], m, n)