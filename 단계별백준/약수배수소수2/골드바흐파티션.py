import sys
input = sys.stdin.readline

isPrime = [True for i in range(1000001)]
isPrime[0], isPrime[1] = False,False

for i in range(2, int(1000001 ** 0.5) + 1):
    if isPrime[i]:
        for j in range(i*i, 1000001, i):
            isPrime[j] = False

t = int(input())

def gold(number, isPrime):
    goldPartion = 0
    i = 2
    while i <= number//2:
        if isPrime[i] and isPrime[number - i]:
            goldPartion += 1
        i += 1
    return goldPartion

for _ in range(t):
    number = int(input())
    print(gold(number, isPrime))

