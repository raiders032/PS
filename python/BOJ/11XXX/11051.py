"""
https://www.acmicpc.net/problem/11051
11051.이항 계수 2
실버1
풀이1.280ms
"""
import sys
sys.setrecursionlimit(10 ** 6)


def bino(n, k):
    if k == 0 or n == k:
        return 1

    if cache[n][k]:
        return cache[n][k]

    cache[n][k] = (bino(n - 1, k - 1) + bino(n - 1, k)) % 10007

    return cache[n][k]


N, K = map(int, input().split())
cache = [[0] * (N + 1) for _ in range(N + 1)]
print(bino(N, K))
