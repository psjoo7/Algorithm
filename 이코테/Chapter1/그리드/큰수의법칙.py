# 가장 큰 수를 K번 까지만 더해서 총 M번 더하는 문제
# "가장 큰 수를 K 번 더하고, 두 번째로 큰 수를 한 번 더하는 방법"
# 배열의 크기 : N ( 2, 1000 )
# 숫자가 더해지는 횟수 : M ( 1, 10000 )
# 연속으로 더할 수 있는 횟수 K ( 1, 10000 )

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
answer = 0
first = data[n - 1]
second = data[n - 2]
idx = 0
for i in range(m):
    if idx < k:
        answer += first
        idx += 1
    else:
        answer += second
        idx = 0
print(answer)

# 이 방법은 시간 초과가 나기 쉽다.