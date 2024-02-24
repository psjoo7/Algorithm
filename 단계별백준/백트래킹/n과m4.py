n, m = map(int, input().split())


def is_m(array, m, n):
    if len(array) == m:
        if sorted(array) == array:
            print(' '.join(map(str, array)))
        return
    for i in range(1, n+1):
        array.append(i)
        is_m(array, m, n)
        array.pop()


is_m([], m, n)