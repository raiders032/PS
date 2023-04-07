"""
https://www.acmicpc.net/problem/2239
2239.스도쿠
풀이1.
"""
import sys

input = sys.stdin.readline


def is_row_valid(i, number):
    for j in range(9):
        if sudoku[i][j] == number:
            return False
    return True


def is_column_valid(j, number):
    for i in range(9):
        if sudoku[i][j] == number:
            return False
    return True


def is_square_valid(i, j, number):
    for i in range(i // 3 * 3, i // 3 * 3 + 3):
        for j in range(j // 3 * 3, j // 3 * 3 + 3):
            if sudoku[i][j] == number:
                return False
    return True


def solve(index):
    if index == len(empty_cell):
        for i in range(9):
            print(''.join(map(str, sudoku[i])))
        return True

    x = empty_cell[index][0]
    y = empty_cell[index][1]

    for number in range(1, 10):
        if not is_row_valid(x, number):
            continue
        if not is_column_valid(y, number):
            continue
        if not is_square_valid(x, y, number):
            continue
        sudoku[x][y] = number
        if solve(index + 1):
            return True
        sudoku[x][y] = 0


sudoku = [[0] * 9 for _ in range(9)]
empty_cell = []
for i in range(9):
    for j, number in enumerate(map(int, input().rstrip())):
        sudoku[i][j] = number
        if number == 0:
            empty_cell.append((i, j))

solve(0)
