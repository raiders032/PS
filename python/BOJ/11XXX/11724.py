"""
11724.연결 요소의 개수
실버2
BFS, DFS, 그래프이론, 그래프탐색
풀이1.948ms
"""
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)


N, M = map(int, input().split())
graph = [list() for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

for i in range(1, N + 1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)