"""
https://www.acmicpc.net/problem/16929
16929번 Two Dots
골드4
깊이우선탐색,그래프이론,그래프탐색
풀이2.140ms
"""
import sys


def is_cycle(level, start_x, start_y, current_x, current_y):
    for direction in range(4):
        next_x = current_x + dx[direction]
        next_y = current_y + dy[direction]

        if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
            continue

        if board[current_x][current_y] != board[next_x][next_y]:
            continue

        if level >= 3 and next_x == start_x and next_y == start_y:
            return True

        if visited[next_x][next_y]:
            continue

        visited[next_x][next_y] = True
        if is_cycle(level + 1, start_x, start_y, next_x, next_y):
            return True
        visited[next_x][next_y] = False

    return False


input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for x in range(N):
    for y in range(M):
        visited[x][y] = True
        if is_cycle(0, x, y, x , y):
            print('Yes')
            exit(0)
        visited[x][y] = False

print('No')