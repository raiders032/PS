"""
https://www.acmicpc.net/problem/1939
1939.중량제한
풀이1.
"""
import sys
import collections


def is_valid(weight):
    visited = [False] * (N + 1)
    q = collections.deque()
    q.append(start)
    visited[start] = True
    while q:
        vertex = q.popleft()
        if vertex == end:
            return True
        for next_vertex, next_weight in graph[vertex]:
            if next_weight < weight:
                continue
            if visited[next_vertex]:
                continue
            q.append((next_vertex))
    return False


input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list() for _ in range(N + 1)]
for _ in range(M):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))

start, end = map(int, input().split())
low = 1
high = 1_000_000_000
sheep_count = 0

while low <= high:
    weight = (low + high) // 2
    if is_valid(weight):
        low = weight + 1
        sheep_count = weight
    else:
        high = weight - 1

print(weight)