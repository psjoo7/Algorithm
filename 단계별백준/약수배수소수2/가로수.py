import sys
input = sys.stdin.readline

t = int(input())
array = [0] * t
for i in range(t):
    array[i] = int(input())

array2 = [0] * (t-1)

for i in range(t-1):
    array2[i] = array[i+1] - array[i]

def ucli(a,b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return ucli(b, a%b)

a = array2[0]
for i in array2:
    a = ucli(a,i)
answer = 0
for i in array2:
    answer += (i-a)//a
print(answer)