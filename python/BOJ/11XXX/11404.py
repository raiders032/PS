"""
https://www.acmicpc.net/problem/11404
11404.플로이드
골드4
풀이1.1000ms
"""
import sys

input = sys.stdin.readline
INF = sys.maxsize
V = int(input())
E = int(input())
dist = [[INF] * V for _ in range(V)]

for _ in range(E):
    v, w, d = map(int, input().split())
    dist[v - 1][w - 1] = min(dist[v - 1][w - 1], d)

for k in range(V):
    for i in range(V):
        for j in range(V):
            if i == j:
                continue
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(V):
    for num in dist[i]:
        print(num if num != INF else 0, end=' ')
    print()