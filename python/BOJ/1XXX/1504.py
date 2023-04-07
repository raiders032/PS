"""
https://www.acmicpc.net/problem/1504
1504.특정한 최단 경로
풀이1.492ms
"""
import sys
import heapq

input = sys.stdin.readline


def get_min_distance(vertex):
    min_distance = [sys.maxsize] * (N + 1)
    visited = [False] * (N + 1)
    min_distance[vertex] = 0
    min_heap = [(0, vertex)]

    while min_heap:
        weight, vertex = heapq.heappop(min_heap)
        if visited[vertex]:
            continue
        visited[vertex] = True
        for next_vertex, next_weight in graph[vertex]:
            if min_distance[vertex] + next_weight < min_distance[next_vertex]:
                min_distance[next_vertex] = min_distance[vertex] + next_weight
                heapq.heappush(min_heap, (min_distance[next_vertex], next_vertex))

    return min_distance


N, E = map(int, input().split())
graph = [list() for _ in range(N + 1)]
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))

mid1, mid2 = map(int, input().split())
start = get_min_distance(1)
intermediate1 = get_min_distance(mid1)
intermediate2 = get_min_distance(mid2)

sheep_count = sys.maxsize
if start[mid1] != sys.maxsize and intermediate1[mid2] != sys.maxsize and intermediate2[N] != sys.maxsize:
    sheep_count = start[mid1] + intermediate1[mid2] + intermediate2[N]
if start[mid2] != sys.maxsize and intermediate2[mid1] != sys.maxsize and intermediate1[N] != sys.maxsize:
    sheep_count = min(sheep_count, start[mid2] + intermediate2[mid1] + intermediate1[N])

print(sheep_count if sheep_count != sys.maxsize else -1)
