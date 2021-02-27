"""
15685.드래곤 커브
골드4
구현,시뮬레이션
풀이1.72ms
"""
import sys

input = sys.stdin.readline
N = int(input())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
board = [[False] * 101 for _ in range(101)]
res = 0

for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon_curve = [d]

    for _ in range(g):
        for dir in dragon_curve[::-1]:
            dragon_curve.append((dir + 1) % 4)

    board[y][x] = True
    for dir in dragon_curve:
        x += dx[dir]
        y += dy[dir]
        board[y][x] = True

for i in range(100):
    for j in range(100):
        if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
            res += 1
print(res)
