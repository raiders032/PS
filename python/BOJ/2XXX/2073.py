"""
https://www.acmicpc.net/problem/2073
2073.수도배관공사
풀이1.1616ms(pypy3)
"""
import sys
input = sys.stdin.readline

D, P = map(int, input().split())
pipes = [tuple()] + [tuple(map(int, input().split())) for _ in range(P)]
dp = [[0] * (D + 1) for _ in range(P + 1)]

for i in range(1, P + 1):
    dp[i][pipes[i][0]] = max(dp[i - 1][pipes[i][0]], pipes[i][1])
    for j in range(D + 1):
        dp[i][j] = max(dp[i][j], dp[i - 1][j])
        if j < pipes[i][0] or not dp[i - 1][j - pipes[i][0]]:
            continue
        dp[i][j] = max(dp[i][j], min(dp[i - 1][j - pipes[i][0]], pipes[i][1]))

print(dp[P][D])