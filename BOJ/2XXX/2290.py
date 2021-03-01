"""
2290.LCD Test
실버2
구현
풀이1. 68ms
"""
import sys


def paint_1(idx, num):
    if num == 1 or num == 4:
        return
    for i in range(s):
        lcd[0][idx * (s + 3) + 1 + i] = '-'


def paint_2(idx, num):
    if num == 1 or num == 2 or num == 3 or num == 7:
        for i in range(s):
            lcd[1 + i][idx * (s + 3) + s + 1] = '|'
    elif num == 5 or num == 6:
        for i in range(s):
            lcd[1 + i][idx * (s + 3)] = '|'
    else:
        for i in range(s):
            lcd[1 + i][idx * (s + 3)] = '|'
            lcd[1 + i][idx * (s + 3) + s + 1] = '|'


def paint_3(idx, num):
    if num == 0 or num == 1 or num == 7:
        return
    for i in range(s):
        lcd[s + 1][idx * (s + 3) + 1 + i] = '-'


def paint_4(idx, num):
    if num == 1 or num == 3 or num == 4 or num == 5 or num == 7 or num == 9:
        for i in range(s):
            lcd[s + 2 + i][idx * (s + 3) + s + 1] = '|'
    elif num == 2:
        for i in range(s):
            lcd[s + 2 + i][idx * (s + 3)] = '|'
    else:
        for i in range(s):
            lcd[s + 2 + i][idx * (s + 3)] = '|'
            lcd[s + 2 + i][idx * (s + 3) + s + 1] = '|'


def paint_5(idx, num):
    if num == 1 or num == 4 or num == 7:
        return
    for i in range(s):
        lcd[2 * s + 2][idx * (s + 3) + 1 + i] = '-'


input = sys.stdin.readline
s, n = map(int, input().split())
num = list(map(int, str(n)))
length = len(num)
N = 2 * s + 3
M = (s + 3) * length
lcd = [[' '] * M for _ in range(N)]

for i in range(length):
    paint_1(i, num[i])
    paint_2(i, num[i])
    paint_3(i, num[i])
    paint_4(i, num[i])
    paint_5(i, num[i])

for i in range(N):
    for j in range(M):
        print(lcd[i][j], end='')
    print()
