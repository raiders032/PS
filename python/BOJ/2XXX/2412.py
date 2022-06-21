"""
https://www.acmicpc.net/problem/2412
2412.암벽 등반
골드3
풀이1.608ms
"""
import collections
import sys
input = sys.stdin.readline


def bfs():
    visited = collections.defaultdict(int)
    q = collections.deque()
    q.append((0, 0))
    visited[(0, 0)] = 1

    while q:
        x, y = q.popleft()

        if y == T:
            return visited[(x, y)] - 1

        for dx in range(-2, 3):
            for dy in range(-2, 3):
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx > 1000000 or ny < 0 or ny > T:
                    continue
                if (nx, ny) not in x_y:
                    continue
                if visited[(nx, ny)]:
                    continue
                visited[(nx, ny)] = visited[(x, y)] + 1
                q.append((nx, ny))

    return -1


N, T = map(int, input().split())
x_y = set()
for _ in range(N):
    x, y = map(int, input().split())
    x_y.add((x, y))

print(bfs())

"""
2 4
2 2
0 4
"""