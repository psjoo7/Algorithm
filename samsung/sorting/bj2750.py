x = int(input())
y = [int(input()) for _ in range(x)]
answer = sorted(y)

for _ in range(x):
    print(answer[_])