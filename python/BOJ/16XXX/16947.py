"""
https://www.acmicpc.net/problem/16947
16947.서울 지하철 2호선
골드3
그래프이론,그래프탐색,DFS,BFS
풀이1.1812ms
"""

import sys
from collections import deque
sys.setrecursionlimit(100000)

def is_circular_path(level, start_vertex, cur_vertex):
    for next_vertex in graph[cur_vertex]:
        if level > 1 and next_vertex == start_vertex:
            return True

        if visited[next_vertex]:
            continue

        visited[next_vertex] = True
        circular_path.append(next_vertex)

        if is_circular_path(level + 1, start_vertex, next_vertex):
            return True

        visited[next_vertex] = False
        circular_path.pop()


def get_distance(vertex):
    visited = [0] * (N + 1)
    que = deque([vertex])
    visited[vertex] = 1

    while que:
        vertex = que.popleft()
        for next_vertex in graph[vertex]:
            if visited[next_vertex] or next_vertex in circular_path:
                continue
            visited[next_vertex] = visited[vertex] + 1
            distance[next_vertex] = visited[vertex]
            que.append(next_vertex)



input = sys.stdin.readline
N = int(input())
graph = [list() for _ in range(N + 1)]
visited = [0] * (N + 1)
distance = [0] * (N + 1)
circular_path = []

for _ in range(N):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for vertex in range(1, N + 1):
    visited = [0] * (N + 1)
    circular_path = [vertex]
    visited[vertex] = 1
    if is_circular_path(0, vertex, vertex):
        break

circular_path = set(circular_path)
for vertex in circular_path:
    if len(graph[vertex]) > 2:
        get_distance(vertex)

print(*distance[1:])