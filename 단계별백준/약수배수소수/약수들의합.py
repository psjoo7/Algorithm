while True:
    t = int(input())
    if t == -1:
        break
    array = []
    mid = t // 2
    for i in range(1, mid+1):
        if t % i == 0:
            array.append(i)
    compare = 0
    for i in array:
        compare += i
    if compare == t:
        print(t, '=', end=" ")
        for i in range(len(array)-1):
            print(array[i], end=" + ")
        print(array[len(array)-1])
    else:
        print(t, 'is NOT perfect.')