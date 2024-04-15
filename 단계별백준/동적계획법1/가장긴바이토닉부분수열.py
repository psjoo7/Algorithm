n = int(input())
numbers = list(map(int, input().split()))
dp_up = [1 for _ in range(n)] # 상승중일 때 개수, 하락중일 때 개수
dp_down = [1 for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(1,n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp_up[i] = max(dp_up[i], dp_up[j] + 1)

for i in range(n-2, -1, -1):
    for j in range(n-1, i-1, -1):
        if numbers[i] > numbers[j]:
            dp_down[i] = max(dp_down[i], dp_down[j] + 1)
for i in range(1,n):
    num_list = []
    for j in range(i, n):
        if numbers[i] > numbers[j]:
            num_list.append(dp_down[j])
    max_down = 0
    if len(num_list) != 0:
        max_down = max(num_list)
    max_up = max(dp_up[:i+1])
    dp[i] = max_down + max_up

if max(dp_down) == n or max(dp_up) == n:
    print(n)
else:
    print(max(dp))