n, k = map(int, input().split())
answer = 0
while n != 1 :
    answer += 1
    if n % k != 0 :
        n -= 1
    else :
        n = n/k

print(answer)