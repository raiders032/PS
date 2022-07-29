"""
https://www.acmicpc.net/problem/16928
16928.뱀과 사다리 게임
풀이3.100ms
"""
import sys
import collections

input = sys.stdin.readline

N, M = map(int, input().split())
jump = dict()
for _ in range(N + M):
    start, end = map(int, input().split())
    jump[start] = end

visited = [-1] * 101
visited[1] = 0
q = collections.deque()
q.append(1)
while q:
    vertex = q.popleft()

    if vertex == 100:
        print(visited[100])
        break

    for i in range(1, 7):
        next_vertex = vertex + i
        if next_vertex > 100 or visited[next_vertex] != -1:
            continue

        visited[next_vertex] = visited[vertex] + 1
        q.append(next_vertex)

        while next_vertex in jump:
            q.pop()
            if visited[jump[next_vertex]] == -1:
                visited[jump[next_vertex]] = visited[vertex] + 1
                q.append(jump[next_vertex])
            next_vertex = jump[next_vertex]
