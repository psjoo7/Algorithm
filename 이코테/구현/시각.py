# 모든 시각 중 3이 하나라도 포함되어 있는 모든 경우의 수 구하기

n = int(input())
answer = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                answer += 1
print(answer)