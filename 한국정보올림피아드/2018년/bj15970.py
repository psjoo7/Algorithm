n = int(input())

locNcolor = [list(map(int, input().split())) for _ in range(n)]

distance = 0

def compare(node): # 각 노드간의 거리를 비교하자
    temp = 214700000
    for i in locNcolor: # 모든 노드간에
        if i[1] == locNcolor[node][1] and i[0] != locNcolor[node][0]: # 색깔이 같은 경우만
            temp = min(abs(i[0]-locNcolor[node][0]), temp)
        else : #색깔이 같지않다면
            continue
    return temp

for i in range(n):
    distance += compare(i)

print(distance)