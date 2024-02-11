import sys
input = sys.stdin.readline

m, n = map(int, input().split())

# def find(number):
#     if number == 1:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# for i in range(m, n+1):
#     if find(i):
#         print(i)

isPrime = [True for _ in range(n+1)]
isPrime[0], isPrime[1] = False, False

for i in range(2,n+1):
    if not isPrime[i]:
        continue
    for j in range(i*i, n+1, i):
        isPrime[j] = False

for i in range(m):
    isPrime[i] = False

for i in range(n+1):
    if isPrime[i]:
        print(i)