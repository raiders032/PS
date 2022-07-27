"""
https://www.acmicpc.net/problem/1695
1695.팰린드롬 만들기
풀이1.804ms
"""
import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
reversed_numbers = numbers[::-1]
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if numbers[i - 1] == reversed_numbers[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(N - dp[N][N])