n = str(input())
array = []
for i in range(len(n)): array.append(int(n[i]))

array.sort(reverse=True)
for i in array: print(i, end="")