n, k = map(int, input().split())

dp = [[0 for col in range(k+1)] for row in range(n+1)]

for i in range(1, k+1):
    dp[0][i] = 1
for i in range(1, n+1):
    for j in range(1, k+1):
        if i == 1:
            dp[i][j] = j
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[n][k] % 1000000000)