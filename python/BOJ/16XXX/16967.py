"""
16967.배열 복원하기
실버3
풀이1.152ms
"""
import sys

input = sys.stdin.readline
H, W, X, Y = map(int, input().split())
arrs = [list(map(int, input().split())) for _ in range(H + X)]

for x in range(H - X):
    for y in range(W - Y):
        arrs[x + X][y + Y] -= arrs[x][y]

for i in range(H):
    print(*arrs[i][0:W])
