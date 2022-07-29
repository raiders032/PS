"""
https://www.acmicpc.net/problem/1992
1992.쿼드트리
풀이2.76ms
"""
import sys

input = sys.stdin.readline


def get_quad_tree(x, y, length):
    target = board[x][y]
    is_valid = True

    for i in range(x, x + length):
        for j in range(y, y + length):
            if target != board[i][j]:
                is_valid = False
                break
        if not is_valid:
            break

    if is_valid:
        print(target, end='')
    else:
        unit = length // 2
        print("(", end='')
        get_quad_tree(x, y, unit)
        get_quad_tree(x, y + unit, unit)
        get_quad_tree(x + unit, y, unit)
        get_quad_tree(x + unit, y + unit, unit)
        print(")", end='')


n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
get_quad_tree(0, 0, n)
