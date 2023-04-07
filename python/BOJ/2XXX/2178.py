"""
https://www.acmicpc.net/problem/2178
2178.미로 탐색
실버1
풀이2.108ms
"""
import sys
import collections
input = sys.stdin.readline


def get_min_distance():
    q = collections.deque()
    visited[0][0] = 1
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                continue
            if visited[nx][ny] or not board[nx][ny]:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))


N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
get_min_distance()
print(visited[N - 1][M - 1])