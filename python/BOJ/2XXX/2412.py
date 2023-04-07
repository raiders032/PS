"""
https://www.acmicpc.net/problem/2412
2412.암벽 등반
풀이2.496ms
"""
import sys
from collections import deque

input = sys.stdin.readline

n, t = map(int, input().split())
locations = set(tuple(map(int, input().split())) for _ in range(n))

q = deque()
visited = set()
visited.add((0, 0))
q.append((0, 0, 0))
sheep_count = -1
while q:
    x, y, count = q.popleft()

    if y == t:
        sheep_count = count
        break

    for nx in range(x - 2, x + 3):
        for ny in range(y - 2, y + 3):
            if (nx, ny) not in locations or (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            q.append((nx, ny, count + 1))

print(sheep_count)
"""
2 4
2 2
0 4
"""
