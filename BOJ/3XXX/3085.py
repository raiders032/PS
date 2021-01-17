'''
3085번 사탕게임 실버4
브루트포스
'''
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0
N = int(input())
board = [list(input()) for _ in range(N)]


def getCandy():
    res = 0
    for i in range(N):
        count = 1
        for j in range(N - 1):
            if board[i][j] == board[i][j+1]:
                count += 1
            else:
                res = max(res, count)
                count = 1
        res = max(res, count)

        count = 1
        for j in range(N - 1):
            if board[j][i] == board[j+1][i]:
                count += 1
            else:
                res = max(res, count)
                count = 1
        res = max(res, count)
    return res


for i in range(0, N * N, 2):
    for d in range(4):
        x = i // N
        y = i % N
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            continue
        board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
        res = max(res, getCandy())
        board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
print(res)
