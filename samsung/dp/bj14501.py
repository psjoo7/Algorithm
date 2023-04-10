n = int(input()) # 총 일수

t = []
p = []
dp = [0 for _ in range(n+1)]

for _ in range(n):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)

for i in range(n-1, -1, -1): # 뒤에서 거꾸로
    if t[i] + i > n: # 상담에 필요한 일수가 초과 일수를 넘어가면
        dp[i] = dp[i+1] # 다음날 값을 그대로 가져온다.
    else : # 오늘 상담을 할 경우와 안할 경우를 비교해보기
        dp[i] = max(dp[i+1], dp[t[i] + i] + p[i])

print(dp[0])