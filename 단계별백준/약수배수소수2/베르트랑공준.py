import sys
input = sys.stdin.readline

while True:
    number = int(input().strip())
    if number == 0:
        break
    isPrime = [True for _ in range(number*2+1)]
    isPrime[0], isPrime[1] = False, False

    for i in range(2, int((number*2)**0.5)+1):
        if isPrime[i]:
            for j in range(i*i, number*2+1, i):
                isPrime[j] = False

    # for i in range(number):
    #     isPrime[i] = False
    # answer = 0
    # for i in range(number * 2 + 1):
    #     if isPrime[i]:
    #         answer += 1
    answer = sum(1 for i in range(number+1, number*2+1) if isPrime[i])
    print(answer)