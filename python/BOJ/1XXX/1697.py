"""
https://www.acmicpc.net/problem/1697
1697.숨바꼭질
풀이2.148ms
"""
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001
queue = deque()

visited[n] = True
queue.append((n, 0))

while queue:
    x, distance = queue.popleft()
    if x == k:
        print(distance)
        break

    for dx in [1, -1, x]:
        nx = x + dx
        if nx < 0 or nx >= 100001 or visited[nx]:
            continue

        visited[nx] = True
        queue.append((nx, distance + 1))