"""
https://www.acmicpc.net/problem/1956
1956.운동
풀이1.1808ms(PyPy3)
"""
import sys
import heapq
input = sys.stdin.readline


def get_min_distance(start):
    q = [(0, start)]
    min_distance[start][start] = 0

    while q:
        weight, vertex = heapq.heappop(q)
        if min_distance[start][vertex] < weight:
            continue

        for next_vertex, next_weight in graph[vertex]:
            if min_distance[start][next_vertex] <= weight + next_weight:
                continue
            min_distance[start][next_vertex] = weight + next_weight
            heapq.heappush(q, (weight + next_weight, next_vertex))


V, E = map(int, input().split())
graph = [list() for _ in range(V + 1)]
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
min_distance = [[sys.maxsize] * (V + 1) for _ in range(V + 1)]

for i in range(1, V + 1):
    get_min_distance(i)

sheep_count = sys.maxsize
for i in range(1, V + 1):
    for j in range(i + 1, V + 1):
        if min_distance[i][j] == -1 or min_distance[j][i] == -1:
            continue
        sheep_count = min(sheep_count, min_distance[i][j] + min_distance[j][i])
print(sheep_count if sheep_count != sys.maxsize else -1)