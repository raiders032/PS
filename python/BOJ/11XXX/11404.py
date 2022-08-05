"""
https://www.acmicpc.net/problem/11404
11404.플로이드
풀이2.704ms
"""
import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [list() for _ in range(N)]
dist = [[sys.maxsize] * N for _ in range(N)]  # 무한으로 인접행렬 초기화

for i in range(N):
    dist[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    dist[a - 1][b - 1] = min(dist[a - 1][b - 1], c)

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(N):
    for d in dist[i]:
        if d == sys.maxsize:
            print(0, end=' ')
        else:
            print(d, end=' ')
    print()