"""
https://www.acmicpc.net/problem/2636
2636.치즈
골드4
풀이1.144ms
"""
import sys
import collections
input = sys.stdin.readline


def melt_cheese(x, y):
    is_air = False
    q = collections.deque()
    q.append((x, y))
    visited[x][y] = True
    cheese_to_melt = set()

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                is_air = True
                continue

            if visited[nx][ny]:
                continue

            if board[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
            else:
                cheese_to_melt.add((nx, ny))

    if is_air:
        for x, y in cheese_to_melt:
            board[x][y] = 0
        return len(cheese_to_melt)
    else:
        return 0


N, M = map(int, input().split())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
cheese_count = 0
pre_count = 0
seconds = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            cheese_count += 1

while cheese_count:
    visited = [[False] * M for _ in range(N)]
    pre_count = cheese_count
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 or visited[i][j]:
                continue

            cheese_count -= melt_cheese(i, j)

    seconds += 1

print(seconds)
print(pre_count)