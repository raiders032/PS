import sys
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = board[0][0]
for i in range(1, N):
    dp[0][i] = dp[0][i-1] + board[0][i]
    dp[i][0] = dp[i-1][0] + board[i][0]


def solve(x, y):
    if dp[x][y]:
        return dp[x][y]
    else:
        dp[x][y] = min(solve(x-1, y), solve(x, y-1)) + board[x][y]
        return dp[x][y]


print(solve(N-1, N-1))
