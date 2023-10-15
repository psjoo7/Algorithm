# 5로 나누기
# 3으로 나누기
# 2로 나누기
# 1 빼기
n = int(input())
d = [0] * 300001
def makeOne(n):
    if n == 1:
        return 0
    if d[n] != 0:
        return d[n]

    five = three = two = 99999

    if n % 5 == 0:
        five = makeOne(n//5)
    if n % 3 == 0:
        three = makeOne(n//3)
    if n % 2 == 0:
        two = makeOne(n//2)
    d[n] = min(five, three, two, makeOne(n-1)) + 1
    return d[n]

print(makeOne(n))