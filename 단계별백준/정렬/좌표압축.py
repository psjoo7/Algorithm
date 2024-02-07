import copy

n = int(input())
array = list(map(int,input().split()))
'''
배열의 얕은 복사 ( 실제로는 복사가 아닌 연결, copy()로도 가능 )
tempArray = array
'''
# 이 경우 깊은 복사가 필요
tempArray = copy.deepcopy(array)
tempArray.sort()
array2 = dict()
index = 0
for i in tempArray:
    if not i in array2:
        array2[i] = index
        index += 1
for i in array:
    print(array2[i], end=" ")