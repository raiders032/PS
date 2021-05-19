"""
https://www.acmicpc.net/problem/5014
5014.스타트링크
골드5
BFS
풀이1
"""
import sys
from collections import deque


def solve():
    visited = [0] * (F + 1)
    q = deque([S])
    visited[S] = 1
    while q:
        current = q.popleft()
        if current == G:
            return visited[current] - 1

        up = current + U
        if up <= F and not visited[up]:
            visited[up] = visited[current] + 1
            q.append(up)

        down = current - D
        if down >= 1 and not visited[down]:
            visited[down] = visited[current] + 1
            q.append(down)

    return -1


input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
result = solve()

if result == -1:
    print("use the stairs")
else:
    print(result)

