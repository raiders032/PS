"""
https://www.acmicpc.net/problem/11724
11724.연결 요소의 개수
실버2
풀이2.848ms
"""
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if visited[next_v]:
            continue
        dfs(next_v)


input = sys.stdin.readline
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


