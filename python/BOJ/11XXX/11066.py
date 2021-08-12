"""
https://www.acmicpc.net/problem/11066
11066.파일 합치기
골드3
풀이1.2692ms(PyPy3)
"""
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    K = int(input())
    files = list(map(int, input().split()))

    sum = [0] * (K + 1)
    for i in range(1, K + 1):
        sum[i] = sum[i - 1] + files[i - 1]

    dp = [[0] * K for _ in range(K)]
    for j in range(1, K):
        for i in range(K - j):
            dp[i][i + j] = sys.maxsize
            for k in range(i, i + j):
                dp[i][i + j] = min(dp[i][i + j], dp[i][k] + dp[k + 1][i + j] + sum[i + j + 1] - sum[i])

    print(dp[0][K - 1])
