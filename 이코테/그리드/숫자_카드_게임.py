# N : 행 M : 열
n, m = map(int, input().split())
result = 0
for i in range(n):
    # 행렬 list로 저장하는 방법임
    data = list(map(int, input().split()))
    result = max(result, min(data))

print(result)