"""
https://www.acmicpc.net/problem/2073
2073.수도배관공사
골드4
풀이2.1084ms
"""
import sys
input = sys.stdin.readline

D, P = map(int, input().split())
pipes = [tuple(map(int, input().split())) for _ in range(P)]
dp = [[0] * (D + 1) for _ in range(2)]

for i in range(P):
    dp[i % 2][pipes[i][0]] = max(dp[i % 2][pipes[i][0]], pipes[i][1])
    for j in range(1, D + 1):
        dp[i % 2][j] = max(dp[i % 2][j], dp[(i + 1) % 2][j])
        if j - pipes[i][0] >= 0:
            dp[i % 2][j] = max(dp[i % 2][j], min(dp[(i + 1) % 2][j - pipes[i][0]], pipes[i][1]))

print(dp[(P - 1) % 2][D])
