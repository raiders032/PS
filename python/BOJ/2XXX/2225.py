"""
https://www.acmicpc.net/problem/2225
2225.합분해
골드5
다이나믹프로그래밍
풀이1.1728ms
"""


N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N + 1)]

for i in range(0, N + 1):
    dp[i][1] = 1

for i in range(1, K + 1):
    dp[0][i] = 1

for select_count in range(2, K + 1):
    for num in range(1, N + 1):
        for last_selected_num in range(0, num + 1):
            dp[num][select_count] += dp[num - last_selected_num][select_count - 1]
            dp[num][select_count] %= 1000000000

print(dp[N][K])