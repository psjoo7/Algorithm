import sys
input = sys.stdin.readline

n = int(input())
wordArray = []

for i in range(n):
    wordArray.append(str(input().rstrip()))


def recursion(word, start, end, reCnt):
    reCnt += 1
    if start >= end: return 1, reCnt
    elif word[start] != word[end]: return 0, reCnt
    else: return recursion(word, start+1, end-1, reCnt)


def is_palindrome(word):
    reCnt = 0
    return recursion(word, 0, len(word)-1, reCnt)


for i in range(n):
    isPal, cnt = is_palindrome(wordArray[i])
    print(isPal, cnt)