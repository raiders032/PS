"""
https://www.acmicpc.net/problem/20924
20924.트리의 기둥과 가지
풀이1.980ms
"""
import sys
from collections import deque

input = sys.stdin.readline


def find_giga_node():
    queue = deque([r])
    visited[r] = 0

    while queue:
        current_node = queue.popleft()
        out_degree = 0

        for next_node, weight in graph[current_node]:
            if visited[next_node] != -1:
                continue
            out_degree += 1

        if out_degree != 1:
            return current_node

        for next_node, weight in graph[current_node]:
            if visited[next_node] != -1:
                continue

            visited[next_node] = visited[current_node] + weight
            queue.append(next_node)


n, r = map(int, input().split())
graph = [list() for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(n - 1):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))

giga_node = find_giga_node()
answer = [str(visited[giga_node])]
queue = deque([giga_node])
length = 0
visited[giga_node] = 0

while queue:
    current_node = queue.popleft()
    length = max(length, visited[current_node])

    for next_node, weight in graph[current_node]:
        if visited[next_node] != -1:
            continue

        visited[next_node] = visited[current_node] + weight
        queue.append(next_node)

answer.append(str(length))
print(" ".join(answer))