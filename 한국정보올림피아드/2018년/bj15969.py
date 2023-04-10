n = int(input())
score = list(map(int, input().split()))

score.sort()
print(score[-1] - score[0])