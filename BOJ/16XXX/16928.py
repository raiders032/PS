"""
https://www.acmicpc.net/problem/16928
16928.뱀과 사다리 게임
실버2
BFS
풀이1. 1336ms
"""

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
jump = dict()
visited = [0] * (101)


def bfs(x):
    q = deque()
    visited[x] = 1
    q.append(x)
    while q:
        x = q.popleft()
        if x == 100:
            return visited[x] - 1
        if x in jump:
            nx = jump[x]
            if visited[nx] and visited[nx] < visited[x]:
                continue
            visited[nx] = visited[x]
            q.appendleft(nx)
        else:
            for nx in range(x+1, x+7):
                if nx > 100 or (visited[nx] and visited[nx] < visited[x] + 1):
                    continue
                visited[nx] = visited[x] + 1
                q.append(nx)


for _ in range(N+M):
    x, y = map(int, sys.stdin.readline().split())
    jump[x] = y

print(bfs(1))
