array = list()
for i in range(5):
    array.append(int(input()))
array.sort()
print(sum(array)//5)
print(array[2])