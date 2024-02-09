import sys
input = sys.stdin.readline

t = int(input())

def ans(a,b):
    if a < b :
        a , b = b , a
    if a % b == 0:
        return b
    return ans(b, a%b)

for _ in range(t):
    a, b = map(int, input().split())
    최대공약수 = ans(a,b)
    if 최대공약수 == 1:
        print(a * b)
    else:
        print((a * b) // 최대공약수)