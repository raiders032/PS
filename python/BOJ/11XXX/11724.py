"""
11724.연결 요소의 개수
실버2
BFS, DFS, 그래프이론, 그래프탐색
"""
import sys

sys.setrecursionlimit(100000)

def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if visited[next_v]:
            continue
        dfs(next_v)


input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * N
cnt = 0
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1 - 1].append(v2 - 1)
    graph[v2 - 1].append(v1 - 1)
for i in range(N):
    if not visited[i]:
        cnt += 1
        dfs(i)
print(cnt)
