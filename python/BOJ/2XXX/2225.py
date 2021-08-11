"""
https://www.acmicpc.net/problem/2225
2225.합분해
골드5
다이나믹프로그래밍
풀이3.1104ms
"""
N, K = map(int, input().split())
table = [[1] * (K + 1) for _ in range(N + 1)]

for j in range(2, K + 1):
    for i in range(N + 1):
        table[i][j] = 0
        for k in range(i + 1):
            table[i][j] += table[i - k][j - 1]
        table[i][j] %= 1000000000

print(table[N][K])
