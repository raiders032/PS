"""
https://www.acmicpc.net/problem/1753
1753.최단경로
풀이1.744ms
"""
import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
source_vertex = int(input())
graph = [list() for _ in range(V + 1)]

for _ in range(E):
    vertex1, vertex2, weight = map(int, input().split())
    graph[vertex1].append((vertex2, weight))

min_distance = [sys.maxsize] * (V + 1)
min_distance[source_vertex] = 0

min_heap = [(0, source_vertex)]

while min_heap:
    distance, vertex = heapq.heappop(min_heap)

    if min_distance[vertex] < distance:
        continue

    for next_vertex, weight in graph[vertex]:
        if distance + weight < min_distance[next_vertex]:
            min_distance[next_vertex] = distance + weight
            heapq.heappush(min_heap, (min_distance[next_vertex], next_vertex))

for distance in min_distance[1:]:
    if distance == sys.maxsize:
        print("INF")
        continue
    print(distance)