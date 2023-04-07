"""
https://www.acmicpc.net/problem/4781
4781.사탕 가게
골드5
풀이1.X
"""
import sys

sys.setrecursionlimit(10 ** 6)


def solve(n, m):
    if n == 0 or m == 0:
        return 0

    if (n, m) not in cache:
        cache[(n, m)] = solve(n - 1, m)

        if W[n] <= m:
            cache[(n, m)] = max(cache[(n, m)], solve(n - 1, m - W[n]) + V[n])
            cache[(n, m)] = max(cache[(n, m)], solve(n, m - W[n]) + V[n])

    return cache[(n, m)]


input = sys.stdin.readline

while True:
    N, M = input().rstrip().split()
    N = int(N)
    M = float(M)
    if N == 0 and M == 0.00:
        break

    cache = dict()
    V = [0]
    W = [0]
    for _ in range(N):
        v, w = input().rstrip().split()
        V.append(int(v))
        W.append(float(w))

    print(solve(N, M))
