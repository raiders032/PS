"""
https://www.acmicpc.net/problem/11048
11048.이동하기
실버1
다이나믹 프로그래밍
풀이1.2992ms
"""
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = board[0][0]
dx = [0, 1, 1]
dy = [1, 1, 0]
for x in range(N):
    for y in range(M):
        for dir in range(3):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if nx >= N or ny >= M:
                continue
            dp[nx][ny] = max(dp[nx][ny], dp[x][y] + board[nx][ny])
print(dp[N - 1][M - 1])