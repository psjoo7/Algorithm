from math import factorial

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(factorial(m)// (factorial(n) * factorial(m-n)))