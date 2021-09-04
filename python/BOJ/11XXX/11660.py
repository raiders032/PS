"""
https://www.acmicpc.net/problem/11660
11660.구간 합 구하기 5
실버1
풀이1.1496ms
"""
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sum = [[0] * N for _ in range(N)]
for x in range(N):
    for y in range(N):
        sum[x][y] = board[x][y] + (sum[x][y - 1] if y else 0)

for x in range(1, N):
    for y in range(N):
        sum[x][y] += sum[x - 1][y]

for _ in range(M):
    x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())
    answer = sum[x2][y2]
    if x1:
        answer -= sum[x1 - 1][y2]
    if y1:
        answer -= sum[x2][y1 - 1]
    if x1 and y1:
        answer += sum[x1 - 1][y1 - 1]
    print(answer)