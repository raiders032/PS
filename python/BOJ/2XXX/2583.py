"""
https://www.acmicpc.net/problem/2583
2583.영역 구하기
실버1
풀이1.96ms
"""
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def get_area(y, x):
    visited[y][x] = True
    count = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visited[ny][nx] or board[ny][nx] == 1:
            continue

        count += get_area(ny, nx)

    return count


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

ans = []
for y in range(M):
    for x in range(N):
        if visited[y][x] or board[y][x] == 1:
            continue
        ans.append(get_area(y, x))

ans.sort()
print(len(ans))
print(*ans)