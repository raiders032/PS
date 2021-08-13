"""
https://www.acmicpc.net/problem/1520
1520.내리막 길
골드4
풀이1.192ms
"""
import sys
sys.setrecursionlimit(10**6)


def solve(x, y):
    if x == N - 1 and y == M - 1:
        return 1

    if cache[x][y] == -1:
        cache[x][y] = 0

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[x][y] <= board[nx][ny]:
                continue
            cache[x][y] += solve(nx, ny)

    return cache[x][y]


input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cache = [[-1] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
print(solve(0, 0))