"""
https://www.acmicpc.net/problem/1581
1581.락스타 락동호
풀이1.
"""
song = list(map(int, input().split()))
dp = [[[[[[0] * 1001 for _ in range(1001)] for _ in range(1001)] for _ in range(1001)] for _ in range(4)] for _ in range(4001)]
if song[0]:
    dp[1][0][1][0][0][0] = 1
if song[1]:
    dp[1][1][0][1][0][0] = 1

for i in range(2, 4001):
    dp[i][0]