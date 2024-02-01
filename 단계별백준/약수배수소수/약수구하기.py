n, k = map(int, input().split())

array = []

mid = n // 2
for i in range(1, mid+1):
    if n % i == 0:
        array.append(i)

array.append(n)

if len(array) < k:
    print(0)
else:
    print(array[k-1])