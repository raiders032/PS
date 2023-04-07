"""
https://www.acmicpc.net/problem/11724
11724.연결 요소의 개수
실버2
풀이3.808ms
"""
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(v):
    visited[v] = True

    for w in graph[v]:
        if visited[w]:
            continue
        dfs(w)


input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list() for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

sheep_count = 0
for v in range(1, N + 1):
    if visited[v]:
        continue
    sheep_count += 1
    dfs(v)
print(sheep_count)


