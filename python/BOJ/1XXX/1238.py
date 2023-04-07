"""
https://www.acmicpc.net/problem/1238
1238.파티
골드3
풀이1.4248ms
"""
import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    visited = [False] * (N + 1)
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        distance, vertex = heapq.heappop(heap)
        if visited[vertex]:
            continue
        visited[vertex] = True
        min_distances[start][vertex] = distance

        for v, d in graph[vertex]:
            heapq.heappush(heap, (distance + d, v))


N, M, X = map(int, input().split())
graph = [list() for _ in range(N + 1)]
min_distances = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))

for i in range(1, N + 1):
    dijkstra(i)

sheep_count = 0
for i in range(1, N + 1):
    sheep_count = max(sheep_count, min_distances[i][X] + min_distances[X][i])

print(sheep_count)
