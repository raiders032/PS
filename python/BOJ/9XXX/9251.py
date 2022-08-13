"""
https://www.acmicpc.net/problem/9251
9251.LCS
풀이1.688ms
"""
import sys
input = sys.stdin.readline
string1 = input().rstrip()
string2 = input().rstrip()
dp = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]
for i in range(1, len(string1) + 1):
    for j in range(1, len(string2) + 1):
        if string1[i - 1] == string2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(string1)][len(string2)])