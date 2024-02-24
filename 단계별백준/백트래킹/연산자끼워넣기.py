'''
0 : +
1 : -
2 : x
3 : %
'''

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
op = list(map(int, input().split()))


def solution(op, answer, results):
    if op == [0, 0, 0, 0]:
        results.append(answer[:])
        return answer
    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            answer.append(i)
            solution(op, answer, results)
            op[i] += 1
            answer.pop()


results = []
solution(op, [], results)

temp = []
for result in results:
    num = array[0]
    for i in range(1,n):
        if result[i-1] == 0:
            num += array[i]
        if result[i-1] == 1:
            num -= array[i]
        if result[i-1] == 2:
            num *= array[i]
        if result[i-1] == 3:
            if num < 0:
                num = -num
                num //= array[i]
                num = -num
            else:
                num //= array[i]
    temp.append(num)

print(max(temp))
print(min(temp))