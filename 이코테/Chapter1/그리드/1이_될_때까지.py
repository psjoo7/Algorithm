# 1이 될때까지 두 과정 중 하나를 반복적으로 선택해서 최단 횟수를 찾는 문제
# "최대한 많이 나누기"

n, k = map(int, input().split())
answer = 0
while n != 1 :
    answer += 1
    if n % k != 0 :
        n -= 1
    else :
        n = n/k

print(answer)