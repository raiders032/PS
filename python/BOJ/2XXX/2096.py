"""
https://www.acmicpc.net/problem/2096
2096.내려가기
골드4
풀이1.956ms
"""
import sys

input = sys.stdin.readline
N = int(input())

dp = [[[0] * 3 for _ in range(2)] for _ in range(2)]

nums = list(map(int, input().split()))
dp[0][0][0] = dp[1][0][0] = nums[0]
dp[0][0][1] = dp[1][0][1] = nums[1]
dp[0][0][2] = dp[1][0][2] = nums[2]

for x in range(1, N):
    nums = list(map(int, input().split()))
    x %= 2
    for y in range(3):
        dp[0][x][y] = dp[0][x ^ 1][y]
        dp[1][x][y] = dp[1][x ^ 1][y]

        if y:
            dp[0][x][y] = max(dp[0][x][y], dp[0][x ^ 1][y - 1])
            dp[1][x][y] = min(dp[1][x][y], dp[1][x ^ 1][y - 1])

        if y < 2:
            dp[0][x][y] = max(dp[0][x][y], dp[0][x ^ 1][y + 1])
            dp[1][x][y] = min(dp[1][x][y], dp[1][x ^ 1][y + 1])

        dp[0][x][y] += nums[y]
        dp[1][x][y] += nums[y]

print(max(dp[0][(N + 1) % 2]), min(dp[1][(N + 1) % 2]))
