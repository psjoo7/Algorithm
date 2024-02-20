import sys
input = sys.stdin.readline

array = []
arrayDic = dict()

n = int(input())
for _ in range(n):
    temp = int(input())
    array.append(temp)
    if temp not in arrayDic:
        arrayDic[temp] = 1
    else:
        arrayDic[temp] += 1

array.sort()

maxNum = max(arrayDic.values())
second = 0
mode = 0
for i in sorted(set(array)):
    if arrayDic[i] == maxNum:
        mode = i
        second += 1
    if second == 2:
        break

print(round(sum(array)/n))
print(array[n//2])
print(mode)
print(array[-1] - array[0])