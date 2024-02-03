def make_triangle(array):
    if array[0] + array[1] > array[2]:
        return print(sum(array))
    return print((array[0]+array[1])*2 - 1)

array = list(map(int,input().split()))
array.sort()

make_triangle(array)