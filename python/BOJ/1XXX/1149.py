"""
https://www.acmicpc.net/problem/1149
1149.RGB거리
풀이1.48ms
"""
import sys

input = sys.stdin.readline

n = int(input())
colors = [list(map(int, input().split())) for _ in range(n)]
dp = [[[sys.maxsize] * 3 for _ in range(3)] for _ in range(n)]
dp[0][0][0] = colors[0][0]
dp[0][1][1] = colors[0][1]
dp[0][2][2] = colors[0][2]

for row in range(1, n - 1):
    for color in range(3):
        for first_color in range(3):
            dp[row][color][first_color] = min(dp[row - 1][(color + 1) % 3][first_color],
                                              dp[row - 1][(color + 2) % 3][first_color])
            if dp[row][color][first_color] != sys.maxsize:
                dp[row][color][first_color] += colors[row][color]

if n > 2:
    for color in range(3):
        for first_color in range(3):
            dp[n - 1][color][first_color] = min(dp[n - 2][(color + 1) % 3][(first_color + 1) % 3],
                                                dp[n - 2][(color + 1) % 3][(first_color + 2) % 3],
                                                dp[n - 2][(color + 2) % 3][(first_color + 1) % 3],
                                                dp[n - 2][(color + 2) % 3][(first_color + 2) % 3])
            if dp[n - 1][color][first_color] != sys.maxsize:
                dp[n - 1][color][first_color] += colors[n - 1][color]

answer = sys.maxsize
for colors in dp[n - 1]:
    answer = min(answer, min(colors))

print(answer)
