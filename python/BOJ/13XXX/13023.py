"""
13023.ABCDE
골드5
DFS, BFS, 그래프탐색
"""
import sys


def dfs(level, v):
    visited[v] = True
    if level == 4:
        print(1)
        exit(0)
    for next_v in graph[v]:
        if visited[next_v]:
            continue
        dfs(level + 1, next_v)
        visited[next_v] = False


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
visited = [False] * N
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(N):
    dfs(0, i)
    visited[i] = False
print(0)
