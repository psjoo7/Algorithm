n, m, k = map(int, input().split())
data = map(int, input().split())

# 가장 큰 수를 K 번, 두번째 큰 수를 1번 더하는게 패턴임
# 따라서 m / k+1 만큼 더해주고, 나머지만큼 가장 큰 수를 곱해주면 됨

data.sort()
first = data[n - 1]
second = data[n - 2]
arr = first * k + second
answer = arr * (m / (k+1)) + first * (m % (k + 1))
print(answer)