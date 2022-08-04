"""
https://www.acmicpc.net/problem/14567
14567.선수과목 (Prerequisite)
풀이1.728ms
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list() for _ in range(N + 1)]
inDegree = [0] * (N + 1)
queue = deque()
result = [0] * (N + 1)

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    inDegree[v2] += 1

for i in range(1, N + 1):
    if inDegree[i] == 0:
        queue.append((i, 1))


for _ in range(N):
    if not queue:
        print('사이클 발생')
        break

    vertex, semester = queue.popleft()
    result[vertex] = semester
    for next_vertex in graph[vertex]:
        inDegree[next_vertex] -= 1
        if inDegree[next_vertex] == 0:
            queue.append((next_vertex, semester + 1))

print(*result[1:])