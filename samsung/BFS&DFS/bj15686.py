N, M = map(int, input().split()) # 도시 크기, 남길 치킨집 수
city = [] # 도시
chicken = [] # 치킨집
home = [] # 집

def distance(chicken): # 거리를 계산하는 함수
    dist = 0
    for r1, c1 in home:
        dist += min([abs(r1 - r2) + abs(c1 - c2) for r2, c2 in chicken])
    return dist

def dfs(L, cur) : # 조합을 만들어 치킨 거리의 최솟값을 찾는 함수
    global min_dist
    if L == M :
        select_chicken = [chicken[i] for i in range(chilen) if visited[i]]
        print(" selection : ", select_chicken)
        min_dist = min(min_dist, distance(select_chicken))
        print(" min_dist : ", min_dist)
        return

    for i in range(cur, chilen) :
        if visited[i] == 0:
            visited[i] = 1
            dfs(L + 1, i + 1)
            visited[i] = 0

for r in range(N):
    temp = list(map(int, input().split()))
    city.append(temp)
    for c in range(N):
        if temp[c] == 2: # 치킨집인 경우
            chicken.append((r,c))
        elif temp[c] == 1: #집인 경우
            home.append((r,c))

if len(chicken) == M: # 폐업할 필요가 없는 경우
    print(distance(chicken))
else : # 폐업을 할 필요가 있어서 치킨 거리의 최솟값을 찾아야할 경우
    min_dist = 2145000000 # 대략적인 큰수
    chilen = len(chicken)
    visited = [0] * chilen
    dfs(0, 0)
    print(min_dist)