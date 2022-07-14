"""
https://www.acmicpc.net/problem/1992
1992.쿼드트리
실버1
풀이1.80ms
"""
import sys

input = sys.stdin.readline


def solve(x, y, length):
    wb = board[x][y]
    is_valid = True
    for i in range(x, x + length):
        for j in range(y, y + length):
            if board[i][j] != wb:
                is_valid = False
                break
        if not is_valid:
            break
    if is_valid:
        print(wb, end='')
    else:
        print('(', end='')
        unit = length // 2
        solve(x, y, unit)
        solve(x, y + unit, unit)
        solve(x + unit, y, unit)
        solve(x + unit, y + unit, unit)
        print(')', end='')


N = int(input())
board = [list(map(int, input().rstrip())) for _ in range(N)]
solve(0, 0, N)
