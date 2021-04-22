"""
https://programmers.co.kr/learn/courses/30/lessons/12913
땅따먹기
DP
풀이1
"""


def solution(land):
    dp = [[0] * 4 for _ in range(len(land))]
    dp[0] = land[0]

    for i in range(len(land) - 1):
        for j in range(4):
            for k in range(4):
                if j == k:
                    continue
                dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + land[i + 1][k])

    return max(dp[len(land) - 1])