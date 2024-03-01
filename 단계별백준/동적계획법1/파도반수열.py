import sys
input = sys.stdin.readline

n = int(input())
array = [0 for _ in range(101)]
array[1] = 1
array[2] = 1
array[3] = 1
array[4] = 2
array[5] = 2


def pado(number):
    if number <= 5:
        return array[number]

    if array[number] != 0:
        return array[number]

    for i in range(6, number+1):
        array[i] = array[i-1] + array[i-5]

    return array[number]


for i in range(n):
    t = int(input())
    print(pado(t))