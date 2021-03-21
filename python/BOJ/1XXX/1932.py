"""
1932.정수 삼각형
실버1
다이나믹 프로그래밍
"""
import sys

input = sys.stdin.readline
N = int(input())
board = []
dp = [[0] * N for _ in range(N)]
for _ in range(N):
    row = list(map(int, input().rstrip().split()))
    board.append(row)
dp[0][0] = board[0][0]
for row in range(N - 1):
    for col in range(row + 1):
        dp[row + 1][col] = max(dp[row + 1][col], dp[row][col] + board[row + 1][col])
        dp[row + 1][col + 1] = max(dp[row + 1][col + 1], dp[row][col] + board[row + 1][col + 1])
print(max(dp[N - 1]))
