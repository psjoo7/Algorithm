import sys

n, k = map(int, input().split())
coin = []
dp = [0 for i in range(k+1)]
for i in range(n):
    coin.append(int(input()))

for i in range(1, k+1):
    #경우의 수를 담을 스택 만들어야함
    a = []
    #단위별로 뺐을 때, -1인 경우의 수가 있으면 그냥 안되는 거
    #단위별로 뺐을 때, 단위별로 뺀거(+1) + 뺀 경우
    for j in coin:
        if j <= i and dp[i-j] != -1:
            a.append(dp[i-j])
    if not a:
        dp[i] = -1
    else:
        dp[i] = min(a) + 1
print(dp[k])

# n, k = map(int, input().split())
# coin = []
# dp = [10001 for i in range(k+1)]
# dp[0] = 0
# for i in range(n):
#     coin.append(int(input()))
#
# for c in coin:
#     for i in range(c, k+1):
#         if dp[i] > 0:
#             dp[i] = min(dp[i], dp[i-c] + 1)
#
# if dp[k] == 10001:
#     print(-1)
# else:
#     print(dp[k])