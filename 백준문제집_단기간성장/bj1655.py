# 가운데를 말해요.
# 정수를 하나씩 외칠때마다, 그 중 중간값을 말하는 게임
# --- 외친 수의 개수가 짝수개일땐 중간에 있는 두 수 중 작은 수를 말해야한다.

N = int(input()) # 외칠 정수의 개수( N <= 1 <= 100,000
numbers = [int(input()) for _ in range(N)]

