import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 10001
wines = [0] * 10001

for i in range(1, n+1):
    wines[i] = int(input())

dp[1] = wines[1]
dp[2] = wines[2]+wines[1]
for i in range(3, n+1):
    dp[i] = max(wines[i] + wines[i-1] + dp[i-3], wines[i] + dp[i-2], dp[i-1])

print(dp[n])