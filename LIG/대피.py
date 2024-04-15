from itertools import combinations
from collections import deque
n, k = map(int, input().split())
location = []
for _ in range(n):
    location.append(list(map(int,input().split())))


def get_distance(loc1, loc2):
    x = abs(loc1[0] - loc2[0])
    y = abs(loc1[1] - loc2[1])

    return x+y


dis_info = []
for i in range(n):
    distance = []
    for j in range(n):
        distance.append(get_distance(location[i], location[j]))
    dis_info.append(distance)

for comb in combinations(range(n), k):
    print(comb)
