import sys
input = sys.stdin.readline


def merge(array, start, mid, end):
    global k
    global a
    i, j, t = start, mid+1, 0
    temp = [0] * a
    while i <= mid and j <= end:
        if array[i] <= array[j]:
            temp[t] = array[i]
            t += 1
            i += 1
        else:
            temp[t] = array[j]
            t += 1
            j += 1
    while i <= mid:
        temp[t] = array[i]
        t += 1
        i += 1
    while j <= end:
        temp[t] = array[j]
        t += 1
        j += 1
    i = start
    t = 0
    while i <= end:
        array[i] = temp[t]
        k -= 1
        if k == 0:
            print(temp[t])
            break
        i += 1
        t += 1
    return k


def merge_sort(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid+1, end)
        merge(array, start, mid, end)


a, k = map(int, input().split())
array = list(map(int, input().split()))
merge_sort(array, 0, len(array) - 1)
if k > 0:
    print(-1)