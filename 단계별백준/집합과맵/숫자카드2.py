import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
array = map(int, input().split())

standardArray = Counter(array)

m = int(input())
array = map(int, input().split())

for i in array:
    print(standardArray.get(i, 0), end=' ')