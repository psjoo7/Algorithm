# 여러 개의 카드 중 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임
# "각 행마다 가장 작은 수를 찾은 뒤, 그 수에서 가장 큰 수를 찾는 것"

# N : 행 M : 열
n, m = map(int, input().split())
result = 0
for i in range(n):
    # 행렬 list로 저장하는 방법임
    data = list(map(int, input().split()))
    result = max(result, min(data))

print(result)