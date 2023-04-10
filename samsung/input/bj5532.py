import math

L, A, B, C, D = [ int(input()) for _ in range(5) ]

x = math.ceil(A/C)
y = math.ceil(B/D)

if x >= y :
    print(L - x)
else : print(L - y)