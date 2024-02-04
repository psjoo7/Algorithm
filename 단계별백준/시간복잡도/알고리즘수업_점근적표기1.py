a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

if a1 * n + a0 > c * n: print(0)
elif a1 * 100 + a0 > c * 100:print(0)
else:
    print(1)