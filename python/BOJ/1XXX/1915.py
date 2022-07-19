"""
https://www.acmicpc.net/problem/1915
1915.가장 큰 정사각형
풀이1.4572ms
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
x, y, length = 0, 0, 1
answer = 0

while True:
    is_valid = True
    if x + length > N:
        break

    if y + length > M:
        y = 0
        x = x + 1
        continue

    for i in range(x, x + length):
        for j in range(y, y + length):
            if board[i][j] != 1:
                is_valid = False
                break
        if not is_valid:
            break
    if is_valid:
        answer = length
        length += 1
        continue

    y += 1

print(answer ** 2)

"""
3 3
000
000
100

"""