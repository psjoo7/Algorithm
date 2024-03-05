n = int(input())

dp = {0:0, 1:0, 2:1, 3:1}

if n <= 3:
    print(dp[n])
else:
    for i in range(4,n+1):
        a = dp[i-1]
        if i % 3 == 0:
            a = min(a, dp[i//3])
        if i % 2 == 0:
            a = min(a, dp[i//2])
        dp[i] = a + 1
    print(dp[n])