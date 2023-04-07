"""
https://www.acmicpc.net/problem/2157
2157.여행
골드4
풀이2
"""
import sys
input = sys.stdin.readline


def solve(vertex, level):
    print(f'vertex:{vertex}, level:{level}')
    if dp[vertex][level] != -1:
        return dp[vertex][level]
    if level == 0:
        return 0

    dp[vertex][level] = 0
    for pre_vertex, weight in graph[vertex]:
        dp[vertex][level] = max(dp[vertex][level], solve(pre_vertex, level - 1) + weight)

    return dp[vertex][level]


N, M, K = map(int, input().split())
graph = [list() for _ in range(N + 1)]
dp = [[-1] * (M + 1) for _ in range(N + 1)]

for _ in range(K):
    v1, v2, w = map(int, input().split())
    if v1 > v2:
        continue
    dp[v2][1] = max(dp[v2][1], w)
    graph[v2].append((v1, w))


print(solve(N, M))
print(dp)
