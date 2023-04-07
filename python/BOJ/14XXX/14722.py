"""
https://www.acmicpc.net/problem/14722
14722.우유 도시
풀이1.
"""
import sys

input = sys.stdin.readline

n = int(input())
milks = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for x in range(n):
    for y in range(n):
        if milks[x][y] == 0:
            dp[x][y] = 1

for i in range(1, n):
    dp[i][0] = max(dp[i][0], dp[i - 1][0] + (1 if milks[i][0] == (milks[i - 1][0] + 1) % 3 else 0))
    dp[0][i] = max(dp[0][i], dp[0][i - 1] + (1 if milks[0][i] == (milks[0][i - 1] + 1) % 3 else 0))

for x in range(1, n):
    for y in range(1, n):
        dp[x][y] = max(dp[x][y], dp[x - 1][y] + (1 if milks[x][y] == (milks[x - 1][y] + 1) % 3 else 0))
        dp[x][y] = max(dp[x][y], dp[x][y - 1] + (1 if milks[x][y] == (milks[x][y - 1] + 1) % 3 else 0))

print(dp[n - 1][n - 1])
print(dp)
"""
2
1 0
0 0
1
---
2
0 2
0 0
1
"""