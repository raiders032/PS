"""
https://www.acmicpc.net/problem/17845
17845.수강 과목
골드5
풀이1.
"""
import sys


def solve(K, N):
    if K == 0 or N == 0:
        return 0

    if cache[K][N] == -1:
        cache[K][N] = solve(K - 1, N)
        if times[K] <= N:
            cache[K][N] = max(cache[K][N], solve(K - 1, N - times[K]) + priorities[K])

    return cache[K][N]


input = sys.stdin.readline
N, K = map(int, input().split())
priorities = [0]
times = [0]

for _ in range(K):
    priority, time = map(int, input().split())
    priorities.append(priority)
    times.append(time)

cache = [[-1] * (N + 1) for _ in range(K + 1)]

print(solve(K, N))