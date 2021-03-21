'''
3085번 사탕게임
실버4
브루트포스
2번째 풀이 364ms
'''
import sys


def check_length(x, y):
    global res
    row_cnt = 1
    col_cnt = 1
    for i in range(1, N):
        if board[x][i] == board[x][i - 1]:
            col_cnt += 1
        else:
            col_cnt = 1
        res = max(res, col_cnt)
    for i in range(1, N):
        if board[i][y] == board[i - 1][y]:
            row_cnt += 1
        else:
            row_cnt = 1
        res = max(res, row_cnt)


input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
res = 1
for x in range(N):
    for y in range(N):
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
            check_length(x, y)
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
print(res)
