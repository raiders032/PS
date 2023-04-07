"""
https://www.acmicpc.net/problem/1520
1520.내리막 길
골드4
풀이4.220ms
"""
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def get_route(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    if x == 0 and y == 0:
        return 1

    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if board[x][y] >= board[nx][ny]:
            continue
        dp[x][y] += get_route(nx, ny)
    return dp[x][y]


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
print(get_route(N - 1, M - 1))
# print(dp)