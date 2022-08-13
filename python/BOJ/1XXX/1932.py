"""
https://www.acmicpc.net/problem/1932
1932.정수 삼각형
풀이2.240ms
"""
import sys

input = sys.stdin.readline

N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = triangle[0][0]
for i in range(N - 1):
    for j in range(i + 1):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])
print(max(dp[N - 1]))
