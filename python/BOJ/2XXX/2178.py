"""
https://www.acmicpc.net/problem/2178
2178.미로 탐색
실버1
풀이1.108ms
"""
import sys
import collections
input = sys.stdin.readline


def get_min_distance():
    visited[0][0] = 1
    q = collections.deque()
    q.append((0, 0))
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y = q.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not board[nx][ny] or visited[nx][ny]:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))


N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
print(get_min_distance())



