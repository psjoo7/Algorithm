n = int(input())
board = [[-1] * n for _ in range(n)]

def able(board, i, j, n):
    dx = [-1, -1, 1, 1,  1, -1]
    dy = [0,   1, 1, 0, -1, -1]
    for t in range(6):
        x = i
        y = j
        while True:
            x += dx[t]
            y += dy[t]
            if x < 0 or x >= n or y < 0 or y >= n:
                break
            if board[x][y] != -1:
                return False
    return True


def queen(board, i, n):
    # n개의 퀸을 모두 놓았을 때
    if i == n:
        return 1 # 전체 경우의 수 하나를 더해준다
    total = 0
    for j in range(n):
        if able(board, i, j, n):
            board[i][j] = 1
            total += queen(board, i + 1, n)
            board[i][j] = -1
    return total


print(queen(board, 0, n))