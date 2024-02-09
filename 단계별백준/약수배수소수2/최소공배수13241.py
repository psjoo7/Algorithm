import sys

input = sys.stdin.readline

def ans(a,b):
    if a < b :
        a , b = b , a
    if a % b == 0:
        return b
    return ans(b, a%b)

a, b = map(int, input().split())
if ans(a,b) == 1:
    print(a * b)
else:
    print((a*b)//ans(a,b))