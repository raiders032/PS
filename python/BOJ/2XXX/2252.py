"""
https://www.acmicpc.net/problem/2252
2252.줄 세우기
풀이1.260ms
"""
import sys
from collections import deque
input = sys.stdin.readline

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list() for _ in range(N + 1)]
inDegree = [0] * (N + 1)
queue = deque()
result = []

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    inDegree[v2] += 1

for i in range(1, N + 1):
    if inDegree[i] == 0:
        queue.append(i)

for _ in range(N):
    if not queue:
        print('사이클 발생')
        break

    vertex = queue.popleft()
    result.append(vertex)

    for next_vertex in graph[vertex]:
        inDegree[next_vertex] -= 1
        if inDegree[next_vertex] == 0:
            queue.append(next_vertex)

print(*result)