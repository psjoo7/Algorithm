import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] * 301
for i in range(1, n + 1):
    stairs[i] = int(input())
dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[2] + stairs[1]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

'''
F(n) = max(stairs[n] + stairs[n-1] + F(n-3), stairs[n] + F(n-2))
'''
for i in range(4, n+1):
    dp[i] = max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2])

print(dp[n])