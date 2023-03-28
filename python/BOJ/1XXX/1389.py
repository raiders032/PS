"""
https://www.acmicpc.net/problem/1389
1389.케빈 베이컨의 6단계 법칙
풀이2.64ms
"""
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list() for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

answer = sys.maxsize
min_beacon = sys.maxsize

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    visited[i] = True
    queue = deque([(i, 0)])
    beacon = 0

    while queue:
        vertex, distance = queue.popleft()
        beacon += distance
        for next_vertex in graph[vertex]:
            if visited[next_vertex]:
                continue
            visited[next_vertex] = True
            queue.append((next_vertex, distance + 1))

    if beacon < min_beacon:
        min_beacon = beacon
        answer = i

print(answer)