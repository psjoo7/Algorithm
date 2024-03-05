'''
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
dp[2] = [0, dp[1][0] + dp[1][2], ... dp[9][8]]
'''
n = int(input())

dp = [[0 for _ in range(10)] for _ in range(101)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
dp[2] = [0, 2, 2, 2, 2, 2, 2, 2, 2, 1]
if n <= 2:
    print(sum(dp[n]))
else:
    for i in range(3, n+1):
        dp[i][1] = dp[i-2][1] + dp[i-1][2]
        dp[i][2] = dp[i-1][1] + dp[i-1][3]
        dp[i][3] = dp[i-1][2] + dp[i-1][4]
        dp[i][4] = dp[i-1][3] + dp[i-1][5]
        dp[i][5] = dp[i-1][4] + dp[i-1][6]
        dp[i][6] = dp[i-1][5] + dp[i-1][7]
        dp[i][7] = dp[i-1][6] + dp[i-1][8]
        dp[i][8] = dp[i-1][7] + dp[i-1][9]
        dp[i][9] = dp[i-1][8]
    print(sum(dp[n]) % 1000000000)