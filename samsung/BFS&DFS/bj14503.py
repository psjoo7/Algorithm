n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

#처음 방문하는 곳 처리
visited[r][c] = 1
cnt = 1

while 1:
    flag = 0
    # 4방향 확인
    for _ in range(4):
        # 0, 3, 2, 1 순서를 부여해야함
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        # 한번 돌았으면 그 방향으로 출발
        d = (d+3) % 4
        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                #청소를 한 방향이라도 했다면 다음으로 넘어간다
                flag = 1
                break
    if flag == 0 : # 4방향 모두 청소가 되어있다는 뜻
        if room[r-dx[d]][c-dy[d]] == 1: #후진했는데 벽
            print(cnt)
            break
        else:
            r, c = r-dx[d], c-dy[d]