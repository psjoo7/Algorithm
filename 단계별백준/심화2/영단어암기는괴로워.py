'''
1. 자주 나오는 단어 - 앞
2. 길이가 길수록 - 앞
3. 사전 순
'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
d = {}
for _ in range(n):
    word = str(input().rstrip())
    if len(word) < m:
        continue
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

d = sorted(d.items(), key=lambda x: x[0])
d = sorted(d, key=lambda x: (x[1], len(x[0])), reverse=True)
for i in range(len(d)):
    print(d[i][0])