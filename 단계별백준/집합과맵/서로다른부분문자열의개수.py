import sys
input = sys.stdin.readline

word = str(input().strip())
n = len(word)
array = set()

i = 1
while 1:
    if i > len(word):
        break
    for j in range(n):
        if j+i <= n:
            array.add(word[j:j+i])
    i += 1

print(len(array))